def is_prime(number):
    number=int(number)
    for i in range(2, number):
        if number% i==0:
            return False
        
    return True
print(is_prime(17))
    