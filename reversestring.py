def rev_str1(s):
    if type(s) != str:
        raise ValueError('input not string')
    s_arr = list(s)
    return ''.join(s_arr[-1::-1])


def rev_str2(s):
    if type(s) != str:
        raise ValueError('input not string')
    new_s = ''
    for i in range(len(s)-1, -1, -1):
        new_s += s[i]
    return new_s


def rev_rec(s):
    if type(s) != str:
        raise ValueError('input not string')
    if len(s)==1:
        return s
    else:
        return s[-1] + rev_rec(s[:-1])



input = 'guruprasad'
print(rev_str1(input))
print(rev_str2(input))
print(rev_rec(input))