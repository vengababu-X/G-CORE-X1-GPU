module vector_regfile #(
    parameter LANES = 4,
    parameter REGS  = 8
)(
    input  wire               clk,
    input  wire               we,          // write enable
    input  wire [2:0]         waddr,       // write register
    input  wire [32*LANES-1:0] wdata,       // write data

    input  wire [2:0]         raddr_a,     // read reg A
    input  wire [2:0]         raddr_b,     // read reg B
    output wire [32*LANES-1:0] rdata_a,
    output wire [32*LANES-1:0] rdata_b
);

reg [32*LANES-1:0] regs [0:REGS-1];

// synchronous write
always @(posedge clk) begin
    if (we) begin
        regs[waddr] <= wdata;
    end
end

// combinational read
assign rdata_a = regs[raddr_a];
assign rdata_b = regs[raddr_b];

endmodule
