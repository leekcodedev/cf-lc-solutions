#LeekCodeDev

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        '''
        solving this question requires backtracking AGAIN, and the only difficulty
        here is really keeping track of state and how to change the state for
        future recursive calls. One may realize that first I can keep track of a 
        used array of 3 size with truthy falsy values to mark each index as
        a,b,c respectively. and i keep a running string to make sure i add
        to the result array once the length reaches n. For example, 
        when I have the current string "ab", I have the used array be something
        like F T F, as T being t he most recently used, I have to reset everything
        to false false false and then set just B as the truth before passing it 
        on. This is because if you can see if we didn't reset it, a would mark
        first as true, b would mark second as true, and if we pass "ab", we would
        only get "abc" as a possible route, even tohugh "aba", is also clearly valid,
        so we have to reset every array as falsy first and set just one latest
        as true to avoid this issue. However, this can also create another issue
        which we can solve. Recall that at "ab", the truthiness array is "FTF",
        and once we hit "aba", as length n is 3, we return back. However this is 
        where it gets tricky. when we passed an array to aba, we transformed
        the array everything as false false false and just the middle one B to 
        true so that we avoid missing out on some combinations. However, in doing so,
        we accidentally change the state of the array it was before hand. 
        If it was "ab", it used to be FTF, but we changed it to be TFF since
        we used A last. Since A gets returned, the previous state needs to return
        as well. Looking at the transformed array of TFF, this would assume we can
        make ABB, since B is False, but that's clearly not working, since we need
        to rely on other state FTF, before transformation. So all we have to do is 
        keep track of the previous state array as temp variable and set the array
        to that temp array once we finish exploring a route using backtracking :D
        '''
        happy_strings = []
        used = [False] * 3
        def bt(cur,happy_strings,used):
            if len(cur) == n:
                happy_strings.append(cur)
                return
            for i in range(3):
                if not used[i]:
                    temp = used
                    used = [False] * 3
                    used[i] = True
                    bt(cur+chr(97+i),happy_strings,used)
                    used = temp
        bt("",happy_strings,used)
        if k > len(happy_strings):
            return "" 
        else:
            happy_strings.sort()
            return happy_strings[k-1]
