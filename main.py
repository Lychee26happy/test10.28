from fastmcp import FastMCP

mcp = FastMCP("My First MCP Server")


@mcp.tool
def hello(name: str) -> str:
    """根据姓名返回欢迎信息。"""
    return f"Hello, {name}!"


@mcp.tool
def add(a: float, b: float) -> float:
    """计算两个数字之和。"""
    return a + b
