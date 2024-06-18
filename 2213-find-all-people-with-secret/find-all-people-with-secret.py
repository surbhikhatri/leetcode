class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # can do bfs, level wise operation
        secrets = set([0, firstPerson]) # result
        time_map = {} # time -> adj list

        for src, dst, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)
        
        def dfs(src, adj):
            if src in visit:
                return
            
            visit.add(src)
            secrets.add(src)

            for nei in adj[src]:
                dfs(nei, adj)


        
        for t in sorted(time_map.keys()): # sorted order
            visit = set()
            for src in time_map[t]:
                if src in secrets:
                    dfs(src, time_map[t])





        return list(secrets)
        
        
        
        known_set = set([0, firstPerson])
        
        sorted_meetings = []
        meetings.sort(key=lambda x:x[2])

        seen_time = set()
        
        for meeting in meetings:
            if meeting[2] not in seen_time:
                seen_time.add(meeting[2])
                sorted_meetings.append([])
            sorted_meetings[-1].append((meeting[0], meeting[1]))
        

        for meeting_group in sorted_meetings:
            people_know_secret = set()
            graph = defaultdict(list)
            
            for p1, p2 in meeting_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in known_set:
                    people_know_secret.add(p1)
                if p2 in known_set:
                    people_know_secret.add(p2)
                    
            queue = deque((people_know_secret))
        
            while queue:
                curr = queue.popleft()
                known_set.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in known_set:
                        known_set.add(neighbor)
                        queue.append(neighbor)

        return list(known_set)







        fmap = defaultdict(list)
        knows = set()
        knows.add(0)
        q = deque()
        q.append((firstPerson, 0))
        q.append((0, 0))

        for x, y, t in meetings:
            fmap[x].append((y, t))
            fmap[y].append((x, t))
            if x == 17 or y == 17:
                print(x, y, t)

        seen = set()
        while q:
            # print(q)
            cur, tcur = q.popleft()
            knows.add(cur)
            if cur not in seen:
                for nxt, tnext in fmap[cur]:
                    if tnext >= tcur and nxt not in seen:
                        q.append((nxt, tnext))
                        knows.add(nxt)
                seen.add(cur)


        return knows




        