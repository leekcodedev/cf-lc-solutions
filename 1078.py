class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        '''
        To solve this problem we can first go through the entire 
        array of words we extract from the original string, check
        if the first index and second index matches the first and
        second words as we keep going through the array, and we simply
        add to the array if there exists a word right after it :D
        ''' 
        text_arr = text.split()
        n = len(text_arr)
        res = []
        for i in range(n):
            if i <= n - 3:
                if text_arr[i] == first and text_arr[i+1] == second:
                    res.append(text_arr[i+2])
        return res
