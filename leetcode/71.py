class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        new_path = []

        for i in range(len(split_path)):
            if not split_path[i] or split_path[i] == ".":
                continue
            elif split_path[i] == "..":
                if new_path:
                    new_path.pop()
            else:
                new_path.append(split_path[i])

        return "/" + "/".join(new_path)


testcases = []
testcases.append(["/home/", "/home"])
testcases.append(["/../", "/"])
testcases.append(["/home//foo/", "/home/foo"])

solution = Solution()
for testcase in testcases:
    assert (
        getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]
    ), testcase
