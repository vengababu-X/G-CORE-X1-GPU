module processing_element (
    input clk, reset,
    input [15:0] in_a, in_b,
    output reg [15:0] out_a, out_b,
    output reg [31:0] acc
);
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            acc <= 32'b0; out_a <= 16'b0; out_b <= 16'b0;
        end else begin
            acc <= acc + (in_a * in_b);
            out_a <= in_a; out_b <= in_b;
        end
    end
endmodule