`timescale 1ns/1ps

module tb_simd_core;

reg clk;
reg reset;
reg [1:0] opcode;
reg [127:0] src_a;
reg [127:0] src_b;
wire [127:0] result;

simd_core dut (
    .clk(clk),
    .reset(reset),
    .opcode(opcode),
    .src_a(src_a),
    .src_b(src_b),
    .result(result)
);

always #5 clk = ~clk;

initial begin
    clk = 0;
    reset = 1;
    opcode = 0;
    src_a = 0;
    src_b = 0;

    #10 reset = 0;

    // SIMD ADD test
    src_a = {32'd4, 32'd3, 32'd2, 32'd1};
    src_b = {32'd40, 32'd30, 32'd20, 32'd10};
    opcode = 2'b00;
    #10;
    $display("ADD result (lane3..lane0) = %d %d %d %d",
             result[127:96], result[95:64], result[63:32], result[31:0]);

    // SIMD MUL test
    src_a = {32'd4, 32'd3, 32'd2, 32'd1};
    src_b = {32'd5, 32'd6, 32'd7, 32'd8};
    opcode = 2'b01;
    #10;
    $display("MUL result (lane3..lane0) = %d %d %d %d",
             result[127:96], result[95:64], result[63:32], result[31:0]);

    $finish;
end

endmodule
