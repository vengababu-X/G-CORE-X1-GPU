module simd_alu #(
    parameter LANES = 4
)(
    input  wire               clk,
    input  wire               reset,
    input  wire [1:0]         op,     // 00 = ADD, 01 = MUL
    input  wire [32*LANES-1:0] a,
    input  wire [32*LANES-1:0] b,
    output reg  [32*LANES-1:0] result
);

integer i;

always @(posedge clk) begin
    if (reset) begin
        result <= {32*LANES{1'b0}};
    end else begin
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
