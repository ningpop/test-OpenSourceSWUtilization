def fizzbuzz(number):
    if type(number) != int:
        return number

    if str(number).find('7') >= 0:
        return 'github'
    
    a = number % 3
    b = number % 5
    if a == 0 and b == 0:
        return 'fizzbuzz'
    elif a == 0:
        return 'fizz'
    elif b == 0:
        return 'buzz'
    else:
        return number