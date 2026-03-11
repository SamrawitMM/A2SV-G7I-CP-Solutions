class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first, second = 0, 0

        output = []
        while first < m and second < n:

            if nums1[first] < nums2[second]:
                output.append(nums1[first])
                first += 1
            else:
                output.append(nums2[second])
                second += 1

        output.extend(nums1[first:m])
        output.extend(nums2[second:n])

        for i in range(m+n):
            nums1[i] = output[i]

    