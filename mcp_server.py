from mcp.server.fastmcp import FastMCP

from tool_runner import (
    get_customer,
    lookup_order,
    process_refund,
    create_support_ticket
)

mcp = FastMCP("support-agent-tools")

session_state = {
    "verified_customer_id": None,
    "verified_customer_name": None
}


@mcp.tool()
def get_customer_tool(query: str) -> str:
    return get_customer(query, session_state)


@mcp.tool()
def lookup_order_tool(order_id: str) -> str:
    return lookup_order(order_id, session_state)


@mcp.tool()
def process_refund_tool(
    customer_id: str,
    order_id: str,
    amount: float
) -> str:

    return process_refund(
        customer_id,
        order_id,
        amount,
        session_state
    )


@mcp.tool()
def create_support_ticket_tool(
    customer_id: str,
    issue: str
) -> str:

    return create_support_ticket(
        customer_id,
        issue,
        session_state
    )


if __name__ == "__main__":
    mcp.run()