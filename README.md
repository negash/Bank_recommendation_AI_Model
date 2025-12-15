**Bank Recommendation AI Model**

An AI-powered banking product recommendation engine that combines Python, a rule-based recommender, and OpenAI’s function-calling capabilities to deliver personalized financial product suggestions based on customer profiles.

**Project Overview**

This repository demonstrates a complete end-to-end recommendation system where a Large Language Model (LLM) intelligently interacts with backend logic to recommend appropriate bank products tailored to individual customer attributes such as age, balance, occupation, and account type.

The system leverages:

- Python for business logic and tool implementation
- OpenAI function calling to integrate LLM reasoning with structured backend functions
- A rule-based recommendation model representing real-world product eligibility

**Installation**

To install all required dependencies for this project, run the following command:

pip install -r requirements.txt

**Optional :**

Create and activate a virtual environment to isolate project dependencies:

**Create a virtual environment**

python -m venv .venv

**Activate the virtual environment**

source .venv/bin/activate

**Key Features**

- **✔** **Customer model** with normalization and structured attributes
- **✔** **Rule-based Product Recommender** (age, balance, occupation, account type)
- **✔** **Function-calling tool (banker_recommendation_tool)** exposed to the LLM
- **✔** **Automatic model → tool → model response pipeline**
- **✔** **Customer dataset in JSON** (get_customers())
- **✔** Export Customer Recommendation to CSV (Bonous Feature) \*\*to generates customer_recommendations.csv
- **✔** Fully compatible with gpt-5.1 tool invocation format

**Project Architecture**
![alt text](assets/Project_Architecture.png)

**1. Customer Model**

A Customer class that encapsulates core personal and financial information such as:

- Name
- Age
- Address
- Occupation
- Balance
- Account type

This standardized model enables consistent input handling and recommendation logic execution.

**2. Product Recommendation Logic** The Product Recommender uses a set of hierarchical rules to match customers with the right financial products Logic is based on:

**1. Balance Tiers** — Groups customers by account balance.

**2. Occupation Overrides** — Occupation-specific rules that adjust product eligibility.

**3. Age Categories** — Life-stage based product targeting.

**4. Account Type** — Existing account influences upgrade or complementary product offers.

Example output might include recommendations like:

VIP Member; Silver CD; Investment Plan; Retirement Growth Plan; Overdraft Protection

**Function:** banker_recommendation_tool

A Python function exposed to the LLM via OpenAI’s function calling interface:

def banker_recommendation_tool(name: str):

```
customers = get_customers()
recommender = ProductRecommender()

for c in customers:
    if c["name"].lower() == name.lower():
        customer_obj = Customer(
            name=c["name"],
            age=c.get("age"),
            address=c.get("address"),
            occupation=c.get("occupation"),
            balance=c.get("balance"),
            account_type=c.get("account_type")
        )
        return {
            "name": c["name"],
            "occupation": c["occupation"],
            "balance": c["balance"],
            "recommendation": recommender.recommend(customer_obj)
        }
return {"error": f"No customer found with name {name}"}
```

This tool accepts a customer name, retrieves the corresponding record, runs the recommendation logic, and returns a structured recommendation response.

**LLM Interaction Pipeline**

The system follows a **_Model → Tool → Model_** workflow:

1. User issues a natural language request to generate a recommendation.
2. The LLM identifies when a function call is needed and calls banker_recommendation_tool.
3. The backend executes the function and returns results.
4. The LLM produces the final formatted recommendation.

**Example Usage**

**User request:** "Generate a banking recommendation for Maria Lopez"

**LLM triggers:** banker_recommendation_tool(name="Maria Lopez")

messages = [

{

```
 "role": "user",

 "content": "Generate a banking recommendation for Maria Lopez."
```

} ]

response = client.chat.completions.create(

model="openai:gpt-5.1",

messages=messages,

tools=TOOLS )

msg = response.choices[0].message

**Execute the tool if needed to validate**

if msg.tool_calls:

```
tool_call = msg.tool_calls[0]

args = json.loads(tool_call.function.arguments)

tool_response = banker_recommendation_tool(\*\*args)

print("TOOL RESPONSE:", tool_response)
```

**Response: { "name": "Maria Lopez", "occupation": "engineer", "balance": 185000, "recommendation": "VIP Member; Silver CD; Tech Professional Investment Plan; Retirement Growth Plan (RGP); Overdraft Protection Plan" }**

**7. Export Customer Recommendation to CSV (Bonous Feature)**

This document describes the bonus functionality for exporting customer product recommendations to a CSV file. The** \*\***Export to CSV\*\* feature provides a mechanism to generate a comprehensive spreadsheet containing customer details and their corresponding product recommendations. This is useful for auditing, analysis, or sharing the recommendations outside of the application.

[![alt text](https://github.com/negash/Bank_recommendation_AI_Model/raw/main/assets/customer_recommend_csv.png)](https://github.com/negash/Bank_recommendation_AI_Model/blob/main/assets/customer_recommend_csv.png)

**Technologies Used**

- Python
- OpenAI function calling API (GPT-5.1 compatible)
- JSON data structures
- Rule-based logic engine

**Closing Notes**

This project serves as a practical example of how to combine rule-based systems with LLM capabilities for real-world decision support systems in the banking domain. It highlights how structured backend tools can be integrated into an LLM-driven workflow for reliable, explainable outputs.
