CUSTOMERS = {
    "CUST-4492": {
        "customer_id": "CUST-4492",
        "name": "Sarah Chen",
        "email": "sarah.chen@email.com",
        "account_status": "active",
        "orders": ["ORD-8821"]
    },

    "CUST-2201": {
        "customer_id": "CUST-2201",
        "name": "James Okafor",
        "email": "james.okafor@email.com",
        "account_status": "active",
        "orders": ["ORD-1001"]
    },

    "CUST-9901": {
        "customer_id": "CUST-9901",
        "name": "Deepak Kumar",
        "email": "deepak@email.com",
        "account_status": "premium",
        "orders": ["ORD-5001"]
    }
}

ORDERS = {
    "ORD-8821": {
        "order_id": "ORD-8821",
        "customer_id": "CUST-4492",
        "status": "processing",
        "days_since_order": 6,
        "amount": 150,
        "notes": "Warehouse inventory hold."
    },

    "ORD-1001": {
        "order_id": "ORD-1001",
        "customer_id": "CUST-2201",
        "status": "shipped",
        "days_since_order": 3,
        "amount": 650,
        "notes": "In transit."
    },

    "ORD-5001": {
        "order_id": "ORD-5001",
        "customer_id": "CUST-9901",
        "status": "delivered",
        "days_since_order": 12,
        "amount": 299,
        "notes": "Delivered successfully."
    }
}
SUPPORT_TICKETS = {}