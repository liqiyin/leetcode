def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while i < len(nums1):
            nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums.append(nums2[j])
            j += 1

        lenNums = len(nums)
        if lenNums % 2 == 0:
            return float((nums[lenNums / 2] + nums[lenNums / 2 - 1])) / 2
        else:
            return nums[lenNums / 2]

findMedianSortedArrays([1,3], [2])