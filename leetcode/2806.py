from copy import deepcopy


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 >= 5:
            purchaseAmount = purchaseAmount + 10 - (purchaseAmount % 10)
        else:
            purchaseAmount = purchaseAmount - (purchaseAmount % 10)

        return int(100 - purchaseAmount)


testcases = []
testcases.append([9, 90])
testcases.append([15, 80])
testcases.append([11, 90])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
