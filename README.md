# TAMIDCodingChallenge
Coding challenge in Tech application for TAMID at BU

This is my general thought process:

1. Give each spot in the 2-D array a number, and create a new list that contains the numbers of each non-broken seat.

2. Make algorithm that allows to iterate through combinations of a given array.

3. Make algorithm that takes a list of numbers and the 2-D array, and returns true or false whether or not it is valid.

4. Use combination algorithm to generate each combination of numbers starting from n, and working backwards. Then loop through those combinations and see if they are valid using algorith from (3).
    As soon as the algorithm hits a valid combination, return k.