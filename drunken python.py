# A function called int_to_str() that converts integers into strings and a function called str_to_int() that
# converts strings into integers without using the in built functions "int()" and str().


def str_to_int(num_str):
    dec_places = {11: 10000000000, 10: 1000000000, 9: 100000000, 8: 10000000, 7: 1000000, 6: 100000, 5: 10000, 4: 1000,
                  3: 100, 2: 10, 1: 1}
    char_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    num = 0
    length = len(num_str)
    for i in range(length):
        x = char_digit[num_str[0 - (i + 1)]] * dec_places[i + 1]
        num = num + x
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
