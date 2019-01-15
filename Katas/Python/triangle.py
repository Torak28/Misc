"""
See the following triangle:

____________________________________
 1
 2   4   2
 3   6   9   6   3
 4   8   12  16  12  8   4
 5   10  15  20  25  20  15  10  5
 ___________________________________
The total sum of the numbers in the triangle, up to the 5th line included, is 225, part of it, 144, corresponds to the total sum of the even terms and 81 to the total sum of the odd terms.

Create a function that may output an array with three results for each value of n.

triang_mult(n)  ----> [total_sum, total_even_sum, total_odd_sum]
Our example will be:

triang_mult(5) ----> [225, 144, 81]
Features of the random tests:

number of tests = 100
49 < n < 5000
Enjoy it! This kata will be translated in another languages soon
"""

def mult_triangle(n):
    # Sum of first n cubes; or n-th triangular number squared
    all = int((n * (n + 1) / 2) ** 2)
    # Biquadratic Numbers
    odd = (n // 2) ** 2 ** 2 if n % 2 == 0 else ((n // 2) + 1) ** 2 ** 2
    return [all, all - odd, odd]

def mult_triangle(n):
    ret = []
    for _ in range(n):
        num = _ + 1
        first = num
        step = num
        tmp = [first]
        while num < first ** 2:
            tmp.append(tmp[-1] + step)
            num += step
        x = tmp[:-1]
        ret.extend(tmp + x[::-1])
        sum_all = sum(ret)
        sum_even = sum(filter(lambda x: x % 2 == 0, ret))
        sum_odd = sum_all - sum_even
    return [sum_all, sum_even, sum_odd]
