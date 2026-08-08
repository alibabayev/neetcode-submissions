class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 1. initializations and initial state check
        counter = Counter(hand)

        if len(hand) % groupSize:
            return False

        # 2.  heap use
        min_heap = list(counter.keys())
        heapq.heapify(min_heap)

        # 3. trace heap
        while min_heap:
            group_first = min_heap[0]

            for val in range(group_first, group_first + groupSize):
                if counter[val] == 0:
                    return False
                
                counter[val] -= 1

                if counter[val] == 0:
                    heapq.heappop(min_heap)
            
        return True



# {
#     0: 0
#     1: 0
#     2: 0
#     3: 1
#     4: 0
#     5: 1
#     6: 1
#     7: 1
# }

