# while loops

x = 0
while x < 10:
    print(f"print x -> {x}")
    x += 1

# if you do not increment x it will give an infinite loop of 0

x = 0
while x < 10:
    if x == 5:
        break
    print(f"print x -> {x}")
    x += 1
