**Bank Recommendation AI Model**

An AI-powered banking product recommendation engine that combines Python, a rule-based recommender, and OpenAI’s function-calling capabilities to deliver personalized financial product suggestions based on customer profiles.

**Project Overview**

This repository demonstrates a complete end-to-end recommendation system where a Large Language Model (LLM) intelligently interacts with backend logic to recommend appropriate bank products tailored to individual customer attributes such as age, balance, occupation, and account type.

The system leverages:

- Python for business logic and tool implementation
- OpenAI function calling to integrate LLM reasoning with structured backend functions
- A rule-based recommendation model representing real-world product eligibility

**Key Features**

- **✔** **Customer model** with normalization and structured attributes
- **✔** **Rule-based Product Recommender** (age, balance, occupation, account type)
- **✔** **Function-calling tool (banker_recommendation_tool)** exposed to the LLM
- **✔** **Automatic model → tool → model response pipeline**
- **✔** **Customer dataset in JSON** (get_customers())
- **✔** Export Customer Recommendation to CSV (Bonous Feature) \*\*to generates customer_recommendations.csv
- **✔** Fully compatible with gpt-5.1 tool invocation format

![alt text](Project_Architecture.png)


**Project Architecture**

**1. Customer Model**

A Customer class that encapsulates core personal and financial information such as:

- Name
- Age
- Address
- Occupation
- Balance
- Account type

This standardized model enables consistent input handling and recommendation logic execution.

**2. Product Recommendation Logic**
The Product Recommender uses a set of hierarchical rules to match customers with the right financial products
Logic is based on:

1. Balance Tiers — Groups customers by account balance.
2. Occupation Overrides — Occupation-specific rules that adjust product eligibility.
3.Age Categories — Life-stage based product targeting.

Example output might include recommendations like:

Example output:
VIP Member; Silver CD; Investment Plan; Retirement Growth Plan; Overdraft Protection

**Function:** banker_recommendation_tool

def banker_recommendation_tool(name: str):
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

This tool accepts a customer name, retrieves the corresponding record, runs the recommendation logic, and returns a structured recommendation response.

**LLM Interaction Pipeline**

The system follows a **Model → Tool → Model** workflow:

1. User issues a natural language request to generate a recommendation.

2. The LLM identifies when a function call is needed and calls banker_recommendation_tool.

3. The backend executes the function and returns results.

4. The LLM produces the final formatted recommendation.

**CSV Export Feature (Bonus)**

The repository also includes a utility that exports the customer recommendations into a CSV file, useful for reporting, auditing, and downstream analysis.

**Example Usage**
Example invocation:

# User request:
"Generate a banking recommendation for Maria Lopez"

# LLM triggers:
banker_recommendation_tool(name="Maria Lopez")

# Sample response:

{
  "name": "Maria Lopez",
  "occupation": "engineer",
  "balance": 185000,
  "recommendation": "VIP Member; Silver CD; Tech Professional Investment Plan; Retirement Growth Plan (RGP); Overdraft Protection Plan"
}

**Technologies Used**

- Python

- OpenAI function calling API (GPT-5.1 compatible)

- JSON data structures

- Rule-based logic engine

**Closing Notes**

This project serves as a practical example of how to combine rule-based systems with LLM capabilities for real-world decision support systems in the banking domain. It highlights how structured backend tools can be integrated into an LLM-driven workflow for reliable, explainable outputs.
