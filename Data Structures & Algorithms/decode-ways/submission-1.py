class Solution:
    # Analogy: two doors into a room

    #A room has two doors, a left door and a right door. You want to count every 
    #possible way someone could have walked into the room.
    #Every person came through exactly one of the doors, never both and never       neither.
    #So: total ways in = ways through the left door + ways through the right door.
    #ways here = ways to 1 back + ways to 2 back.
    def numDecodings(self, s: str) -> int:
        count = [0] * (len(s)+1)
        count[0] = 1

        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                count[i] += count [i-1]
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                count[i] += count[i-2] 
        return count[len(s)]