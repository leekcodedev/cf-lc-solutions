class Solution:
    def smallestNumber(self, pattern: str) -> str:
        '''
        To solve this problem we can use a similar technique as 
        yesterday since I believe they're both backtracking, I tried other
        methods but backtracking seemed to be the only method I could think of
        Essentially I'm going go through each character in the pattern 
        and create a used array of False times the number of elements,
        and I'm going to check if the previous index was I or D, increasing
        or decreasing, and depending on that, I will go through my array
        and use up numbers that satisfy this condition and mark it as used
        and after I'm done with this route, I can return and I can mark
        the number back as unused again, so that I can explore other options :D
        '''
        n = len(pattern) + 1
        valid_numbers = set()
        used = [False] * 10
        def generateNumber(cur,used,pattern,valid_numbers):
            if len(cur) == n:
                valid_numbers.add(cur)
                return
            if len(cur) == 0:
                for j in range(1,10):
                    used[j] = True
                    generateNumber(cur + str(j),used,pattern,valid_numbers)
                    used[j] = False
            else:
                if pattern[len(cur)-1] == 'I':
                    for j in range(1,10):
                        if not used[j] and j > int(cur[-1]):
                            used[j] = True
                            generateNumber(cur+str(j), used,pattern,valid_numbers)
                            used[j] = False
                else:
                    for j in range(1,10):
                        if not used[j] and j < int(cur[-1]):
                            used[j] = True
                            generateNumber(cur+str(j),used,pattern,valid_numbers)
                            used[j] = False
        generateNumber("",used,pattern,valid_numbers)
        return str(min([int(num) for num in list(valid_numbers)]))
