def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Não pode dividir por 0")
        result = 0
    return result

result = divide(10, 2)
print(result)

result = divide(10, 0)
print(result)