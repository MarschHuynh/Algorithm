class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

print(Solution().canConstruct("aa", "aab"))
