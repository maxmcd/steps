from __future__ import print_function
# for ever number n, generate all lists of sums that add up to n
# no number in the list can be repeated, cannot be n
#
# ie: for n=5
# solutions: 2,3 1,4


def compute(n):
    count = [0 for x in range(n+1)]
    count[0] = 1
    for i in range(1, n+1):
        countdown = range(i, n+1)
        countdown.reverse()
        for j in countdown:
            count[j] = count[j] + count[j-i]
    print(count[n] - 1)

compute(200)
