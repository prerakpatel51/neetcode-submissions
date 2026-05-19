class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(low, mid, high):
            i, j = low, mid + 1
            temp = []

            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= high:
                temp.append(nums[j])
                j += 1

            nums[low:high + 1] = temp

        def mergesort(low, high):
            if low < high:
                mid = (low + high) // 2
                mergesort(low, mid)
                mergesort(mid + 1, high)
                merge(low, mid, high)

        mergesort(0, len(nums) - 1)
        return nums