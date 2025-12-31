class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            freq[nums[right]] +=1
            current_sum += nums[right]

            if right -left+1 >k:
                freq[nums[left]] -=1
                current_sum -= nums[left]
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left +=1

            if right - left +1 == k and len(freq) == k:
                max_sum = max(max_sum, current_sum)
        return max_sum


        
