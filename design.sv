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
        for (i = 0; i < LANES; i = i + 1) begin
            case (op)
                2'b00: result[i*32 +: 32] <= a[i*32 +: 32] + b[i*32 +: 32];
                2'b01: result[i*32 +: 32] <= a[i*32 +: 32] * b[i*32 +: 32];
                default: result[i*32 +: 32] <= 32'd0;
            endcase
        end
    end
end

endmodule


// =====================================================
// VECTOR REGISTER FILE
// =====================================================
module vector_regfile #(
    parameter LANES = 4,
    parameter REGS  = 8
)(
    input  wire               clk,
    input  wire               we,
    input  wire [2:0]         waddr,
    input  wire [32*LANES-1:0] wdata,
    input  wire [2:0]         raddr_a,
    input  wire [2:0]         raddr_b,
    output wire [32*LANES-1:0] rdata_a,
    output wire [32*LANES-1:0] rdata_b
);

reg [32*LANES-1:0] regs [0:REGS-1];

// preload registers
initial begin
    regs[1] = {32'd4, 32'd3, 32'd2, 32'd1};
    regs[2] = {32'd40, 32'd30, 32'd20, 32'd10};
end

always @(posedge clk)
    if (we)
        regs[waddr] <= wdata;

assign rdata_a = regs[raddr_a];
assign rdata_b = regs[raddr_b];

endmodule


// =====================================================
// GPU CORE WITH PC + INSTRUCTION MEMORY
// =====================================================
module simd_gpu_core #(
    parameter LANES = 4
)(
    input  wire clk,
    input  wire reset
);

// ---------------- PC ----------------
reg [3:0] pc;

// ---------------- Instruction ROM ----------------
// format:
// [15:14] opcode
// [13:11] rd
// [10:8]  rs1
// [7:5]   rs2

reg [15:0] imem [0:7];

initial begin
    imem[0] = {2'b00, 3'd3, 3'd1, 3'd2, 5'b0}; // ADD R3 = R1 + R2
    imem[1] = {2'b01, 3'd4, 3'd1, 3'd2, 5'b0}; // MUL R4 = R1 * R2
    imem[2] = 16'h0000; // NOP
end

wire [15:0] instruction = imem[pc];

// ---------------- Decode ----------------
wire [1:0] opcode = instruction[15:14];
wire [2:0] rd     = instruction[13:11];
wire [2:0] rs1    = instruction[10:8];
wire [2:0] rs2    = instruction[7:5];

// ---------------- Register File ----------------
wire [32*LANES-1:0] reg_a, reg_b, alu_result;

vector_regfile rf (
    .clk(clk),
    .we(!reset),
    .waddr(rd),
    .wdata(alu_result),
    .raddr_a(rs1),
    .raddr_b(rs2),
    .rdata_a(reg_a),
    .rdata_b(reg_b)
);

// ---------------- ALU ----------------
simd_alu alu (
    .clk(clk),
    .reset(reset),
    .op(opcode),
    .a(reg_a),
    .b(reg_b),
    .result(alu_result)
);

// ---------------- PC update ----------------
always @(posedge clk)
    if (reset)
        pc <= 0;
    else
        pc <= pc + 1;

endmodule
