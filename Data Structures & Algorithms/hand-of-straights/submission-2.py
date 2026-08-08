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
                    # we need to check whether the value's frequency 
                    # that becomes zero is heap's root or not
                    # because in some cases other next values
                    # can be zero before the heap's root value
                    # so we should not remove the heap's root value 
                    # mistakenly when that value's frequency is not 
                    # actually zero
                    if val != min_heap[0]:
                        return False

                    heapq.heappop(min_heap)
            
        return True

