import unittest

from .solution import rm_leading_ws, check_if_all_allowed, Solution


class TestRmLeadingWs(unittest.TestCase):
    def test_rm_leading_ws_1(self):
        s = '   42'
        self.assertEqual(rm_leading_ws(s), '42')

    def test_rm_leading_ws_2(self):
        s = '   -42'
        self.assertEqual(rm_leading_ws(s), '-42')

    def test_rm_leading_ws_3(self):
        s = '   +42'
        self.assertEqual(rm_leading_ws(s), '+42')

    def test_rm_leading_ws_4(self):
        s = 'a   +42'
        self.assertEqual(rm_leading_ws(s), 'a   +42')


class TestAllowedChars(unittest.TestCase):
    def test_check_if_all_allowed_1(self):
        s = 'a 42'
        res = check_if_all_allowed(s)
        self.assertEqual(res, '0', f'got {res}, expcted ""')

    def test_check_if_all_allowed_2(self):
        s = '42a'
        res = check_if_all_allowed(s)
        self.assertEqual(res, '42', f'got {res}, expcted 42')

    def test_check_if_all_allowed_3(self):
        s = '-42a'
        res = check_if_all_allowed(s)
        self.assertEqual(res, '-42', f'got {res}, expcted -42')


class TestMyAtio(unittest.TestCase):
    def test_my_atoi_1(self):
        cl = Solution()
        inp = '   42'
        exp = 42
        outp = cl.myAtoi(s=inp)
        self.assertEqual(outp, exp, f'got {outp}, expcted {exp}')

    def test_my_atoi_2(self):
        cl = Solution()
        inp = '   -42'
        exp = -42
        outp = cl.myAtoi(s=inp)
        self.assertEqual(outp, exp, f'got {outp}, expcted {exp}')

    def test_my_atoi_3(self):
        cl = Solution()
        inp = '   -42a'
        exp = -42
        outp = cl.myAtoi(s=inp)
        self.assertEqual(outp, exp, f'got {outp}, expcted {exp}')

    def test_my_atoi_4(self):
        cl = Solution()
        inp = '   --42'
        exp = 0
        outp = cl.myAtoi(s=inp)
        self.assertEqual(outp, exp, f'got {outp}, expcted {exp}')

    def test_my_atoi_5(self):
        cl = Solution()
        inp = '-5-'
        exp = -5
        outp = cl.myAtoi(s=inp)
        self.assertEqual(outp, exp, f'got {outp}, expcted {exp}')

    def test_my_atoi_6(self):
        cl = Solution()
        inp = 'a5'
        exp = 0
        outp = cl.myAtoi(s=inp)
        self.assertEqual(outp, exp, f'got {outp}, expcted {exp}')

    def test_my_atoi_7(self):
        cl = Solution()
        inp = ''
        exp = 0
        outp = cl.myAtoi(s=inp)
        self.assertEqual(outp, exp, f'got {outp}, expcted {exp}')
