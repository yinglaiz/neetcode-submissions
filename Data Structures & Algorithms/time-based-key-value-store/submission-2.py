class TimeMap:

    def __init__(self):
        self.add = {}  # key : list of {val, timestamp}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.add:
            self.add[key]=[]    # self.add is now {"alice": []} if key is alice key is default a str 
        self.add[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.add.get(key, [])   # built-in dict .get: returns this key's list of [value, timestamp] pairs, or [] if the key was never set (avoids KeyError)  why values is used not value since we have a 2 things

        #binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

