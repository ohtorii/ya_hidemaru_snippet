# -*- coding: utf-8 -*-

import unittest

import intoc

class TestAnchor(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        dup = intoc.Duplicator()

        def assertion(inputstr, expect):
            actual = intoc.sectionname2anchor(inputstr, dup)
            self.assertEqual(actual, expect)

        assertion('aaa', 'aaa')
        assertion('あいうえお', 'あいうえお')
        assertion('You have the wrong number.', 'you-have-the-wrong-number')
        assertion('なんか「NameError: name \'infile\' is not defined」とか出たんだけど',
                  'なんかnameerror-name-infile-is-not-definedとか出たんだけど')

        assertion('aaa', 'aaa-1')
        assertion('『あい』うえお', 'あいうえお-1')

unittest.main()
