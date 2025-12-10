from ..models.recommend_products_v2 import Customer, ProductRecommender
from ..data.Customers_data import get_customers


def banker_recommendation_tool(name: str):
    # -----------------------------
    # FETCH CUSTOMERS AND INITIALIZE RECOMMENDER
    # -----------------------------

    customers = get_customers()
    recommender = ProductRecommender()

    for c in customers:
        if c["name"].lower() == name.lower():

            # Convert dict into Customer object
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
                # recommend_products(c)
                "recommendation": recommender.recommend(customer_obj)
            }
    return {"error": f"No customer found with name {name}"}
