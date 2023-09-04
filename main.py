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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
