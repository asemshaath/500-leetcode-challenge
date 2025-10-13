class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def h(output, i):
            if len(output) == len(digits):
                res.append(output)
                return

            for c in numpad[digits[i]]:
                h(output + c, i + 1)

        if len(digits) == 0:
            return res
        h("", 0)
        return res






