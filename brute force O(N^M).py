import pytest
from typing import List

def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    for i in range(n-m+1):
        state = True
        for j in range(m):
            if haystack[i+j] != needle[j]:
                state = False
                break
        if state:
            return i
    return -1

# define the test case
tasks = [('sadbutsad', 'sad', 0), ('leetcode', 'leeto', -1), ('hello', 'll', 2)]
@pytest.mark.parametrize("haystack, needle, ans", tasks)
def test_fn(haystack, needle, ans):
    result = strStr(haystack, needle)
    assert result == ans

