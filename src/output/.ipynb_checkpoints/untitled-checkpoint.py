import csv
from src.models.recommend_products_v2 import Customer, ProductRecommender
from src.data.Customers_data import get_customers

output_file = "customer_recommendations.csv"

customers = get_customers()
recommender = ProductRecommender()

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow([
        "Name", "Age", "Address", "Occupation",
        "Balance", "Account Type", "Recommendations"
    ])

    # Write each customer
    for c in customers:
        cust_obj = Customer(
            name=c["name"],
            age=c["age"],
            address=c["address"],
            occupation=c["occupation"],
            balance=c["balance"],
            account_type=c["account_type"]
        )

        recs = recommender.recommend(cust_obj)

        writer.writerow([
            cust_obj.name,
            cust_obj.age,
            cust_obj.address,
            cust_obj.occupation,
            cust_obj.balance,
            cust_obj.account_type,
            recs
        ])

print(f"CSV file '{output_file}' created successfully!")

