import math

fx = "x**3 - x - 1"    # F(X)
e = 0.001
a = 1
b = 1.5

iteration = 0
error = 10  # Start with a large error
c = None

def find_c(a, b) -> float:
    return (a + b) / 2

def find_fx(num) -> float:
    f_num = fx.replace("x", f"({num})")
    return eval(f_num)

print(f"{'i':<2} | {'a':<10} | {'f(a)':<10} | {'b':<10} | {'f(b)':<10} | {'c':<10} | {'f(c)':<10} | error")

while error >= e:
    c_before = c
    c = find_c(a, b)
    fa = find_fx(a)
    fb = find_fx(b)
    fc = find_fx(c)

    if iteration == 0:
        error_str = "—"  # Placeholder for first row
    else:
        error = abs(c_before - c)
        error_str = f"{error:<10.4f}"

    print(f"{iteration:<2} | {a:<10.4f} | {fa:<10.4f} | {b:<10.4f} | {fb:<10.4f} | {c:<10.4f} | {fc:<10.4f} | {error_str}")

    if iteration != 0 and error < e:
        print("\nRoot found:", c)
        break

    if fa * fc < 0:
        b = c
    else:
        a = c

    iteration += 1
