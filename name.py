import re

def analyze_name(user_input):
    # Regular expression to match a constant part of the input
    constant_pattern = r'(my name is|I am|I\'m) (\w+)'

    # Search for the constant part in the user input
    match = re.search(constant_pattern, user_input)

    if match:
        name = match.group(2)
        report = f"Hello {name}! Nice to meet you"
        return report
    else:
        return False


