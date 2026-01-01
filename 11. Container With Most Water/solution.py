class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height)-1

        while left <right:
            width = right -left
            curr_height = min(height[right], height[left])
            area = width*curr_height
            max_water = max(max_water, area)

            if height[left]<height[right]:
                left +=1
            else:
                right -=1
        return max_water
       
