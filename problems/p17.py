#If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
#words, how many letters would be used?

def p17():
    one_to_nine = sum(map(len, ["one", "two","three","four", "five", "six",
        "seven", "eight", "nine"]))
    ten_to_nineteen = sum(map(len, ["ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]))
    twenty_to_ninety = sum(map(len, ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]))

    one_to_ninety_nine = ten_to_nineteen + 9 * one_to_nine + 10 * twenty_to_ninety

    print one_to_ninety_nine + (100 * one_to_nine) + \
        ((100 * len("hundredand") - 3) * 9) + \
        one_to_ninety_nine * 9 + \
        len("onethousand")

p17()
