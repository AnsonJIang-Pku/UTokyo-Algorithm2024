# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/181724
#kmp中这个create_table难理解
def create_table(pattern):
    table = [0] * (len(pattern) - 1)
    j = 0
    for i in range(1, len(pattern) - 1):
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
        else:
            while j > 0 and pattern[i] != pattern[j]: 
                j = table[j-1]
            if pattern[i] == pattern[j]:
                j += 1
                table[i] = j
    return table

def kmp(text, pattern):
    skip = create_table(pattern)

    t_len, p_len = len(text), len(pattern)
    t_i, p_i = 0, 0

    while t_i < t_len and p_i < p_len:
        if text[t_i] == pattern[p_i]:
            t_i += 1
            p_i += 1
        elif p_i == 0:
            t_i += 1
        else:
            p_i = skip[p_i - 1]

    if p_i == p_len:
        print(t_i - p_i)
    else:
        print(-1)

S, T = input(), input()
kmp(S, T)

