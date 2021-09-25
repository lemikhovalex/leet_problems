def rm_leading_ws(s: str):
    l: int = 0
    for _c in s:
        if _c == ' ':
            l += 1
        else:
            break
    out = s[l:]
    return out


def check_if_all_allowed(s: str) -> str:
    s_loc = s
    if s == '':
        return '0'
    out: str = ''
    if s_loc[0] in ['+', '-']:
        out = s_loc[0]
        s_loc = s_loc[1:]
    for _c in s_loc:
        if _c.isdigit():
            out += _c
        else:
            break

    if out == '':
        out = '0'
    return out


def clamp(x: int, lower: int, upper: int) -> int:
    out = x
    if x > upper:
        out = upper
    if x < lower:
        out = lower
    return out


class Solution:
    def myAtoi(self, s: str) -> int:
        s = rm_leading_ws(s)
        s = check_if_all_allowed(s)
        out: int = 0
        try:
            out = int(s)
        except ValueError:
            pass
        low_bound = -1 * (2 ** 31)
        upper_bound = (2 ** 31) - 1
        out = clamp(out, lower=low_bound, upper=upper_bound)
        return out
