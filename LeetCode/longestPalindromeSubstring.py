from operator import floordiv
def expandAroundCenter(s,left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1

def longestPalindrome(s):

    if (s == None or len(s) < 1):
        return "" 
    
    start, end = 0 , 0

    for i in range(0,len(s)):
        len1 = expandAroundCenter(s,i,i)
        len2 = expandAroundCenter(s,i,i+1)

        flen = max(len1,len2)

        if flen > (end-start):
            start = int(i - (floordiv((flen-1),2)))
            end = int(i + (floordiv(flen,2)))

    return s[start:end+1]


print(longestPalindrome("cbbd"))

