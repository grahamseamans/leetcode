from itertools import permutations as perm
import numpy as np
from typing import List


def next_perm(lst):
    x = np.array(lst)
    i = len(lst) - 1
    j = i - 1
    while lst[j] >= lst[i] and j >= 0:
        i -= 1
        j -= 1
    flip = j

    i = lst[flip]
    diffs = x[flip:] - i
    diffs = diffs.astype(float)
    diffs[diffs <= 0] = np.inf
    index = np.argmin(diffs)
    index += flip
    x[[flip, index]] = x[[index, flip]]

    x[flip + 1 :] = np.sort(x[flip + 1 :])


def nextPermutation(nums: List[int]) -> None:
    x = np.array(nums)
    i = len(nums) - 1
    j = i - 1
    while nums[j] >= nums[i] and j >= 0:
        i -= 1
        j -= 1
    flip = j

    i = nums[flip]
    diffs = x[flip:] - i
    diffs = diffs.astype(float)
    diffs[diffs <= 0] = np.inf
    index = np.argmin(diffs)
    index += flip
    swap = nums[index]
    nums[index] = nums[flip]
    nums[flip] = swap

    nums[flip + 1 :] = sorted(nums[flip + 1 :])


if __name__ == "__main__":
    a = [2, 0, 1, 3, 4]
    b = [2, 0, 1, 4, 3]
    c = [2, 0, 3, 1, 4]

    # a.sort()

    nextPermutation(a)

    print(a)
