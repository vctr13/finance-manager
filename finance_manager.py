from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import json


@dataclass(frozen=True)
class Category:
    id: int
    name: str

@dataclass
class Transaction:
    amount: Decimal
    category: Category
    item: str
    created_at: datetime = field(default_factory= lambda: datetime.now(timezone.utc))

class FinanceManager:

    def __init__(self, file_name: str):
        self.transactions: list[Transaction] = []
        self.file_name = file_name

    def add_transaction(self, amount: Decimal, category: Category, item: str) -> Transaction | None:
        try:
            transaction = Transaction(amount, category, item)
            self.transactions.append(transaction)
            return transaction
        except InvalidOperation:
            print("Invalid amount. Transaction not added.")
            return None

    def save_json(self) -> bool:
        try:
            with open(self.file_name, "w", encoding="utf-8") as file:
                converted_transactions = [
                    {
                        "amount": str(t.amount),
                        "category_id": t.category.id,
                        "category_name": t.category.name,
                        "item": t.item,
                        "created_at": t.created_at.isoformat()
                    } for t in self.transactions
                ]
                json.dump(converted_transactions, file, indent=4)
                return True
        except TypeError as e:
            print(f"Error saving to JSON: {e}")
            return False

    def load_json(self) -> bool:
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                loaded_date = json.load(file)
                self.transactions = [
                    Transaction(
                        amount = Decimal(t["amount"]),
                        category= Category(t["category_id"], t["category_name"]),
                        item = t["item"],
                        created_at = datetime.fromisoformat(t["created_at"])
                    ) for t in loaded_date
                ]
                return True
        except FileNotFoundError:
            print("File not found")
            return False

    def report(self) -> dict[str, list[Decimal]]:
        transactions_by_cat = defaultdict(list)
        for trans in self.transactions:
            transactions_by_cat[trans.category.name].append(trans.amount)
        for cat in transactions_by_cat:
            print(f"Category: {cat} - sum: {sum(transactions_by_cat[cat])}")
        return transactions_by_cat



cat_food = Category(id=1, name="Food")
cat_transport = Category(id=2, name="Transport")

fm = FinanceManager("finance.json")
fm.add_transaction(Decimal("1500.00"),  cat_food, "Apples")
fm.add_transaction(Decimal("500.00"),  cat_transport, "Bus")
fm.add_transaction(Decimal("2500.00"),  cat_food, "Steak")
fm.add_transaction(Decimal("500.00"),  cat_transport, "Train")
fm.add_transaction(Decimal("1500.00"),  cat_transport, "Train")

print(fm.transactions)
fm.save_json()

fm.transactions = []
print("Clear transactions:")
print(fm.transactions)
fm.load_json()
print("Loaded json:")
print(fm.transactions)
print("Report by category:")
report = fm.report()
print(report)
