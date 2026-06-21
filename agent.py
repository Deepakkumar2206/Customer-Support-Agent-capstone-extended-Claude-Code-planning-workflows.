from anthropic import Anthropic
from dotenv import load_dotenv

from tool_runner import run_tool
from tools import tools

load_dotenv()

client = Anthropic()

SYSTEM_PROMPT = """
You are a professional customer support agent.

Rules:

1. Verify customer identity before discussing account details.
2. Use get_customer to find customer records.
3. Use lookup_order for order information.
4. Use process_refund for refund requests.
5. Explain tool errors politely.
6. Never invent customer or order data.
7. If an issue cannot be resolved, create a support ticket.
"""

# Persistent conversation memory
conversation_history = []

# Persistent session state
session_state = {
    "verified_customer_id": None,
    "verified_customer_name": None
}


def run_agent(user_message: str) -> str:

    conversation_history.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    while True:

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=conversation_history
        )

        conversation_history.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )

        if response.stop_reason == "end_turn":

            final_text = ""

            for block in response.content:

                if hasattr(block, "text"):
                    final_text += block.text

            return final_text

        if response.stop_reason == "tool_use":

            tool_results = []

            for block in response.content:

                if block.type == "tool_use":

                    result = run_tool(
                        block.name,
                        block.input,
                        session_state
                    )

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result
                        }
                    )

            conversation_history.append(
                {
                    "role": "user",
                    "content": tool_results
                }
            )


if __name__ == "__main__":

    print("Customer Support Agent - Production Capstone")
    print("Type 'quit' to exit")

    while True:

        user_input = input("\nCustomer: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit", "q"]:
            break

        response = run_agent(user_input)

        print("\nAgent:", response)