class ProductOfNumbers:

    def __init__(self):
        self.stack = []
        self.zeroCount = 0
    def add(self, num: int) -> None:
        if num == 0:
            self.zeroCount += 1
        if len(self.stack) == 0:
            self.stack.append((num,self.zeroCount)) 
        else:
            prev = self.stack[-1][0]
            if prev != 0:
                self.stack.append((prev*num,self.zeroCount))
            else:
                self.stack.append((num,self.zeroCount))
    def getProduct(self, k: int) -> int:
        if self.stack[-k][0] == 0:
            return 0
        elif self.stack[-1][1] != self.stack[-k][1]:
            return 0
        else:
            if k == len(self.stack):
                return self.stack[-1][0]
            else:
                if self.stack[-k-1][0] == 0:
                    return self.stack[-1][0]
                else:
                    return self.stack[-1][0] // self.stack[-k-1][0]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
#Digged my head around this one... so I knew we could do this in one pass
'''
because the problem said we could do it O(1) time, and the only time this would
work is if we have some sort of prefix sum, or i guess "product" in this case,
going on, since we can just divide the current product and the product at the 
beginning range and get how many numbers we multiplied in that range. However
I ran into an obstacle the moment I saw a 0... basically we have to identify if
there is a 0 in the range we are looking at. I thought of many ways but they 
weren't really O(1) time, so the only thing i came up with is keeping count 
of the zeros, and if we ever had an increase of 0's during that range, that 
means a 0 was present and we just return 0, otherwise we can just return
the dividing result. The only case I had to separately handle was if 0 was the beginning
of the range, which would mean that it wouldn't increase the number of 0's
seen, so I just check that the beginning is not zero, and that's pretty much it!
'''
