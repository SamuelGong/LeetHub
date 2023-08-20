class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        monotone_stack = [0]
        
        for idx, t in enumerate(temperatures[1:]):
            idx += 1

            while len(monotone_stack) > 0 and t > temperatures[monotone_stack[-1]]:
                _idx = monotone_stack.pop(-1)
                result[_idx] = idx - _idx
            monotone_stack.append(idx)
            
        return result