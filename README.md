# Algorithm: Find the Index of the First Occurrence in a String

## Overview
給定一個兩個字串 haystack, needle，找到needle於haystack的初始位置
備註: 找不到是-1，長度不是空

## Features
Brute Force O(N*M):
-  窮舉所有haystack的位置當作初始位置 (N)
    -  比對needle是否為子字串 (M)

KMP O(N+M)
-  建構next數組，它可以減少重複比對。needle比對失敗時，可以退到上一次比對的最優結果，函數命名nextArr (M)
    -  needle = "ababcaabc", nextArr = [0, 0, 1, 2, 0, 1, 0, 0, 0]
-  當前比對位置表示為pos，最長比對的長度為preLen，
-  同時遍歷haystack 與 needle 的位置， (N)
    -  若haystack[pos] == needle[preLen]，表示單次比對相同，pos += 0 以及 preLen += 1。
    -  若haystack[pos] != needle[preLen]，表示單次比對不同，pos不變， preLen 需要從nextArr找到上一次的最優結果nextArr[preLen - 1]。
    -  若preLen == len(needle)，答案為pos-preLen

```python
# PyTest
pytest "brute force O(N^M).py"
pytest "KMP O(N+M).py"