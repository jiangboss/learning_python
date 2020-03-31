import random

x = 10
y = 0
z = 0
i = 0


while i < x:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    i = i + 1
    if a > b:
        c = a - b
        print("Please calculate %s - %s" % (a, b))
    else:
        c = a + b
        print("Please calculate %s + %s" % (a, b))

    d = int(input("Your Answer:"))

    if d == c:
        print("Correct!! Congratulation!!")
        y = y + 1
    else:
        print("Incorrect!!, Try another one..")
        z = z + 1


print("Test Complete, your score is: %s" % y)

print("TEst")
