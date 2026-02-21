module simd_gpu_core #(
    parameter LANES = 4
)(
    input  wire        clk,
    input  wire        reset,
    input  wire [15:0] instruction,
    output wire [32*LANES-1:0] result_out
);

// Instruction format (simple):
// [15:14] opcode   (00=ADD, 01=MUL)
// [13:11] rd
// [10:8]  rs1
// [7:5]   rs2

wire [1:0] opcode;
wire [2:0] rd, rs1, rs2;

assign opcode = instruction[15:14];
assign rd     = instruction[13:11];
assign rs1    = instruction[10:8];
assign rs2    = instruction[7:5];

// Register file wires
wire [32*LANES-1:0] reg_a;
wire [32*LANES-1:0] reg_b;
wire [32*LANES-1:0] alu_result;

// Always write back except reset
wire we = !reset;

// Register File
vector_regfile #(
    .LANES(LANES),
    .REGS(8)
) rf (
    .clk(clk),
    .we(we),
    .waddr(rd),
    .wdata(alu_result),
    .raddr_a(rs1),
    .raddr_b(rs2),
    .rdata_a(reg_a),
    .rdata_b(reg_b)
);

// ALU
simd_alu #(
    .LANES(LANES)
) alu (
    .clk(clk),
    .reset(reset),
    .op(opcode),
    .a(reg_a),
    .b(reg_b),
    .result(alu_result)
);

assign result_out = alu_result;

endmodule
