#LeekCodeDev
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        '''
        to solve this problem, we can take a look 
        at each character as we go through the list 
        and reverse the character, so that we can guarantee
        that our final result will be a commbination of 
        characters never seen before in our list :P 
        '''
        n = len(nums)
        res = ""
        for i in range(n):
            if nums[i][i] == '0':
                res += '1'
            else:
                res += '0'
        return res
