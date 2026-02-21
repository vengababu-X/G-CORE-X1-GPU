// =====================================================
// SIMD ALU
// =====================================================
module simd_alu #(
    parameter LANES = 4
)(
    input  wire               clk,
    input  wire               reset,
    input  wire [1:0]         op,
    input  wire [32*LANES-1:0] a,
    input  wire [32*LANES-1:0] b,
    output reg  [32*LANES-1:0] result
);
integer i;
always @(posedge clk) begin
    if (reset)
        result <= 0;
    else begin
        for (i=0;i<LANES;i=i+1)
            case(op)
                2'b00: result[i*32 +:32] <= a[i*32 +:32] + b[i*32 +:32];
                2'b01: result[i*32 +:32] <= a[i*32 +:32] * b[i*32 +:32];
                default: result[i*32 +:32] <= 0;
            endcase
    end
end
endmodule

// =====================================================
// VECTOR REGISTER FILE
// =====================================================
module vector_regfile #(
    parameter LANES = 4
)(
    input wire clk,
    input wire we,
    input wire [2:0] waddr,
    input wire [32*LANES-1:0] wdata,
    input wire [2:0] raddr,
    output wire [32*LANES-1:0] rdata
);
reg [32*LANES-1:0] regs [0:7];
initial begin
    regs[1] = {32'd4,3,2,1};
    regs[2] = {32'd40,30,20,10};
end
always @(posedge clk)
    if (we) regs[waddr] <= wdata;
assign rdata = regs[raddr];
endmodule

// =====================================================
// DATA MEMORY (LAYER 4)
// =====================================================
module data_memory #(
    parameter LANES = 4
)(
    input wire clk,
    input wire we,
    input wire [7:0] addr,
    input wire [32*LANES-1:0] wdata,
    output reg [32*LANES-1:0] rdata
);
reg [32*LANES-1:0] mem [0:255];
initial begin
    mem[8] = {32'd1,2,3,4};
end
always @(posedge clk) begin
    if (we) mem[addr] <= wdata;
    rdata <= mem[addr];
end
endmodule

// =====================================================
// GPU CORE — LAYER 4
// =====================================================
module simd_gpu_core(
    input wire clk,
    input wire reset
);

reg [3:0] pc;
reg [15:0] imem [0:7];

// Program:
// LOAD  R3, [8]
// ADD   R4 = R3 + R1
// STORE R4 -> [9]
initial begin
    imem[0] = {2'b10,3'd3,3'd0,8'd8}; // LOAD
    imem[1] = {2'b00,3'd4,3'd3,8'd0}; // ADD
    imem[2] = {2'b11,3'd4,3'd0,8'd9}; // STORE
end

wire [15:0] instr = imem[pc];
wire [1:0] opcode = instr[15:14];
wire [2:0] rd = instr[13:11];
wire [2:0] rs = instr[10:8];
wire [7:0] imm = instr[7:0];

wire [127:0] reg_out, alu_out, mem_out;

vector_regfile rf(
    .clk(clk),
    .we(opcode!=2'b11 && !reset),
    .waddr(rd),
    .wdata(opcode==2'b10 ? mem_out : alu_out),
    .raddr(rs),
    .rdata(reg_out)
);

data_memory dmem(
    .clk(clk),
    .we(opcode==2'b11),
    .addr(imm),
    .wdata(reg_out),
    .rdata(mem_out)
);

simd_alu alu(
    .clk(clk),
    .reset(reset),
    .op(opcode),
    .a(reg_out),
    .b(reg_out),
    .result(alu_out)
);

always @(posedge clk)
    if (reset) pc <= 0;
    else pc <= pc + 1;

endmodule
