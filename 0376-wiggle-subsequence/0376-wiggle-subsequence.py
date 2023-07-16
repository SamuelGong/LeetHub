class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        diff = [ ]
        for i in range(len(nums) - 1):
            d = nums[i] - nums[i+1]
            if not d == 0:
                if d > 0:
                    diff.append(1)
                else:
                    diff.append(-1)

        s = 1
        if len(diff) > 0:
            s = 2
            last = diff[0]
            for i in diff[1:]:
                if i + last == 0:
                    s += 1
                    last = i
        return s