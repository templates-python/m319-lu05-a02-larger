def main():
    number1 = int(input('Give the first number:\n'))
    number2 = int(input('Give the second number:\n'))

    if number1 > number2:
        print('Greater number is: ' + str(number1))
    elif number2 > number1:
        print('Greater number is: ' + str(number2))
    else:
        print('The numbers are equal!')


if __name__ == '__main__':
    main()
