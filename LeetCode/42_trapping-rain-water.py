# Stack으로도 가능하지만, 직관적이지 않아. 코딩테스트시 생각하기 어렵다.
# Stack으로 다시 풀어보기
class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left +=1
            else:
                volume += right_max - height[right]
                right -=1
        return volume

height = [4,2,0,3,2,5]
Solution().trap(height)