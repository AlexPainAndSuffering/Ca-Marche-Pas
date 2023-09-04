#
#(n)
#(k)
#= n! /k!(n-k)!
#
import math

#card (x; N, n ,k)
# N = nb card in deck
# k = target to find
# n card you draw
# x the number of card you want

# [kCx][N-kCn-x]/[NCn]


def calculateCombi(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def calculateCardProbability(x, N, n, k):
    combi1 = calculateCombi(k, x)
    combi2 = calculateCombi(N-k, n-x)
    combi3 = calculateCombi(N, n)
    
    return combi1*combi2*combi3


