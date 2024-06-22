class Solution:
    def lengthLongestPath(self, input: str) -> int:
        depth = 0
        longest = 0
        pathMap = { 0: 0 }
        lines = input.split("\n")

        for line in lines:
            name = line.lstrip("\t")
            depth = len(line) - len(name)

            if "." in name:
                longest = max(longest, pathMap[depth] + len(name))
            else:
                pathMap[depth + 1] = pathMap[depth] + len(name) + 1
            print(pathMap)
        
        return longest
        