""" """
from collections import Counter
import matplotlib.pyplot as plt
from src.models.recommend_products_v2 import Customer, ProductRecommender
from src.data.Customers_data import get_customers


def run_visual_analytics():
    """Generates and saves a consolidated 3-in-1 analytics dashboard."""
    # Load and process data
    raw_data = get_customers()
    recommender = ProductRecommender()
    customers = [
        Customer(c["name"], c["age"], c["address"],
                 c["occupation"], c["balance"], c["account_type"])
        for c in raw_data
    ]

    # Occupation data
    occ_counts = Counter(recommender.normalize_occupation(
        c.occupation).capitalize() for c in customers)

    # Recommendation data
    all_recs = []
    for c in customers:
        rec_string = recommender.recommend(c)
        all_recs.extend([r.strip() for r in rec_string.split(";")])
    rec_counts = Counter(all_recs).most_common(8)  # Top 8 for better spacing
    products, counts = zip(*rec_counts)

    # Demographic data
    ages = [c.age for c in customers]
    balances = [c.balance for c in customers]

    # create a figure and a set of subplots
    # constrained_layout to prevent labels from overlapping
    fig = plt.figure(figsize=(15, 12), constrained_layout=True)
    spec = fig.add_gridspec(2, 2)  # 2 rows, 2 columns

    # --- Top : Occupation Distribution (Pie) ---
    ax1 = fig.add_subplot(spec[0, 0])
    ax1.pie(occ_counts.values(), labels=occ_counts.keys(),
            autopct='%1.1f%%', startangle=140)
    ax1.set_title('Customer Segmentation (Occupation)')

    # --- Top right: Balance vs Age (Scatter) ---
    ax2 = fig.add_subplot(spec[0, 1])
    ax2.scatter(ages, balances, color='forestgreen', alpha=0.6)
    ax2.set_xlabel('Age')
    ax2.set_ylabel('Balance ($)')
    ax2.set_title('Financial Trend: Balance vs. Age')
    ax2.grid(True, linestyle='--', alpha=0.5)

    # --- Bottom: Product Recommendations (Bar) ---
    ax3 = fig.add_subplot(spec[1, :])  # Use ':' to span all columns
    ax3.barh(products, counts, color='skyblue')
    ax3.set_xlabel('Number of Recommendations')
    ax3.set_title('Top Product Recommendations')
    ax3.invert_yaxis()

    # Save the single output file
    output_name = 'customer_analytics_dashboard.png'
    plt.savefig(output_name, dpi=300)  # Save with high resolution
    plt.close()

    print(f"Success! Dashboard generated: {output_name}")


if __name__ == "__main__":
    run_visual_analytics()
