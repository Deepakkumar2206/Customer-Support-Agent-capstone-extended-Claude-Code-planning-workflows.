# Claude Customer Support Production Capstone

A production-style customer support agent built using the Anthropic Claude API and MCP (Model Context Protocol).

This project started as a simple customer lookup agent and was gradually improved by adding customer verification, refund processing, support ticket creation, session management, structured error handling, and MCP tool integration.

---

## Features

- Customer lookup using ID, email, or name
- Order lookup
- Refund processing
- Customer verification before sensitive actions
- Support ticket creation
- Structured error responses
- MCP server integration
- MCP Inspector testing
- Session-based customer verification

---

## Project Structure

```text
claude-customer-support-production-capstone/
│
├── agent.py
├── tools.py
├── tool_runner.py
├── mock_data.py
├── mcp_server.py
├── mcp.json
├── .env
├── .gitignore
├── readme.md
│
└── screenshots/
    ├── 01-mcp-tools-list.png
    ├── 02-support-ticket-tool-input.png
    ├── 03-support-ticket-success.png
    ├── 04-customer-verification-flow.png
    └── 05-refund-processing-success.png
```

---

---

# Key Improvements Made

## 1. Customer Verification

Before processing refunds, the customer must be verified.

```python
if not session_state.get("verified_customer_id"):
    return json.dumps(
        {
            "error": {
                "type": "permission",
                "retryable": False,
                "message":
                "Customer must be verified before refund."
            }
        }
    )
```

### Explanation

This prevents unauthorized users from requesting refunds without first proving their identity.

---

## 2. Session State Management

```python
session_state = {
    "verified_customer_id": None,
    "verified_customer_name": None
}
```

### Explanation

The agent remembers which customer has already been verified during the conversation.

---

## 3. Refund Processing Tool

```python
{
    "name": "process_refund",
    "description": (
        "Process a refund for a verified customer."
    )
}
```

### Explanation

This tool allows the agent to initiate refunds after verification checks are completed.

---

## 4. Support Ticket Creation Tool

```python
{
    "name": "create_support_ticket",
    "description": (
        "Create a support ticket for unresolved issues."
    )
}
```

### Explanation

If a customer issue cannot be solved immediately, the agent can create a support ticket for follow-up.

---

## 5. Support Ticket Generation

```python
ticket_id = f"TICKET-{random.randint(1000,9999)}"
```

### Explanation

Each support ticket receives a unique ticket number.

---

## 6. Structured Error Handling

```python
{
    "error": {
        "type": "validation",
        "retryable": False,
        "message": "Order not found."
    }
}
```

### Explanation

Instead of generic failures, the system returns clear and consistent error messages.

---

## 7. MCP Tool Registration

```python
@mcp.tool()
def get_customer_tool(query: str) -> str:
    return get_customer(query, session_state)
```

### Explanation

This exposes the customer lookup function as an MCP tool.

---

## 8. MCP Server Creation

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("support-agent-tools")
```

### Explanation

Creates the MCP server that can expose tools to MCP-compatible clients.

---

## 9. MCP Configuration

```json
{
  "mcpServers": {
    "support-agent-tools": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```

### Explanation

This configuration tells MCP how to start the server.

---

## 10. MCP Inspector Testing

All tools were tested using MCP Inspector:

- get_customer_tool
- lookup_order_tool
- process_refund_tool
- create_support_ticket_tool

### Explanation

MCP Inspector helped verify that every tool worked correctly before deployment.

---

# Technologies Used

- Python
- Anthropic Claude API
- MCP (Model Context Protocol)
- FastMCP
- MCP Inspector
- python-dotenv
- JSON

---

# Run The Agent

```bash
python agent.py
```

---

# Run MCP Server

```bash
python mcp_server.py
```

---

# Author

**Deepak Kumar**

- Blockchain & Web3 Developer
- Smart Contract Engineer
- AI Agent Builder