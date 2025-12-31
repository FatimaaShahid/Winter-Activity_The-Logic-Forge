from collections import Counter

def minWindow(log, pattern):
    curr = log + " "
    pattern_count = Counter(pattern)

    for i in range(len(log)):
        substr_post = Counter(log[i:])
        substr_pre = Counter(log[:i+1])
        found_pre = True
        found_post = True

        for ch in pattern_count:
            if substr_pre[ch] < pattern_count[ch]:
                found_pre = False
            if substr_post[ch] < pattern_count[ch]:
                found_post = False
            if not found_post and not found_pre:
                break

        if found_post and len(log[i:]) < len(curr):
            curr = log[i:]
        if found_pre and len(log[:i+1]) < len(curr):
            curr = log[:i+1]

    return "" if curr == log + " " else curr