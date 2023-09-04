# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def convert_temp(celsius):
    fahrenheit = (celsius*9/5) + 32
    print("Fahrenheit: ", "{:.2f}".format(fahrenheit))

def find_max(a, b, c):
    if a > b:
        if a > c:
            print("Maximum  number is ", a)
        else:
            print("Maximum  number is ", c)
    elif b > c:
        print("Maximum number is ", b)
    else:
        print("Maximum number is ", c)

def counts_digits(number):
    max = 0
    min = 9
    count = 0
    while number > 0:
        digit = int(number % 10)
        if digit > max:
            max = digit
        if digit < min:
            min = digit
        count += 1
        number = int(number/10)
    print("Number of digits in number: ", count)
    print("Smallest: ", min)
    print("Highest: ", max)

def sum_of_num(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    print("Sum: ", sum)

def decToBinary(dec):
    flag = 0
    while dec != 0:
        digit = int(dec % 2)
        dec //= 2
        if flag == 0:
            binary = digit
        else:
            binary = str(digit) + str(binary)
        flag = 1

    print("Binary: ", binary)

def decToOctal(dec):
    flag = 0
    while dec != 0:
        digit = int(dec % 8)
        dec //= 8
        if flag == 0:
            octal = digit
        else:
            octal = str(digit) + str(octal)
        flag = 1

    print("Octal: ", octal)

def decToHex(dec):
    flag = 0
    while dec != 0:
        digit = int(dec % 16)
        dec //= 16
        if digit == 10:
            digit = "A"
        elif digit == 11:
            digit = "B"
        elif digit == 12:
            digit = "C"
        elif digit == 13:
            digit = "D"
        elif digit == 14:
            digit = "E"
        elif digit == 15:
            digit = "F"

        if flag == 0:
            hex = digit
        else:
            hex = str(digit) + str(hex)
        flag = 1

    print("Hexadecimal: ", hex)


def main():
    decToBinary(10)
    decToOctal(10)
    decToHex(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Number 1
    '''celsius = float(input("Enter Celsius: "))
    convert_temp(celsius)'''
    # Number 2
    '''a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    find_max(a, b, c)'''
    # Number 3
    '''num = int(input("Enter a number: "))
    counts_digits(num)'''
    # Number 4
    '''number = int(input("Enter number: "))
    sum_of_num(number)'''
    # Number 5
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
