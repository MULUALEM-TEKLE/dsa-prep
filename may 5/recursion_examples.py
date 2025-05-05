def walk(steps):
    if steps < 1 :
        return
    walk(steps - 1)
    print(f"you've takes {steps } steps")

walk(10)