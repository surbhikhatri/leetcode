class Solution:
    def reorganizeString(self, s: str) -> str:
        fmap = Counter(s)
        maxheap = [[- val, k] for k, val in fmap.items()]
        heapq.heapify(maxheap) # O(N)
        prev = None
        res = ""

        while maxheap or prev:
            if prev and not maxheap:
                return ""

            # most freq char except prev
            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None

            if cnt < 0:
                prev = [cnt, char]
        
        return res