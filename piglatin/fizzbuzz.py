def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizzbuzz2(n):
    for i in range(1, n+1):
        output = ""
        if i % 3 == 0:
            output = output + "Fizz"
        if i % 5 == 0:
            output = output + "Buzz"
        if output == "":
            output = str(i)
        print(output)


fizzbuzz(90)
fizzbuzz2(90)
