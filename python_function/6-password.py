def validated_password(password):
    if len(password)< 8:
        return False
    has_digit=False
    has_lower=False
    has_upper=False
    has_space=True
    for i in password:
        if  i.isdigit():
            has_digit=True
        elif i.islower():
           has_lower=True
        elif i.isupper():
            has_upper=True
        elif i.isspace():
            has_space=False
    return has_digit and has_lower and has_upper and has_space
print(validated_password("FINLANDer12"))
print()