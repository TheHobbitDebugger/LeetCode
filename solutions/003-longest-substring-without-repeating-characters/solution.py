class Solution:
    def lenghtOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        # O(n)
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            w = (r - 1) + 1
            longest = max(longest, w)
            sett.add(s[r])

        return longest
                       