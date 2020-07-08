# Daniel Delijani
# Solution to DEATH BY PROBLEM
import copy
from itertools import combinations
    
def nonbrokenseats(seats):
    ans = []
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            if (seats[r][c] == "."):
                ans += [r * len(seats[0]) + c]
    return ans
         
def valid(chosenseats, seats):
    seats = copy.deepcopy(seats)
    for seat in chosenseats:
        row = seat // len(seats[0])
        col = seat % len(seats[0])
        seats[row][col] = "T"
        if not validseat(row, col, seats):
            return False
    return True

                    
def validseat(row, col, seats):
    if col - 1 >= 0:
        if seats[row][col-1] == "T":
            return False
    if row - 1 >= 0 and col - 1 >= 0:
        if seats[row-1][col-1] == "T":
            return False
    if row - 1 >= 0 and col + 1 <= len(seats[0]) - 1:
        if seats[row-1][col+1] == "T":
            return False
    if col + 1 <= len(seats[0]) - 1:
        if seats[row][col+1] == "T":
            return False
    return True

def maxstudents(seats):
    goodseats = nonbrokenseats(seats)
    for numstudents in range(len(goodseats), 0, -1):
        for combo in combinations(goodseats, numstudents):
            if valid(combo, seats):
                return numstudents