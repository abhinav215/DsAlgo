
def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if needle not in haystack:
        return -1
    for i in range(len(haystack)):
        if needle == haystack[i:len(needle)+i]:
            return i