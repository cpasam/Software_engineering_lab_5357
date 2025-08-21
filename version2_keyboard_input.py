def quadratic_temperature(a, b, c, t):
    return a * (t ** 2) + b * t + c

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time (t): "))

temperature = quadratic_temperature(a, b, c, t)
print(f"At time t={t}, Predicted Temperature = {temperature}")
