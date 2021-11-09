## Your code here!
def decimalToBin(x,digits):
    counter = 1

    for i in range(1, x):
        counter *= 2
        if counter > x:
            counter //= 2
            break
    num = ""

    while counter != 0:
        if x == counter or x // counter != 0:
            num += "1"
        else:
            num += "0"

        x %= counter
        counter //= 2

    num = num[::-1]
    while len(num) < digits:
        num += "0"

    num = num[::-1]

    return num

def grayCode(digits):
    num = 0
    counter = 1
    current = ""
    lisNums = []
    newlis = []
    for i in range(0,digits):
        num += counter
        counter *= 2

    for x in range(0,num+1):
        lisNums.append(decimalToBin(x,digits))

    for l in lisNums:
        current = l[0]
        for x in range(0,len(l)):
            if x == len(l) -1:
                break
            else:
                if l[x] == l[x+1]:
                    current += "0"
                else:
                    current += "1"
        newlis.append(current)

    return newlis
