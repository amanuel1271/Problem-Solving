class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[''.join(sorted(s))].append(s)
        return ans.values()