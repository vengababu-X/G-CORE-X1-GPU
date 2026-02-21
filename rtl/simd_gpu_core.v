module simd_gpu_core #(
    parameter LANES = 4
)(
    input  wire clk,
    input  wire reset,
    input  wire [15:0] instruction,      // simple 16-bit instruction
    input  wire [32*LANES-1:0] src_a,
    input  wire [32*LANES-1:0] src_b,
    output wire [32*LANES-1:0] result
);

// Instruction format:
// [15:14] opcode
// 00 = ADD
// 01 = MUL

wire [1:0] opcode;

assign opcode = instruction[15:14];

simd_alu #(
    .LANES(LANES)
) alu (
    .clk(clk),
    .reset(reset),
    .op(opcode),
    .a(src_a),
    .b(src_b),
    .result(result)
);

endmodule
