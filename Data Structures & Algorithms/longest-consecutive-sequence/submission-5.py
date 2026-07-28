class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqMap = defaultdict(int)
        res = 0

        for num in nums:
            if not seqMap[num]:
                leftSeq = seqMap[num-1]
                rightSeq = seqMap[num+1]
                seqMap[num] = leftSeq + rightSeq + 1
                seqMap[num - leftSeq] = seqMap[num]
                seqMap[num + rightSeq] = seqMap[num]
                res = max(res, seqMap[num])
        return res
