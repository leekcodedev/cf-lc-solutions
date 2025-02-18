#LeekCodeDev
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        '''
        We can use backtracking to solve this problem. Essentially,
        we're going to keep a set to make sure any unique 
        word combination we get will be unique, and 
        once we choose a character, we're going to 
        remove that count of character in our used[] 
        array which will ensure that we only use 
        character which were not used, and once we
        explore all possibilities with that route, we come back
        and add it back to our used and make it false, as we're
        now going to use a different character for exploration :D
        '''
        combinations = set()
        n = len(tiles)
        used = [False] * n

        def backtrack(cur,used,combinations,tiles):
            combinations.add(cur)
            for i,j in enumerate(tiles):
                if not used[i]:
                    used[i] = True
                    backtrack(cur+j,used,combinations,tiles)
                    used[i] = False
        backtrack("",used,combinations,tiles)
        return len(combinations) - 1
