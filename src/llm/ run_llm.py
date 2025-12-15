import os
import json
from openai import OpenAI

from llm.defin_tools import TOOLS
from tools.banker_recommendation_tool import banker_recommendation_tool

# Ensure your OpenAI API key is set in the environment variables, or replace with your key directly.
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI

messages = [
    {
        "role": "user",
        "content": "Generate a banking recommendation for Maria Lopez."  # John Smith
    }
]

response = client.chat.completions.create(
    model="openai:gpt-5.1",
    messages=messages,
    tools=TOOLS
)

msg = response.choices[0].message
print("MODEL MESSAGE:", msg)

if msg.tool_calls:
    tool_call = msg.tool_calls[0]
    args = json.loads(tool_call.function.arguments)

    tool_response = banker_recommendation_tool(**args)
    print("TOOL RESPONSE:", tool_response)


# TOOL RESPONSE: {'name': 'Maria Lopez', 'occupation': 'Doctor', 'balance': 850000, 'recommendation': 'Diamond Wealth Member; High-Yield Certificate of Deposit (HCD); Wealth Management Portfolio; Medical Professionals Retirement Advantage Plan; Retirement Growth Plan (RGP); Overdraft Protection Plan; Cash-Back Debit Rewards'}
# TOOL RESPONSE: {'name': 'John Smith', 'occupation': 'Engineer', 'balance': 1200000, 'recommendation': 'Elite Priority Banking; Ultra High-Yield Certificate of Deposit (UHCD); Private Wealth Advisory Services; Tech Professional Investment Plan; Retirement Growth Plan (RGP); Overdraft Protection Plan; Cash-Back Debit Rewards'}
