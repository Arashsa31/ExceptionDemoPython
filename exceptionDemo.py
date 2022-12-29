
"""Simple exception handling example."""

while True:
# attempt to convert and divide values
    try:
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter denominator: '))
        result = number1 / number2
    # tried to convert non-numeric value to int
    except ValueError:
        print('You must enter two integers\n')
    # denominator was 0
    except ZeroDivisionError:
        print('Attempted to divide by zero\n')
    # executes only if no exceptions occur
    else:
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
    break # terminate the loop