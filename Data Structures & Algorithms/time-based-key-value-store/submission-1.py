class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.timeMap.get(key)

        if not entries:
            return ""

        left = 0
        right = len(entries) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if timestamp >= entries[mid][0]:
                result = entries[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result

