fib_numb = 1
last_numb = 0
i = 0


while i < 30:
    fib_numb = fib_numb + last_numb
    last_numb = fib_numb - last_numb
    i += 1
    print(f"{i}. {fib_numb}")

