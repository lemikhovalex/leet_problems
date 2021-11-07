import unittest
from solution import Solution


class TestRmLeadingWs(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(2, sol.findMedianSortedArrays(nums1=nums1, nums2=nums2))

    def test_2(self):
        sol = Solution()
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(2.5, sol.findMedianSortedArrays(nums1=nums1, nums2=nums2))

    def test_3(self):
        sol = Solution()
        nums1 = [0, 0]
        nums2 = [0, 0]
        self.assertEqual(0., sol.findMedianSortedArrays(nums1=nums1, nums2=nums2))

    def test_4(self):
        sol = Solution()
        nums1 = []
        nums2 = [1]
        self.assertEqual(1., sol.findMedianSortedArrays(nums1=nums1, nums2=nums2))

    def test_5(self):
        sol = Solution()
        nums1 = [2]
        nums2 = []
        self.assertEqual(2., sol.findMedianSortedArrays(nums1=nums1, nums2=nums2))
