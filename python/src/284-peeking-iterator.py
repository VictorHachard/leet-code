from time import perf_counter

"""
https://leetcode.com/problems/peeking-iterator/

Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next
operations.

Implement the PeekingIterator class:

PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
int next() Returns the next element in the array and moves the pointer to the next element.
boolean hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int
next() and boolean hasNext() functions.

Example 1:

Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]

Explanation
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
All the calls to next and peek are valid.
At most 1000 calls will be made to next, hasNext, and peek.

Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""


# Below is the interface for Iterator, which is already defined for you.
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator: Iterator) -> None:
        self.iterator = iterator
        self.peeked = False
        self.peeked_value = None

    def peek(self) -> int:
        """
        Returns the next element in the iteration without advancing the iterator.
        """
        if not self.peeked:
            self.peeked_value = self.iterator.next()
            self.peeked = True
        return self.peeked_value

    def next(self) -> int:
        if self.peeked:
            self.peeked = False
            return self.peeked_value
        else:
            return self.iterator.next()

    def hasNext(self) -> bool:
        return self.peeked or self.iterator.hasNext()


if __name__ == '__main__':
    tic = perf_counter()

    peekingIterator = PeekingIterator([1, 2, 3])
    peekingIterator.next()
    peekingIterator.peek()
    peekingIterator.next()
    peekingIterator.next()
    peekingIterator.hasNext()

    print(peekingIterator)
    # assert peekingIterator == [None, 1, 2, 2, 3, False]

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
