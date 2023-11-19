# Time: O(logn)
# Space: O(1)


# x^n
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1

    def helper(val, ex):
        if ex == 0:
            return 1
        if ex % 2 == 0:
            return myPow(val * val, ex // 2)
        else:
            return val * myPow(val * val, (ex-1) // 2)

    if n < 0:
        return 1 / helper(x, n)
    return helper(x, n)


print(myPow(2, 10))
