class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        b, e = 0, len(nums) - 1
        
        while not b > e:
            while b < e:
                if nums[b] == val:
                    break
                else:
                    b += 1

            while b < e:
                if not nums[e] == val:
                    break
                else:
                    e -= 1
                    k -= 1

            if b == e:
                if nums[b] == val:
                    k -= 1
                break
            else:
                temp = nums[b]
                nums[b] = nums[e]
                nums[e] = temp
                b += 1
                e -= 1
                k -= 1

        return k
            