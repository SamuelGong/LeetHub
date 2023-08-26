class Solution:
    def three_zeros(self, zeros):
        if len(zeros) >= 3:
            return {(0, 0, 0)}
        else:
            return set()
        
    def one_zero(self, zero, neg, pos):
        result = set()
        if len(zero) < 1:
            return result

        j_start_idx = len(pos) - 1
        for i in neg:
            if j_start_idx < 0:
                break
            
            for idx in range(j_start_idx, -1, -1):
                j = pos[idx]
                if j > -i:
                    continue
                else:
                    if j == -i:
                        result.add((i, 0, j))
                    j_start_idx = idx
                    break
        return result
        
    def no_zero(self, neg, pos):
        result = set()
        
        # two negative
        if len(neg) > 1:
            temp = {}
            for idx, i in enumerate(neg[:-1]):
                for _, j in enumerate(neg[idx+1:]):
                    two_sum = i + j
                    if two_sum not in temp:
                        temp[two_sum] = [[i, j]]
                    else:
                        temp[two_sum] += [[i, j]]

            k_start_idx = len(pos) - 1
            for two_sum in sorted(list(temp.keys())):
                for idx in range(k_start_idx, -1, -1):
                    k = pos[idx]
                    if k > -two_sum:
                        continue
                    else:
                        if k == -two_sum:
                            for i, j in temp[two_sum]:
                                result.add((i, j, k))
                        k_start_idx = idx
                        break
        # two positive
        if len(pos) > 1:
            temp = {}
            for idx, i in enumerate(pos[:-1]):
                for _, j in enumerate(pos[idx+1:]):
                    two_sum = i + j
                    if two_sum not in temp:
                        temp[two_sum] = [[i, j]]
                    else:
                        temp[two_sum] += [[i, j]]

            k_start_idx = len(neg) - 1
            for two_sum in sorted(list(temp.keys())):
                for idx in range(k_start_idx, -1, -1):
                    k = neg[idx]
                    if k > -two_sum:
                        continue
                    else:
                        if k == -two_sum:
                            for i, j in temp[two_sum]:
                                result.add((k, i, j))
                        k_start_idx = idx
                        break
                    
        return result
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        first_zero_idx = None
        first_pos_idx = None
        for idx, e in enumerate(nums):
            if e == 0 and first_zero_idx is None:
                first_zero_idx = idx
            elif e > 0 and first_pos_idx is None:
                first_pos_idx = idx
                break
        
        if first_zero_idx is None and first_pos_idx is None:
            return []
        else:
            if first_zero_idx is None:
                neg = nums[:first_pos_idx]
                zero = []
                pos = nums[first_pos_idx:]
            elif first_pos_idx is None:
                neg = nums[:first_zero_idx]
                zero = nums[first_zero_idx:]
                pos = []
            else:
                neg = nums[:first_zero_idx]
                zero = nums[first_zero_idx:first_pos_idx]
                pos = nums[first_pos_idx:]
        
        result = set()
        result = result.union(self.three_zeros(zero))
        result = result.union(self.one_zero(zero, neg, pos))
        result = result.union(self.no_zero(neg, pos))

        new_result = []
        for e in result:
            new_result.append(list(e))
        return new_result