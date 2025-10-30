class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

                (
            )       (
             (          (
              )
        """

        res = set()


        def h(parenthesis, opened, closed):
            if opened + closed == n * 2:
                res.add("".join(parenthesis))
                return

            if opened + closed > n * 2:
                return
            
            if opened > closed:
                h(parenthesis + [')'], opened, closed + 1)
            
            if opened < n:
                h(parenthesis + ['('], opened + 1, closed)

        h([], 0, 0)
        return list(res)

