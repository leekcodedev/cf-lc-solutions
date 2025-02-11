class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        '''
        To solve this problem we can keep a while loop 
        going while keeping check that "part" exists in our
        current string s, and we keep removing it from the 
        string s until part no longer exists in the string.
        we return our final string s. This is kinda a brute
        force solution, but if you want to be smart about it 
        i guess you can use KMP or stacks, but you know what 
        they say, if it ain't broken, don't fix it :P
        ''' 
        n = len(part)
        while part in s:
            pivot = s.find(part)
            s = s[:pivot] + s[pivot+n:]
        return s
