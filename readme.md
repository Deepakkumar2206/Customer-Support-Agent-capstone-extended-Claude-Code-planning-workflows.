# Claude Customer Support Production Capstone

A production-style AI customer support agent built using the Anthropic Claude API and MCP (Model Context Protocol).

This project evolved from a basic customer lookup application into a production-oriented support system featuring customer verification, refund processing, support ticket management, structured error handling, session management, and MCP tool integration. It also demonstrates AI-assisted development using Claude Code workflows.

---

# Features

* Customer lookup using ID, email, or name
* Order lookup
* Refund processing
* Customer verification before sensitive operations
* Support ticket creation
* Session-based customer verification
* Structured JSON error responses
* MCP Server integration
* MCP Inspector testing
* AI-assisted development with Claude Code

---

# Claude Code Tasks Completed

During the project, Claude Code was used to complete real-world engineering tasks by selecting the appropriate built-in tools (Read, Grep, Edit, Bash).

### Task 1 — Restrict Customer Data Exposure

Updated the `get_customer` tool to return only:

* customer_id
* name
* email
* account_status

instead of exposing the complete customer record.

**Result**

Improved customer privacy while preserving existing application functionality.

---

### Task 2 — Add Global Exception Handling

Implemented a catch-all exception handler in the main agent loop.

Features added:

* Structured error responses
* Exception logging
* Graceful failure handling
* Improved production reliability

---

# Project Structure

```text
claude-customer-support-production-capstone/
│
├── agent.py
├── tool_runner.py
├── tools.py
├── mock_data.py
├── mcp_server.py
├── mcp.json
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── screenshots/
    ├── 01_Task_Prompt.png
    ├── 02_Code_Search_Grep.png
    ├── 03_Proposed_Code_Change.png
    ├── 04_Edit_Approval.png
    ├── 05_Code_Modification.png
    ├── 06_Implementation_Progress.png
    └── 07_Task_Completed.png
```

---

# Key Improvements Made

## 1. Customer Verification

Before processing refunds, customers must first verify their identity.

```python
if not session_state.get("verified_customer_id"):
    return json.dumps({
        "error": {
            "type": "permission",
            "retryable": False,
            "message": "Customer must be verified before refund."
        }
    })
```

This prevents unauthorized refund requests.

---

## 2. Session State Management

```python
session_state = {
    "verified_customer_id": None,
    "verified_customer_name": None
}
```

The agent remembers the verified customer throughout the conversation.

---

## 3. Refund Processing Tool

```python
{
    "name": "process_refund",
    "description": "Process a refund for a verified customer."
}
```

Allows refunds only after successful verification.

---

## 4. Support Ticket Creation

```python
{
    "name": "create_support_ticket",
    "description": "Create a support ticket for unresolved issues."
}
```

Automatically creates tickets for unresolved customer problems.

---

## 5. Ticket Generation

```python
ticket_id = f"TICKET-{random.randint(1000,9999)}"
```

Each ticket receives a unique identifier.

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

Returns standardized JSON error responses instead of generic failures.

---

## 7. MCP Tool Registration

```python
@mcp.tool()
def get_customer_tool(query: str):
    return get_customer(query, session_state)
```

Exposes Python functions as MCP tools.

---

## 8. MCP Server

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("support-agent-tools")
```

Creates the MCP server that exposes the available tools.

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

Defines how the MCP server is launched.

---

## 10. MCP Inspector Testing

Validated every tool using MCP Inspector.

Tested tools:

* get_customer_tool
* lookup_order_tool
* process_refund_tool
* create_support_ticket_tool

---

# Claude Code Workflow

This project demonstrates practical use of Claude Code for AI-assisted software development.

* Used **Grep** to locate the target function.
* Used **Read** to understand the implementation.
* Used **Edit** to apply precise code modifications.
* Approved code changes before execution.
* Verified implementation after completion.

---

# Technologies Used

* Python
* Anthropic Claude API
* MCP (Model Context Protocol)
* FastMCP
* MCP Inspector
* Claude Code
* python-dotenv
* JSON

---

# Run the Agent

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

* Blockchain & Web3 Developer
* Smart Contract Engineer
* AI Agent Builder
