class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    letters = {}
    ansCounter = 0
    count = 0
    left = 0

    for i in range(0, len(s)):
      char = s[i]

      if str(char) in letters and letters[char] >= left:
        # print('%s - IN' % char)
        # Find first letter for new substring
        left = letters[char]
        # Count already included letters
        count = i - left
        letters[char] = i

      else:
        count += 1
        letters[char] = i
        # print('%s - OUT %d' % (char, count))

      if count > ansCounter:
          ansCounter = count

    return ansCounter



my = Solution()

s = 'pwwkew'
ansTrue = 3
# s = ' '
# ansTrue = 1
# s = "dvdf"
# ansTrue = 3

ans = my.lengthOfLongestSubstring(s)
print ('ans = %d [%s]' % (ans, ans == ansTrue))

# pwwkew
# 121231

# Runtime: 52 ms, faster than 93.11% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 38.43% of Python3 online submissions for Longest Substring Without Repeating Characters.