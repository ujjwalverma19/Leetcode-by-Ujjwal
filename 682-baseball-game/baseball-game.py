class Solution:
    def calPoints(self, ops):
        record = []
        for op in ops:
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))
        return sum(record)