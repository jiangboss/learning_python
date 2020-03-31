import random

a = random.randint(1, 200)
c = 100
d = 0


while True:
    d = d + 1
    if d > c:
        print(
            "--------------You Tried %s times...You Loss!!---------------------" % c)
        break
    b = int(input("please enter your number:"))
    if b == a:
        print ("++++++++++++Correct!! Congratuation!!++++++++++++++++. You tried %s" % d)
        break
    elif b > a:
        print ("Incorrect!! Greater... You had tried %s " % d)
    else:
        print ("Incorrect!! Less.. You had tried %s " % d)
