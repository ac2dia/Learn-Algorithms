class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        arr = [''] * numRows

        index, step = 0, 1

        for char in s:
            arr[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        output = ''.join(arr)
        return output

