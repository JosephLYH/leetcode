from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                results.append("FizzBuzz")
            elif i % 3 == 0:
                results.append("Fizz")
            elif i % 5 == 0:
                results.append("Buzz")
            else:
                results.append(str(i))

        return results


testcases = []
testcases.append([3, ["1", "2", "Fizz"]])
testcases.append([5, ["1", "2", "Fizz", "4", "Buzz"]])
testcases.append(
    (
        15,
        [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ],
    )
)

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
