class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        reference = {}

        monotone_stack = [0]
        for idx, n in enumerate(nums2[1:]):
            idx += 1
            
            while len(monotone_stack) > 0 and n > nums2[monotone_stack[-1]]:
                _idx = monotone_stack.pop(-1)
                reference[nums2[_idx]] = n
            monotone_stack.append(idx)
            
        result = []
        for i in nums1:
            if i in reference:
                result.append(reference[i])
            else:
                result.append(-1)
        return result
            