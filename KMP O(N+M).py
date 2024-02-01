import pytest
from typing import List

def strStr(haystack: str, needle: str) -> int:

    def buildNextArr(arr):
        res = [0]*len(arr)
        preLen = 0
        pos = 1
        while pos < len(arr):
            if arr[pos] == arr[preLen]:
                res[pos] = preLen + 1
                preLen += 1
                pos += 1
            else:
                if preLen == 0:
                    pos += 1
                else:
                    preLen = res[preLen-1]
        return res
    
    
    nextArr = buildNextArr(needle)
    preLen = 0
    pos = 0
    while pos < len(haystack):
        if haystack[pos] == needle[preLen]:
            preLen += 1
            pos += 1
        else:
            if preLen > 0:
                preLen = nextArr[preLen-1]
            else:
                pos += 1
        if preLen == len(needle):
            return pos-preLen
    return -1

# define the test case
tasks = [('sadbutsad', 'sad', 0), ('leetcode', 'leeto', -1), ('hello', 'll', 2), ("mississippi", "issip", 4), ("ababcaababcaabc", "ababcaabc", 6)]
@pytest.mark.parametrize("haystack, needle, ans", tasks)
def test_fn(haystack, needle, ans):
    result = strStr(haystack, needle)
    assert result == ans