# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/181725
def RollingHash(text, pattern):
    a = 31
    h = 998244353
    t_len, p_len = len(text), len(pattern)
    t_hash, p_hash = 0, 0
    a_l = 1   # a的l次方

    # 先计算pattern和text(0,l)的hash
    for i in range(p_len):
        p_hash = (a * p_hash + ord(pattern[i])) % h #对i==0也适用
        t_hash = (a * t_hash + ord(text[i])) % h
        a_l = (a_l * a) % h # 一开始这一步写成了a_l *= a, a_l太大了导致超时
        # a_l *= a % h也不对, 因为a%h还是a, 这并没有对a_l取mod

    #如果一开始就匹配上了
    if p_hash == t_hash:
        print(0)
    l_pt, r_pt = 0, p_len #text中的前后指针, r_pt不能越界
    while r_pt < t_len:
        t_hash = (a * t_hash - a_l * ord(text[l_pt]) + ord(text[r_pt])) % h
        if t_hash == p_hash:
            print(l_pt + 1)
        l_pt += 1
        r_pt += 1
    print()

S = input()
T = input()
RollingHash(S, T)
