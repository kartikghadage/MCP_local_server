from fastmcp import FastMCP

mcp = FastMCP("hey server")

@mcp.tool
def sum(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run()