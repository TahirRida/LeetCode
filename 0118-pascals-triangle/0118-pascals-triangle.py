class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        if numRows == 1:
            return res

        for i in range(1, numRows):
            ires = [1]  # Start each row with 1
            for j in range(1, i):  # Loop to calculate intermediate values
                ires.append(res[i - 1][j - 1] + res[i - 1][j])
            ires.append(1)  # End each row with 1
            res.append(ires)

        return res
