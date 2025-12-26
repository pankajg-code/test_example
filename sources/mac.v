module mac (
    input  wire        clk,
    input  wire        rst_n,
    input  wire        valid,
    input  wire signed [7:0] a,
    input  wire signed [7:0] b,
    output reg  signed [31:0] acc
);

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        acc <= 32'sd0;
    end else if (valid) begin
        acc <= acc + (a * b);
    end
end

endmodule
