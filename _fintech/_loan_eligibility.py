#Loan Eligibility Predictor 

REQUIRED_FIELDS = {
    "credit_score",
    "annual_income",
    "loan_amount",
    "employment_status",
    "debt_to_income_ratio"
}

def validate_applicant_data(_applicant):
    _missing_fields = REQUIRED_FIELDS - _applicant.keys()
    if _missing_fields:
        return f"invalid fields : {_missing_fields}"
    return "All are valid"
    # for _field in REQUIRED_FIELDS:
    #     if _field not in _applicant.keys():
    #         return f"invalid field {_field}"
    # return "All fields are valid"

def check_loan_eligibility(_applicant):
    try:
        validate_applicant_data(_applicant)
        _credit_score = _applicant["credit_score"]
        _annual_income = _applicant["annual_income"]
        _loan_amount = _applicant["loan_amount"]
        _employment_status = _applicant["employment_status"]
        _debt_to_income_ratio = _applicant["debt_to_income_ratio"]
        if (
            _credit_score<650 or 
            _debt_to_income_ratio>40 or 
            _loan_amount > _annual_income*5 or 
            _employment_status.lower()=="unemployed"
            ):
            return "Not Elegible"
        return "Elegible"
    except Exception as err:
        print(f"Error : {err}")


def check_debt_to_income_ratio(_debt_ratio):
    if _debt_ratio>40:
        return "Not Elegible"
    return "Elegible"

def calculate_emi(_loan_amount, _interest_rate, _tenure_year):
    _monthly_interest = (_interest_rate/100)/12
    _number_of_payments = _tenure_year * 12
    _emi = (_loan_amount*_monthly_interest*((1+_monthly_interest)**_number_of_payments))/(((1+_monthly_interest)**_number_of_payments)-1) 
    return f"{_number_of_payments} months, emi : {_emi:.2f}"

def process_applicants_list(_applicants):
    _results = []
    for _app in _applicants:
        _results.append(check_loan_eligibility(_app))
    return _results

_applicant1 ={
    "credit_score": 750,
    "annual_income": 60000,
    "loan_amount": 15000,
    "employment_status": "employed",
    "debt_to_income_ratio": 30
}

_applicant2 ={
    "credit_score": 620,
    "annual_income": 40000,
    "loan_amount": 20000,
    "employment_status": "self-employed",
    "debt_to_income_ratio": 45
}

_applicant3 ={
    "credit_score": 680,
    "annual_income": 50000,
    "loan_amount": 10000,
    "employment_status": "unemployed",
    "debt_to_income_ratio": 25
}

_applicant4 ={
    "credit_score": 720,
    "annual_income": 80000,
    "loan_amount": 25000,
    "employment_status": "employed",
    "debt_to_income_ratio": 20
}

_applicants = [_applicant1, _applicant2, _applicant3, _applicant4]

print(process_applicants_list(_applicants))

for _app in _applicants:
    print(validate_applicant_data(_app))

for _app in _applicants:
    print(check_loan_eligibility(_app))

print(check_debt_to_income_ratio(50)) 
print(check_debt_to_income_ratio(20)) 

_calculate_emi_data = [(200000, 10, 5),(500000, 7, 10)]
for _emi in _calculate_emi_data:
    print(calculate_emi(*_emi)) 