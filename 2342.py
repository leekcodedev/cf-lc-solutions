class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        '''
        to solve this problem i first thought about using a hash 
        map to store the sum of digits as the key values and the 
        actual values as the part of a list so i can keep track of 
        the biggest numbers for that specific digit sum. after all brute
        force would take so long... so hash map would be the go to solution.
        Then I keep a priority queue to make my life easier since i don't
        have to sort the array value each time to find the biggest 
        ones later :D i do this and i just find the biggest possible
        addition for one of the values in the dictionaries and return it 
        pretty ez stuff :P
        ''' 
        num_map = defaultdict(list)
        solution_exists = False
        for val in nums:
            str_val = str(val)
            key = sum([int(c) for c in str_val])
            heapq.heappush(num_map[key],-1*val)
            #since heapq is min heap by default we can make it max by just reversing it :P
        best = 1
        for num_list in num_map.values():
            if len(num_list) > 1:
                solution_exists = True
                cur = -1 * (heapq.heappop(num_list)+heapq.heappop(num_list))            
                best = max(best,cur)
        
        return best if solution_exists else -1
