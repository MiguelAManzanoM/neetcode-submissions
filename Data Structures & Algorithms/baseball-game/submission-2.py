class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        if operations == None or len(operations) == 0:
            return 0

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)