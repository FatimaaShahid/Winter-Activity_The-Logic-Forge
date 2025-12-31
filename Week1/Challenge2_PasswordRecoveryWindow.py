
def minWindow(log, pattern):
    if not log or not pattern or len(log) < len(pattern):
        return ""
    characters = [0]*128
    min_len_found = float('inf')
    left = 0
    right = 0
    missing_letters = len(pattern)
    min_len_left_index = 0

    for char in pattern:
        characters[ord(char)] += 1
    while right<len(log):
        if characters[ord(log[right])] > 0:
            missing_letters -= 1
        characters[ord(log[right])] -=1
        right += 1

        while missing_letters == 0:
            if right - left < min_len_found:
                min_len_left_index = left
                min_len_found = right - left

            if characters[ord(log[left])] == 0:
                missing_letters += 1
            characters[ord(log[left])] += 1
            left += 1

    return "" if min_len_found == float('inf') else log[min_len_left_index:min_len_left_index + min_len_found]
print("Output 1:", minWindow("ADOBECODEBANC", "ABC"))
print("Output 2:", minWindow("a", "a"))
print("Output 3:", minWindow("a", "aa"))