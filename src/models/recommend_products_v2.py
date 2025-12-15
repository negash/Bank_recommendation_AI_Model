# Recommendation Engine
class Customer:
    """
    Docstring for Customer class representing a banking customer.
    """

    def __init__(self, name, age, address, occupation, balance, account_type):
        self.name = name
        self.age = age
        self.address = address
        self.occupation = occupation.lower().strip() if occupation else ""
        self.balance = balance
        self.account_type = account_type.lower().strip() if account_type else ""


class ProductRecommender:
    """
    Docstring for ProductRecommender
    """
    OCCUPATION_MAP = {
        "techer": "teacher",
        "samll buisness": "small business",
        "buisness": "business",
        "cheking": "checking",
        "saving": "saving",
    }

    def __init__(self):
        pass

    def recommend(self, customer: Customer) -> str:
        """Generate product recommendations based on customer profile."""

        occupation = self.normalize_occupation(customer.occupation)
        balance = customer.balance
        age = customer.age
        account_type = customer.account_type

        recommendations = []

        # Apply rule groups
        recommendations.extend(self.balance_based_rules(balance))
        recommendations.extend(self.occupation_based_rules(occupation))
        recommendations.extend(self.age_based_rules(age))
        recommendations.extend(self.account_type_rules(account_type))

        # If nothing recommended
        if not recommendations:
            recommendations.append("Standard Banking Products")

        # Remove duplicates while keeping order
        recommendations = list(dict.fromkeys(recommendations))

        return "; ".join(recommendations)

    def normalize_occupation(self, occ: str) -> str:
        """Normalize occupation using predefined mapping."""
        return self.OCCUPATION_MAP.get(occ, occ)

    def balance_based_rules(self, balance: float):
        """Recommendation rules based on balance tiers."""
        r = []
        if balance > 1_000_000:
            r += [
                "Elite Priority Banking",
                "Ultra High-Yield Certificate of Deposit (UHCD)",
                "Private Wealth Advisory Services",
            ]
        elif balance > 500_000:
            r += [
                "Diamond Wealth Member",
                "High-Yield Certificate of Deposit (HCD)",
                "Wealth Management Portfolio",
            ]
        elif balance > 250_000:
            r += [
                "Platinum Saving Member",
                "Certificate of Deposit (VIP CD)",
            ]
        elif balance > 150_000:
            r += [
                "VIP Member",
                "Certificate of Deposit (Silver CD)",
            ]
        elif balance > 100_000:
            r += ["Premium Certificate of Deposit (PCD)"]

        return r

    def occupation_based_rules(self, occupation: str):
        """Recommendations based on specific job categories."""
        r = []

        if occupation == "student":
            r += ["Student Savings Account", "Zero-Fee Debit Card"]

        if occupation == "teacher":
            r += ["Teacher Special Mortgage Savings Account",
                  "Education Grant-Linked Savings Plan"]

        if occupation == "engineer":
            r += ["Tech Professional Investment Plan"]

        if occupation in ["doctor", "nurse"]:
            r += ["Medical Professionals Retirement Advantage Plan"]

        if occupation in ["small business", "entrepreneur"]:
            r += ["Business Growth Checking Account",
                  "Small Business Credit Line"]

        return r

    def age_based_rules(self, age: int):
        """Recommends age-targeted financial products."""
        r = []

        if age is None:
            return r

        if age < 18:
            r += ["Youth Savings Account", "Financial Literacy Program"]
        elif 18 <= age <= 25:
            r += ["Starter Investment Portfolio"]
        elif 26 <= age <= 45:
            r += ["Retirement Growth Plan (RGP)"]
        elif age > 45:
            r += ["Retirement Stability Bonds"]

        return r

    def account_type_rules(self, account_type: str):
        """Add-ons based on the account type a customer already has."""
        r = []

        if account_type == "checking":
            r += ["Overdraft Protection Plan", "Cash-Back Debit Rewards"]

        if account_type == "saving":
            r += ["Automatic Monthly Savings Booster"]

        return r


# Test, this part would be in a separate test file normally
# Create a customer object
cust = Customer(
    name="Alice Brown",
    age=45,
    address="1200 Lake View Rd, Seattle, WA",
    occupation="Engineer",
    balance=180000,
    account_type="checking"
)

# Run recommendations
recommender = ProductRecommender()
print(recommender.recommend(cust))
