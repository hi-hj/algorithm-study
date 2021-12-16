class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        # 1. preprocess data
        origin_time = list(time[:2] + time[3:])
        digits = sorted(origin_time)

        # Convert Function : list to time
        def conv_string(digits):
            return digits[0]+digits[1]+":"+digits[2]+digits[3]

        
        # check units -> tens -> hundres -> thousands

        for i in range(3, -1, -1):
            for digit in digits:
                if digit > origin_time[i]:
                    # except case (HH < 24, MM < 60)
                    if (i==0 and int(digit)>2) or (i==2 and int(digit)>5):
                        continue
                    elif (i==1 and origin_time[0]=='2' and int(digit)>3):
                        continue
                    else:
                        # Change origin_time
                        # sort after i. to minimum digit
                        origin_time[i] = digit
                        for j in range(i+1, 4):
                            origin_time[j] = digits[0]
                        return conv_string(origin_time)
        
        # Edge case
        # should consider next day
        next_day = digits[0]*4
        return conv_string(next_day)

        