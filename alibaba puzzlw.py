# Read four integers a, b, c, d
a, b, c, d = map(int, input().split())

ops = [
    lambda x,y: x + y,
    lambda x,y: x - y,
    lambda x,y: x * y
]

# Represent operator indices: 0 -> +, 1 -> -, 2 -> *
found = False
for i in range(3):
    for j in range(3):
        if i == j:
            continue  # must not repeat operator
        val = ops[j](ops[i](a, b), c)  # (a op_i b) op_j c
        if val == d:
            found = True
            break
    if found:
        break

print("YES" if found else "NO")
