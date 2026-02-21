``timescale 1ns/1ps

module tb_simd_gpu_core;

reg clk;
reg reset;
reg [15:0] instruction;
wire [127:0] result;

simd_gpu_core dut (
    .clk(clk),
    .reset(reset),
    .instruction(instruction),
    .result_out(result)
);

always #5 clk = ~clk;

initial begin
    $dumpfile("gpu_rf.vcd");
    $dumpvars(0, tb_simd_gpu_core);

    clk = 0;
    reset = 1;
    instruction = 0;

    #10 reset = 0;

    // LOAD R1 and R2 implicitly via initial regfile state
    // (for now, regfile starts with Xs, we just demonstrate flow)

    // ADD R3 = R1 + R2
    instruction = {2'b00, 3'd3, 3'd1, 3'd2, 5'b0};
    #10;
    $display("ADD result written to R3 = %h", result);

    // MUL R4 = R1 * R2
    instruction = {2'b01, 3'd4, 3'd1, 3'd2, 5'b0};
    #10;
    $display("MUL result written to R4 = %h", result);

    $finish;
end

endmodule
