#  ******************* Problem Statement *************************
# Write a program to create a number converter that can convert numbers between binary, decimal, octal and hexadecimal.
# E.g. i/p - Please Enter the base of your input number : 2 Please Enter Binary number : 1111 Please Enter Base for your output number : 8 O/p- 1111 in octal is:0o17



def bintodec(n):
    ind = 0
    output = 0
    while n != 0:
        x = n % 10
        output = output + x * pow(2, ind)
        n = n // 10
        ind = ind + 1
    return output


def bintooct(n):
    output = ''
    while n != 0:
        x = n % 1000
        out = bintodec(x)
        output = str(out) + output
        n = n // 1000
    return int(output)


def bintohex(n):
    output = ''
    while n != 0:
        x = n % 10000
        out = bintodec(x)
        out = str(out)
        if int(out) > 9:
            if out == '10':
                out = 'A'
            elif out == '11':
                out = 'B'
            elif out == '12':
                out = 'C'
            elif out == '13':
                out = 'D'
            elif out == '14':
                out = 'E'
            elif out == '15':
                out = 'F'

        output = out + output
        n = n // 10000
    return output


def dectobin(n):
    output = ""
    while n != 0:
        if n > 0:
            if n % 2 != 0:
                ans = "1"
            else:
                ans = "0"
            n = n / 2
            n = int(n)
            output = ans + output
    return output


def dectooct(n):
    out = dectobin(n)
    output = bintooct(int(out))
    return output


def dectohex(n):
    out = dectobin(n)
    output = bintohex(int(out))
    return output


def octtobin(n):
    output = ''
    while n != 0:
        x = n % 10
        if x >= 8:
            print("Invalid Input !!")
            return 0
        out = dectobin(x)
        if len(out) != 3:
            diff = 3 - len(out)
            for i in range(diff):
                out = '0' + out
        output = str(out) + output
        n = n // 10
    return int(output)


def octtodec(n):
    out = octtobin(n)
    output = bintodec(int(out))
    return output


def octtohex(n):
    out = octtobin(n)
    output = bintohex(int(out))
    return output


def hextobin(n):
    output = ''
    for i in n:
        if i == 'A':
            i = '10'
        elif i == 'B':
            i = '11'
        elif i == 'C':
            i = '12'
        elif i == 'D':
            i = '13'
        elif i == 'E':
            i = '14'
        elif i == 'F':
            i = '15'
        out = dectobin(int(i))
        out = str(out)
        if len(out) != 4:
            diff = 4 - len(out)
            for i in range(diff):
                out = '0' + out
        output = output + out
    return output


def hextooct(n):
    out = hextobin(n)
    output = bintooct(int(out))
    return output


def hextodec(n):
    out = hextobin(n)
    print(out)
    output = bintodec(int(out))
    return output


b = int(input("Please Enter the base of your input number :"))
n = input("Please Enter input number : ")
op = int(input("Please Enter Base for your output number : "))

if b == 2:
    if op == 10:
        output = bintodec(int(n))
        print(output)
    elif op == 8:
        output = bintooct(int(n))
        print(output)
    elif op == 16:
        output = bintohex(int(n))
        print(output)

elif b == 8:
    if op == 2:
        output = octtobin(n)
        print(output)
    elif op == 10:
        output = octtodec(int(n))
        print(output)
    elif op == 16:
        output = octtohex(int(n))
        print(output)

elif b == 10:
    if op == 2:
        output = dectobin(int(n))
        print(output)
    elif op == 8:
        output = dectooct(int(n))
        print(output)
    elif op == 16:
        output = dectohex(int(n))
        print(output)

elif b == 16:
    if op == 2:
        output = hextobin(n)
        print(output)
    elif op == 8:
        output = hextooct(n)
        print(output)
    elif op == 10:
        output = hextodec(n)
        print(output)
