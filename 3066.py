class Solution:
    def minOperations(self, nums: List[int], k: int) -> int: 
        '''
        Not sure why this has such a low acceptance rate but it's 
        pretty simple. We can use a priority queue to keep track
        of the smallest ones, and just keep checking if the length
        of the priority queue is always at least 2, and after
        we finish one operation we just check the beginning of the 
        queue to see if it's greater or equal than 10 in which we 
        can finish the process and simply return how many 
        operations we have done until that point :P 
        '''
        heapq.heapify(nums)
        num_operations = 0
        while(True):
            if(nums[0] >= k):
                break
            if len(nums) < 2:
                break
            fsmol = heapq.heappop(nums)
            ssmol = heapq.heappop(nums)
            heapq.heappush(nums,fsmol*2 + ssmol)
            num_operations += 1
        return num_operations
