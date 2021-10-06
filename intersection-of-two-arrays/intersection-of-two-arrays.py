class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                s.append(nums1[i])

            else:
                continue

        return set(s)