class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansgrams  = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string in ansgrams:
                ansgrams[sorted_string].append(string)
            else:
                ansgrams[sorted_string] = [string]

        return list(ansgrams.values())