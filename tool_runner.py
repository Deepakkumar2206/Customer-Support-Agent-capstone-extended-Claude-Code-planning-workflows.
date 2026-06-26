import json

from mock_data import CUSTOMERS, ORDERS

# Simple Audit Log
audit_log = []


def get_customer(query: str, session_state: dict) -> str:

    query = query.strip().lower()

    for customer in CUSTOMERS.values():

        if (
            query == customer["customer_id"].lower()
            or query == customer["email"].lower()
            or query == customer["name"].lower()
        ):

            session_state["verified_customer_id"] = (
                customer["customer_id"]
            )

            session_state["verified_customer_name"] = (
                customer["name"]
            )

            return json.dumps(
                {
                    "customer_id": customer["customer_id"],
                    "name": customer["name"],
                    "email": customer["email"],
                    "account_status": customer["account_status"],
                }
            )

    return json.dumps(
        {
            "error": {
                "type": "validation",
                "retryable": False,
                "message": "Customer not found."
            }
        }
    )


def lookup_order(order_id: str, session_state: dict) -> str:

    order_id = order_id.strip().upper()

    if order_id in ORDERS:
        return json.dumps(ORDERS[order_id])

    return json.dumps(
        {
            "error": {
                "type": "validation",
                "retryable": False,
                "message": "Order not found."
            }
        }
    )


def process_refund(
    customer_id: str,
    order_id: str,
    amount: float,
    session_state: dict
) -> str:

    # Gate Check 1
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

    # Gate Check 2
    if customer_id != session_state["verified_customer_id"]:

        return json.dumps(
            {
                "error": {
                    "type": "permission",
                    "retryable": False,
                    "message":
                    "Customer ID mismatch."
                }
            }
        )

    # Gate Check 3
    if order_id not in ORDERS:

        return json.dumps(
            {
                "error": {
                    "type": "validation",
                    "retryable": False,
                    "message":
                    "Order not found."
                }
            }
        )

    order = ORDERS[order_id]

    # Gate Check 4
    if order["customer_id"] != session_state["verified_customer_id"]:

        return json.dumps(
            {
                "error": {
                    "type": "permission",
                    "retryable": False,
                    "message":
                    "Order does not belong to verified customer."
                }
            }
        )

    # Business Rule
    if order["status"] != "delivered":

        return json.dumps(
            {
                "error": {
                    "type": "business_rule",
                    "retryable": False,
                    "message":
                    "Refunds can only be processed for delivered orders."
                }
            }
        )

    # Human Escalation
    if amount > 500:

        audit_log.append(
            {
                "action": "refund_escalated",
                "customer_id": customer_id,
                "order_id": order_id,
                "amount": amount
            }
        )

        return json.dumps(
            {
                "escalation": True,
                "message":
                "Refund exceeds approval threshold and requires human review."
            }
        )

    # Audit Log
    audit_log.append(
        {
            "action": "refund_processed",
            "customer_id": customer_id,
            "order_id": order_id,
            "amount": amount
        }
    )

    return json.dumps(
        {
            "success": True,
            "refund_id":
            "REF-" + order_id.split("-")[1],

            "customer_id":
            customer_id,

            "order_id":
            order_id,

            "amount":
            amount,

            "status":
            "initiated",

            "message":
            f"Refund of ${amount:.2f} has been initiated."
        }
    )
def create_support_ticket(
    customer_id: str,
    issue: str,
    session_state: dict
) -> str:

    import json

    ticket_id = f"TICKET-{len(issue) + 1000}"

    return json.dumps(
        {
            "success": True,
            "ticket_id": ticket_id,
            "customer_id": customer_id,
            "issue": issue,
            "status": "open",
            "priority": "high"
        }
    )

def run_tool(
    tool_name: str,
    tool_input: dict,
    session_state: dict
) -> str:

    if tool_name == "get_customer":

        return get_customer(
            tool_input["query"],
            session_state
        )

    elif tool_name == "lookup_order":

        return lookup_order(
            tool_input["order_id"],
            session_state
        )

    elif tool_name == "process_refund":

        return process_refund(
            tool_input["customer_id"],
            tool_input["order_id"],
            tool_input["amount"],
            session_state
        )
    
    elif tool_name == "create_support_ticket":

        return create_support_ticket(
            tool_input["customer_id"],
            tool_input["issue"],
            session_state
        )

    return json.dumps(
        {
            "error": {
                "type": "system",
                "retryable": False,
                "message":
                f"Unknown tool: {tool_name}"
            }
        }
    )