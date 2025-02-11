class Solution:
    def clearDigits(self, s: str) -> str:
        '''
        We can tackle this problem by using stacks,
        and that once we find a digit we take a look
        at our current stack of characters we made and 
        check the first non digit and remove that . We
        repeat this process and we return the stringifyed
        version of our final stack :D
        ''' 
        stack = []
        for c in s:
            if c.isdigit():
                if stack:
                    for i in range(len(stack))[::-1]:
                        if not stack[i].isdigit():
                            stack.pop(i)
                            break
            else:
                stack.append(c)
        return "".join(stack)
