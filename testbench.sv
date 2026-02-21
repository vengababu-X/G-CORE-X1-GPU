`timescale 1ns/1ps
module tb_simd_gpu_core;
reg clk, reset;
simd_gpu_core dut(.clk(clk), .reset(reset));
always #5 clk = ~clk;
initial begin
    $dumpfile("layer4_memory.vcd");
    $dumpvars(0, tb_simd_gpu_core);
    clk=0; reset=1;
    #10 reset=0;
    #120 $finish;
end
endmodule
