import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

FILE_PATH = Path("_finance_transactions.json")
# FILE_NAME = "_finance_transactions.json"

BUDGET_LIMIT = {
    "Groceries" : 5_000,
    "Utilities" : 4_000,
    "Dining Out" : 3_000
}
VALID_CATEGORIES = set(BUDGET_LIMIT)

def load_transactions():
    if FILE_PATH.exists():
        try:
            return json.loads(FILE_PATH.read_text())
        except json.JSONDecodeError:
            return []
    return []

def save_transactions(_transactions):
    FILE_PATH.write_text(json.dumps(_transactions, indent=4))

"""
def load_transactions():
    try:
        with open(FILE_NAME, 'r') as _file:
            #either of therm will work
            _transactions = json.loads(_file.read())
            _transactions = json.load(_file)
        return _transactions
    except Exception as err:
        print(f"Error : {err}")
        return []

def save_transactions(_transactions):
    try:
        with open(FILE_NAME, 'w') as _file:
            json.dump(_transactions, _file, indent=4)
            # _file.write(json.dumps(_transactions, indent=4))
    except Exception as err:
        print(f"Error : {err}")
"""

def add_transaction(_amount, _category, _transaction_type):
    #load existing transactions
    _transactions = load_transactions()
    validate_category(_category)
    _transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": _amount,
        "category": _category,
        "type": _transaction_type
    }
    #add new transaction to existing transactions
    _transactions.append(_transaction)
    save_transactions(_transactions)

def summary_report():
    _transactions = load_transactions()
    _summary_report = {
        "Income" : 0,
        "Expense" : 0,
        #set value of key that do not exist as 0
        "Categories" : defaultdict(int)
    }
    for _tran in _transactions:
        _transaction_type = _tran["type"]
        _transaction_category = _tran["category"]
        _transaction_amount = _tran["amount"]

        _summary_report[_transaction_type] += _transaction_amount
        if _transaction_type=="Expense":
            #below line set value of the key that do not exist as zero without "defaultdict" we do it like this
            # _summary_report["Categories"][_transaction_category] = _summary_report["Categories"].get(_transaction_category, 0) + _transaction_amount
            _summary_report["Categories"][_transaction_category] +=  _transaction_amount
    
    print(f"Income : {_summary_report['Income']}")
    print(f"Expense : {_summary_report['Expense']}")
    for _cate_key, _cate_val in _summary_report["Categories"].items():
        print(f"{_cate_key} : {_cate_val}")

def filter_expense_by_category(_category):
    _transactions = load_transactions()
    _total_category_amount = sum(
        _tran["amount"] 
        for _tran in _transactions 
        if (_tran["type"]=="Expense" and _tran["category"]==_category)
        )
    print(f"{_category} : {_total_category_amount} ")

def check_budget(_category, _amount):
    _transactions = load_transactions()
    _total_category_expense = sum(
        _tran["amount"]
        for _tran in _transactions
        if (_tran["category"]==_category and _tran["type"]=="Expense")
    )
    if _total_category_expense+_amount > BUDGET_LIMIT[_category]:
        print(f"Limit Exceeded : {_category} : {_total_category_expense}")
    else:
        print(f"Within Limit : {_category} : {_total_category_expense}")

def validate_category(_category):
    if _category in VALID_CATEGORIES:
        print(f"Valid : {_category}")
    else:
        print(f"Invalid : {_category}")

validate_category("Groceries")
validate_category("Utilities")
validate_category("Dining In")
validate_category("Entertainment")

check_budget("Groceries", 1_000)
check_budget("Utilities", 1_000)
check_budget("Dining Out", 3_000)

_add_transaction_data = [
    (50_000, "Salary", "Income"),
    (2_000, "Groceries", "Expense"),
    (1_000, "Groceries", "Expense"),
    (500, "Groceries", "Expense"),
    (1_500, "Utilities", "Expense"),
    (2_500, "Utilities", "Expense"),
    (30_000, "Freelance Work", "Income"),
    (500, "Dining Out", "Expense"),
    (1_000, "Dining Out", "Expense")
]
for _add in _add_transaction_data:
    add_transaction(*_add)


summary_report()

filter_expense_by_category("Groceries")
filter_expense_by_category("Utilities")
filter_expense_by_category("Dining Out")