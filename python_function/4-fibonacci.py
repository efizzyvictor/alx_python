def fibonacci_sequence(n):
    if n <= 0:
        return "[]"
    elif n==1:
        return "[0]"
    x=[0, 1]
    for i in range(2, n):
        next_number = x[i - 1] + x[i - 2]
        x.append(next_number)
    return x
print(fibonacci_sequence())
