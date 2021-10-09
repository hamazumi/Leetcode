class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        maps = {}
        for i in arr:
            if i not in maps:
                maps[i] = 0
            else:
                maps[i] += 1
        print(maps)
        print(len(maps))
        print(set(maps.values()))
        if len(maps) == len(set(maps.values())):
            return True
        return False