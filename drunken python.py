# A function called int_to_str() that converts integers into strings and a function called str_to_int() that
# converts strings into integers without using the in built functions "int()" and str().


def str_to_int(num_str):
    char_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    num = 0
    dec = 1
    length = len(num_str)
    for i in range(length):
        x = char_digit[num_str[0 - (i + 1)]] * dec
        num = num + x
        dec = dec * 10
    return num


def calculate_length(num):
    div = 10
    i = 1
    while num / div >= 1:
        div = div * 10
        i = i + 1
    return i


def int_to_str(num_int):
    word = ""
    div = 10
    char_digit = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    length = calculate_length(num_int)
    for i in range(length):
        x = (num_int % div) // (div // 10)
        word = char_digit[x] + word
        num_int = num_int - x
        div = div * 10
    return word
