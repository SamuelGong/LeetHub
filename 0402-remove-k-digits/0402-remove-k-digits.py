class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        
        num_int = []
        discarded_cnt = 0
        for ch in num:
            i = ord(ch) - ord('0')
            if len(num_int) == 0:
                pass
            else:
                while not len(num_int) == 0 and num_int[-1] > i:
                    if discarded_cnt == k:
                        break

                    num_int.pop(-1)
                    discarded_cnt += 1
            num_int.append(i)
        
        num_int = num_int[:len(num) - k]
        leading_zero_ended = False
        new_num = ""
        for i in num_int:
            if not leading_zero_ended:
                if not i == 0:
                    leading_zero_ended = True
                else:
                    continue
            new_num += chr(ord('0') + i)

        if len(new_num) == 0:
            return "0"
        else:
            return new_num