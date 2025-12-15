
# -----------------------------
# The LLM uses this schema to call the tool
# -----------------------------
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "banker_recommendation_tool",
            "description": "Return the banking recommendation for a given customer name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        }
    }
]
