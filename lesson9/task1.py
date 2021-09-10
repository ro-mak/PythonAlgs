import hashlib


def Rabin_Karp_modified(s, subs):
    assert len(s) > 0 and len(subs) > 0, 'Strings cannot be empty'
    assert len(s) >= len(subs), 'Substring cannot be longer than original string'
    times = 0
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

            if s[i:i + len_sub] == subs:
                times += 1

    return times


def search_substrings(s):
    s_len = len(s)
    result = 0
    for i in range(1, s_len):
        next_sub = s[:i]
        result += Rabin_Karp_modified(s, next_sub)
    return result


s = input("Input s: ")
print(search_substrings(s))
