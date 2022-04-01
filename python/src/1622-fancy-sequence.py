from time import perf_counter

"""
https://leetcode.com/problems/fancy-sequence/

Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:

Fancy() Initializes the object with an empty sequence.
void append(val) Appends an integer val to the end of the sequence.
void addAll(inc) Increments all existing values in the sequence by an integer inc.
void multAll(m) Multiplies all existing values in the sequence by an integer m.
int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is
greater or equal than the length of the sequence, return -1.

Example 1:

Input
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex",
"getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
Output
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

Explanation
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20

Constraints:

1 <= val, inc, m <= 100
0 <= idx <= 105
At most 105 calls total will be made to append, addAll, multAll, and getIndex.
"""


class Fancy:
    """
    https://leetcode.com/problems/fancy-sequence/discuss/898861/C%2B%2B-Math-Solution-O(1)-extra-space-and-O(1)-time-for-each
    The solution is to compute the value only when it requested.

    So we need to keep track of the changes to the increment and multiplication.
    With this approach we need to negate the increment and multiplication to an added value.
    """

    def __init__(self):
        self.seq = []
        self.i = 0  # the increment
        self.m = 1  # the multiplication
        self.mod97 = 1000000007

    from functools import cache

    @cache
    def fermat(self, m, y):
        tot, p = 1, m
        while y:
            if y & 1:
                tot = (tot * p) % self.mod97
            p = (p * p) % self.mod97
            y >>= 1
        return tot

    @cache
    def invert(self, x):
        return pow(x, -1, self.mod97)

    def append(self, val: int) -> None:
        # self.seq.append((self.mod97 + val - self.i) * self.fermat(self.m, self.mod97-2))
        self.seq.append((val - self.i) * self.invert(self.m))

    def addAll(self, inc: int) -> None:
        self.i += inc

    def multAll(self, m: int) -> None:
        self.m, self.i = self.m * m % self.mod97, self.i * m % self.mod97

    def getIndex(self, idx: int) -> int:
        return -1 if idx >= len(self.seq) else (self.seq[idx] * self.m + self.i) % self.mod97


if __name__ == '__main__':
    fancy = Fancy()
    tic = perf_counter()

    for m, n in zip(["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"],
                    [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]):
        if m == "Fancy":
            fancy = Fancy()
        elif m == "append":
            fancy.append(n[0])
        elif m == "addAll":
            fancy.addAll(n[0])
        elif m == "multAll":
            fancy.multAll(n[0])
        elif m == "getIndex":
            print(fancy.getIndex(n[0]))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
