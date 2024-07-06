class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [n for n in range(numCourses)]

        prereq = defaultdict(list)
        for c, pre in prerequisites:
            prereq[c].append(pre)
        
        white, grey, black = set(prereq.keys()), set(), set()
        res = []

        def dfs(course):
            grey.add(course)
            for p in prereq[course]:
                if p in black:
                    continue
                
                if p in grey:
                    return False
                
                if not dfs(p):
                    return False
            
            res.append(course)
            grey.remove(course)
            black.add(course)
            return True


        while white:
            course = white.pop()
            if course in black:
                continue

            if not dfs(course):
                return []
        

        for i in range(numCourses):
            if i not in white and i not in res:
                res.append(i)
        return res


        


        