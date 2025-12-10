from models.recommend_products_v2 import Customer, ProductRecommender


def test_customer_normalization():
    # occupation and account_type should be lowercased and stripped
    c = Customer(name="Bob", age=30, address="",
                 occupation="  Engineer  ", balance=0, account_type=" CHECKING ")
    assert c.occupation == "engineer"
    assert c.account_type == "checking"


def test_recommend_for_typical_customer():
    # Based on the rules in recommend_products_v2, this customer should get
    # balance-based, occupation-based, age-based and account-type recommendations
    cust = Customer(
        name="Alice Brown",
        age=45,
        address="1200 Lake View Rd, Seattle, WA",
        occupation="Engineer",
        balance=180000,
        account_type="checking",
    )

    recommender = ProductRecommender()
    result = recommender.recommend(cust)

    expected_items = [
        "VIP Member",
        "Certificate of Deposit (Silver CD)",
        "Tech Professional Investment Plan",
        "Retirement Growth Plan (RGP)",
        "Overdraft Protection Plan",
        "Cash-Back Debit Rewards",
    ]

    for item in expected_items:
        assert item in result

    # Check order (first two from balance rules)
    assert result.startswith("VIP Member; Certificate of Deposit (Silver CD)")


def test_occupation_normalization_map():
    # A misspelled occupation 'techer' should map to 'teacher' and yield teacher offers
    cust = Customer(name="David", age=35, address="",
                    occupation="techer", balance=4500, account_type="")
    recommender = ProductRecommender()
    res = recommender.recommend(cust)
    assert "Teacher Special Mortgage Savings Account" in res
    assert "Education Grant-Linked Savings Plan" in res


def test_default_when_no_rules_apply():
    # If no rules match, default recommendation should be returned
    cust = Customer(name="Empty", age=None, address="",
                    occupation="", balance=0, account_type="")
    recommender = ProductRecommender()
    assert recommender.recommend(cust) == "Standard Banking Products"

# Run the tests with: pytest tests/test_recommend_products_v2.py
