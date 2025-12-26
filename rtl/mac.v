module mac (
    input  wire        clk,
    input  wire        rst_n,
    input  wire        valid,
    input  wire [7:0]  a,   // BUG: unsigned
    input  wire [7:0]  b,   // BUG: unsigned
    output reg  [31:0] acc  // BUG: unsigned
);

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        acc <= 32'd0;
    end else if (valid) begin
        acc <= acc + (a * b); // BUG: unsigned math
    end
end

endmodule
