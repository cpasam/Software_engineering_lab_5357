def quadratic_temperature(a, b, c, t):
    return a * (t ** 2) + b * t + c

a, b, c = 1, -2, 30
t = 5

temperature = quadratic_temperature(a, b, c, t)
print(f"At time t={t}, Predicted Temperature = {temperature}")
