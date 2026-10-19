class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        finalSum = 0
        if operations == None or len(operations) == 0:
            return 0

        for i in range(len(operations)):
            if operations[i] == "+":
                res.append(int(res[-2]) + int(res[-1]))
            elif operations[i] == "C":
                res.pop()
            elif operations[i] == "D":
                res.append(int(res[-1]) * 2)
            else:
                res.append(operations[i])
        
        for e in res:
            e = int(e)
            finalSum += e

        return finalSum