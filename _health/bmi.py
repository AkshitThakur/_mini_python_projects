# BMI Calculator & Health Recommendation 

def validate_input(_height : float, _weight : float) -> None:
    if _weight<=0 or _height<=0:
        raise ValueError("Height/Weight must be greater than 0.")

def calculate_bmi(_height : float, _weight : float) -> float:
    validate_input(_height, _weight)      
    bmi = _weight / (_height ** 2)         
    return round(bmi, 2) 

def classify_bmi(bmi : float) -> tuple[str, str]:
    if bmi < 18.5:
        return "Underweight", "Increase calorie intake with a balanced diet."     
    elif 18.5 <= bmi < 24.9:         
        return "Normal Weight", "Maintain a healthy diet and regular exercise."     
    elif 25 <= bmi < 29.9:         
        return "Overweight", "Incorporate a balanced diet and regular physical activity."     
    else:         
        return "Obese", "Consult a nutritionist and engage in a structured fitness program." 

def process_user(_user : list):
    try:
        bmi = calculate_bmi(_user['height'], _user['weight'])
        category, advice = classify_bmi(bmi)
    except Exception as err:
        bmi = None
        category = "invalid"
        advice = str(err)
    return {
        "name": _user["name"],
        "BMI": bmi, 
        "Category": category, 
        "Advice": advice
    }

def batch_bmi_calculations(_users : list[dict]) -> list[dict]:
    return [process_user(_user) for _user in _users]

users = [
    {"name": "Alice", "weight": 55, "height": 1.65},
    {"name": "Bob", "weight": 85, "height": 1.75},
    {"name": "Charlie", "weight": 95, "height": 1.68},
] 
print(batch_bmi_calculations(users)) 
 