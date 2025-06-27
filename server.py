from pathlib import Path
from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Proposal Management System", "1.0.0")

@mcp.tool()
def list_proposal() -> List[str]:
    p = Path("C:\\Users\\dinesh_subramanian\\Documents\\uploads")
    if not p.is_dir():
        raise ValueError(f"Invalid directory: {directory}")
    return [f.name for f in p.iterdir() if f.is_file()]

@mcp.tool()
def read_proposal(filepath: str) -> str:
    p = Path(filepath)
    if not p.is_file():
        raise ValueError(f"Invalid file: {filepath}")
    return p.read_text(encoding="utf-8")

if __name__ == "__main__":
    mcp.run("stdio")