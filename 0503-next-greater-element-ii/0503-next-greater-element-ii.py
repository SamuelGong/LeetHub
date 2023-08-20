class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        monotone_stack = [0]
        result = [-1] * len(nums)
        for idx, n in enumerate(nums[1:]):
            idx += 1
            
            while len(monotone_stack) > 0 and n > nums[monotone_stack[-1]]:
                _idx = monotone_stack.pop(-1)
                result[_idx] = n
            monotone_stack.append(idx)
            
        for idx, n in enumerate(nums[:monotone_stack[-1]]):
            while len(monotone_stack) > 0 and n > nums[monotone_stack[-1]]:
                _idx = monotone_stack.pop(-1)
                result[_idx] = n
            monotone_stack.append(idx)
        
        return result