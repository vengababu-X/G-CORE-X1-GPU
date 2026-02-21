`timescale 1ns/1ps

module tb_simd_gpu_core;

reg clk;
reg reset;

simd_gpu_core dut (
    .clk(clk),
    .reset(reset)
);

always #5 clk = ~clk;

initial begin
    $dumpfile("gpu_layer3.vcd");
    $dumpvars(0, tb_simd_gpu_core);

    clk = 0;
    reset = 1;
    #10 reset = 0;

    #100;
    $finish;
end

endmodule
