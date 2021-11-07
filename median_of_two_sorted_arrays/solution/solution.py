from typing import List, Union


class Solution:
    answer_is_last: bool
    pair: List[Union[int, None]]
    arrays: List[List[int]]
    pointers: List[int]
    needed_els: float

    def post_init(self, nums1: List[int], nums2: List[int]):
        self.pair = [None, None]
        self.arrays = []
        self.pointers = []
        total_len = 0
        for _arr in [nums1, nums2]:
            if _arr:
                self.arrays.append(_arr)
                self.pointers.append(0)
                total_len += len(_arr)
        self.needed_els = total_len / 2
        self.answer_is_last = sum([len(_a) for _a in self.arrays]) % 2 == 1

    def __update(self, value):
        self.pair = [self.pair[1], value]

    def get_answer(self) -> float:
        out_array = [_x for _x in self.pair if _x is not None]
        if self.answer_is_last:
            return out_array[-1]
        else:
            return sum(out_array) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.post_init(nums1=nums1, nums2=nums2)
        while sum(self.pointers) <= self.needed_els:
            # look for latest values all over array by current pointers
            _not_done_array_indexes = [_i for _i in range(len(self.arrays)) if self.pointers[_i] < len(self.arrays[_i])]
            _values = [self.arrays[_i][self.pointers[_i]] for _i in _not_done_array_indexes]
            index_min = min(range(len(_values)), key=_values.__getitem__)
            index_min = _not_done_array_indexes[index_min]
            # update output pair with latest value
            self.__update(self.arrays[index_min][self.pointers[index_min]])
            self.pointers[index_min] += 1
        return self.get_answer()

