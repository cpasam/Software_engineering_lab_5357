def quadratic_temperature(a, b, c, t):
    return a * (t ** 2) + b * t + c

with open("inputs_single.txt", "r") as f:
    line = f.readline().strip()
    a, b, c, t = map(float, line.split())

temperature = quadratic_temperature(a, b, c, t)
print(f"At time t={t}, Predicted Temperature = {temperature}")
