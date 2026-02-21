module simd_core (
    input  wire         clk,
    input  wire         reset,
    input  wire [1:0]   opcode,
    input  wire [127:0] src_a,
    input  wire [127:0] src_b,
    output wire [127:0] result
);

simd_alu #(
    .LANES(4)
) alu (
    .clk(clk),
    .reset(reset),
    .op(opcode),
    .a(src_a),
    .b(src_b),
    .result(result)
);

endmodule
