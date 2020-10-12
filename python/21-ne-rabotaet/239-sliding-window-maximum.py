class Solution:
    
    # time limit exceeded
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        maximums = []
        
        maximums.append(max(nums[:k]))
        
        for i in range(1, len(nums)):
            if len(nums[i: i + k]) < k:
                break

            maximums.append(max(nums[i: i + k]))
            
        return maximums
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = []
        cache = []
        
        #maximums.append(max(nums[:k]))
        
        
        def leave_maximum_in_cache(cache, num):
            while cache and nums[cache[-1]] <= num:
                cache = cache[:-1] #remove last
        
        def remove_first_outside_window(cache, i):
            if cache[0] == i - k:
                cache = cache[1:]
        
        for i in range(len(nums)):
            leave_maximum_in_cache(cache, nums[i])
            
            cache.append(i)
            
            remove_first_outside_window(cache, i)
            
            #if len(nums[i: i + k]) < k:
                #break
            if i >= k - 1:
                maximums.append(nums[cache[0]])
            
        return maximums