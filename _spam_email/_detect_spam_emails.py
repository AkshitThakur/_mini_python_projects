#Detecting Spam Emails
# Detect spam keywords
# Check excessive uppercase letters
# Detect too many links
# Detect multiple exclamation marks
# Calculate a spam score
# Classify email as Spam or Ham

SPAM_WORDS = [
    "free", "win", "winner", "lottery", "prize",
    "money", "cash", "offer", "urgent", "claim",
    "click", "buy now", "discount", "limited",
    "congratulations", "guaranteed", "investment",
    "credit card", "loan", "earn", "bonus"
]

def count_spam_words(_email_content):
    """
    Count and Find spam keywords in email content
    """
    _count_spam_word = 0
    _found_spam_word = []

    for _word in _email_content.lower():
        if _word in SPAM_WORDS:
            _count_spam_word += 1
            _found_spam_word.append(_word)
    return (
        _count_spam_word, 
        _found_spam_word
    )

def calculate_spam_score(_email_content):
    """
    Calculate total Spam Score
    """
    _spam_score = 0
    _spam_word_count, _spam_word_found = count_spam_words(_email_content)
    _spam_score += _spam_word_count*2
    return ({
        "spam_score" : _spam_score,
        "spam_keyword_found" : _spam_word_found
    })

def classify_email(_email_content):
    """
    Classify email as Spam or Ham
    """
    _result = calculate_spam_score(_email_content)
    return (
        ("spam" if _result["spam_score"] >= 8 else "ham"),
        _result
    )

def display_report(_emails):
    """
    Display detailed report
    """
    _category, _result = classify_email(_emails)
    print(f"\nClassification : {_category}")
    print(f"Spam Score : {_result['spam_score']}")
    print(f"Spam Score : {_result['spam_keyword_found']}")

_email_data ="CONGRATULATIONS!!! You are the lucky WINNER of $10000 CASH. Click here now: https://free-money.com Limited offer!!!"

display_report(_email_data)



