class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m < 1:
            nums1[:] = nums2[:n]
        elif n <1:
            nums1[:] = nums1[:m]
        else:
            nums1[:] = sorted(nums1[:m] + nums2[:n])