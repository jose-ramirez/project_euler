#If a box contains twenty-one coloured discs, composed of 
#fifteen blue discs and six red discs, and two discs were 
#taken at random, it can be seen that the probability of 
#taking two blue discs, P(BB) = (15/21)x(14/20) = 1/2. 
#
#The next such arrangement, for which there is exactly 50% 
#chance of taking two blue discs at random, is a box 
#containing eighty-five blue discs and thirty-five red discs. 
#
#By finding the first arrangement to contain over 10^12 = 
#1,000,000,000,000 discs in total, determine the number of 
#blue discs that the box would contain. 

from utils import Utils

u = Utils()

def p100():
    """
        The number of blue discs, b_k, and the total number
        of discs in the arrangement, t_k, are solutions to
        the following Pell equation:

        x_k^2 - 2y_k^2 = -1,

        with x_k = 2t_k - 1, y_k = 2b_k - 1,
        minimal solution given by (x_0, y_0) = (1, 1), and
        the next solution by the given recurrences:

        (x_{k + 1}, y_{k + 1}) = (3x_k + 4y_k, 2x_k + 3y_k)
        for k >= 0.
    """
    x, y = 1, 1
    total = (x + 1) / 2
    while total < 10 ** 12:
        x, y = 3 * x + 4 * y, 2 * x + 3 * y
        total = (x + 1) / 2
    print (y + 1) / 2

u.exec_time(p100)