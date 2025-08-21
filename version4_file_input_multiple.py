def quadratic_temperature(a, b, c, t):
    return a * (t ** 2) + b * t + c

with open("inputs_multiple.txt", "r") as f:
    for line in f:
        if line.strip():
            a, b, c, t = map(float, line.split())
            temperature = quadratic_temperature(a, b, c, t)
            print(f"For coefficients (a={a}, b={b}, c={c}) and t={t} -> Predicted Temperature = {temperature}")
