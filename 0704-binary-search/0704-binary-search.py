class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b, e = 0, len(nums)
        
        while e > b:
            m = int((e + b) / 2)

            if nums[m] == target:
                return m
            elif nums[m] > target:
                e = m
            else:
                b = m + 1

        return -1