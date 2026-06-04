# Bank Transaction Monitoring System 

from datetime import datetime

TRANSACTION_LIMIT = 1_00_000
SUSPICIOUS_FREQUENCY = 3
suspicious_activity = {} 
REQUIRED_FIELDS = ["account_id", "amount", "transaction_type", "timestamp"] 

def detect_high_value_transaction(_account_id, _amount):
    return (
        f"{_account_id} : Amount limit exceeded {_amount}"
        if _amount > TRANSACTION_LIMIT
        else
        None
    )  

def detect_frequent_transactions(_account_id, _timestamp):
    _timestamps = suspicious_activity.setdefault(_account_id, [])
    _timestamps.append(_timestamp)
    suspicious_activity[_account_id] = [
        _time
        for _time in _timestamps
        if (_timestamp - _time).seconds <60
    ]
    if len(suspicious_activity[_account_id])>SUSPICIOUS_FREQUENCY:
        return f"Number of transaction limit exceeded {_account_id}"
    return None

def validate_transactions_data(_transaction):
    if _missing_fields:= REQUIRED_FIELDS - _transaction.keys():
        return f"Invalid field : {", ".join(_missing_fields)}"
    return None

def monitor_transaction(_transaction):
    try:
        #walrus operator (:=), introduced in Python 3.8.
        if _alert_message := validate_transactions_data(_transaction):
            return _alert_message
        _account_id = _transaction["account_id"]
        _amount = _transaction["amount"]
        _timestamp = _transaction["timestamp"]
        _alert_high_value = detect_high_value_transaction(_account_id, _amount)
        _alert_fraud = detect_frequent_transactions(_account_id, _timestamp)
        return (
            _alert_high_value or
            _alert_fraud or
            f"Transaction Approved : {_account_id}"
        )
    except Exception as err:
        print(err)

def process_transactions(_transactions):
    _result = [monitor_transaction(_transaction) for _transaction in _transactions]
    return _result

_transaction_1 = {
    "account_id": "A001",
    "amount": 10_000,
    "transaction_type": "Transfer",
    "timestamp": datetime.now()
}
_transaction_2 = {
    "account_id": "A002",
    "amount": 500_000,
    "transaction_type": "Withdrawal",
    "timestamp": datetime.now()
}
_transaction_3 = {
    "account_id": "A001",
    "amount": 25_000,
    "transaction_type": "Deposit",
    "timestamp": datetime.now()
}
_transaction_4 = {
    "account_id": "A001",
    "amount": 80_000,
    "transaction_type": "Transfer",
    "timestamp": datetime.now()
}
_transaction_5 = {
    "account_id": "A001",
    "amount": 1_00_000,
    "transaction_type": "Withdrawal",
    "timestamp": datetime.now()
}
_transaction_6 = {
    "account_id": "A002",
    "amount": 2_00_000,
    "transaction_type": "Deposit",
    "timestamp": datetime.now()
}
_transaction_7 = {
    "account_id": "A002",
    "amount": 50_000,
    "transaction_type": "Deposit",
    "timestamp": datetime.now()
}
_transaction_8 = {
    "account_id": "A002",
    "amount": 90_000,
    "transaction_type": "Deposit",
    "timestamp": datetime.now()
}

_transactions = [
    _transaction_1,
    _transaction_2,
    _transaction_3,
    _transaction_4,
    _transaction_5,
    _transaction_6,
    _transaction_7,
    _transaction_8
]

print(process_transactions(_transactions))