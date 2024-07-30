# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 * 1 = 192
# 192 * 2 = 384
# 192 * 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1, 2, 3).

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1, 2, 3, 4, 5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1, 2, ..., n) where n > 1?



def is_pandigital(s):
    if(len(s) < 9):
        return False
    for i in [str(m) for m in range(1, 10)]:
        if i not in s:
            return False
    return True

def p38():
    """
        Ideas that helped narrow down the possible values to search for the pandigital:

        - The target number must start with a 9
        - m can't have 2 or 4 digits; otherwise we can't have a 9-pandigital by concatenating the products
        - m can't be single digit, since m = 9 was already shown as an example
        - If m has 3 digits, it must be <= 500, since otherwise the concatenations can't be a 9-pandigital; but in that case, it can't start with a 9
        - If m has 4 digits, we can have at most 2 products to concatenate, and hence 9000 <= m < 10000, since the concatenation must start with a 9
        - Moreover, m < 9500, because otherwise 2m >= 19000, and so the concatenation can't be pandigital, since it'd have 9 at least twice
    """
    max_val = -1
    for i in range(9000, 9500):
        s = str(i) + str(2 * i)
        if is_pandigital(s) and int(s) > max_val:
            max_val = int(s)
    return max_val

print(p38())