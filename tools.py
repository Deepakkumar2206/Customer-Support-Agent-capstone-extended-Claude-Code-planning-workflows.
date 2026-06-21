tools = [
    {
        "name": "get_customer",

        "description": (
            "Look up customer information using customer ID, "
            "email address or full name. "
            "Returns account details and order IDs."
        ),

        "input_schema": {
            "type": "object",

            "properties": {
                "query": {
                    "type": "string",
                    "description": (
                        "Customer ID, email address or full name."
                    )
                }
            },

            "required": ["query"]
        }
    },

    {
        "name": "lookup_order",

        "description": (
            "Look up order information using an order ID."
        ),

        "input_schema": {
            "type": "object",

            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Order ID like ORD-8821"
                }
            },

            "required": ["order_id"]
        }
    },

    {
        "name": "process_refund",

        "description": (
            "Process a refund for a verified customer. "
            "Requires customer_id, order_id and amount."
        ),

        "input_schema": {
            "type": "object",

            "properties": {

                "customer_id": {
                    "type": "string"
                },

                "order_id": {
                    "type": "string"
                },

                "amount": {
                    "type": "number"
                }
            },

            "required": [
                "customer_id",
                "order_id",
                "amount"
            ]
        }
    },
    
    {
        "name": "create_support_ticket",

        "description": (
            "Create a support ticket for unresolved issues."
       ),

       "input_schema": {
            "type": "object",

            "properties": {

                "customer_id": {
                    "type": "string"
                },

                "issue": {
                    "type": "string"
                }
           },

            "required": [
                "customer_id",
                "issue"
            ]
        }
    }
]
