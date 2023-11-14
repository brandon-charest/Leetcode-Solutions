from typing import List


def generateParenthesis(n: int) -> List[str]:
    res = []

    def generate(open_paren, close_paren, curr):
        if open_paren == n and close_paren == n:
            res.append(curr)
            return

        if open_paren < n:
            generate(open_paren + 1, close_paren, curr + '(')

        if close_paren < n and close_paren < open_paren:
            generate(open_paren, close_paren + 1, curr + ')')

    generate(0, 0, '')
    return res


print(generateParenthesis(3))
print(generateParenthesis(4))
