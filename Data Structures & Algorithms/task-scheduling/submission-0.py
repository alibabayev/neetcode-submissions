class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)

        q = deque() # [time, -frequency]
        time = 0

        while max_heap or q:
            if not max_heap:
                time = q[0][0]
            
            while q and q[0][0] <= time:
                freq = q.popleft()[1]
                heapq.heappush(max_heap, freq)
            
            
            # max_heap is always non-none since it will take something from q if max_heap itself is none
            # because if both none then it wouldn't enter while
            freq = heapq.heappop(max_heap)
            freq += 1 # since freq is negative in heap so we decrease it by adding +1
            time += 1

            if freq < 0:
                q.append([time + n, freq])

        return time



            
            
            
                

        