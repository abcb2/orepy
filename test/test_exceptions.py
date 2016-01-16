# -*- coding: utf-8 -*-

import os
import sys
import unittest

class ExceptionTests(unittest.TestCase):

    def raise_catch(self, exc, excname):
        try:
            raise exc("spam")
        except exc as err:
            buf1 = str(err)

        try:
            raise exc("spam")
        except exc as err:
            buf2 = str(err)

        self.assertEqual(buf1, buf2)
        self.assertEqual(exc.__name__, excname)


    
    def testRaising(self):
        self.raise_catch(AttributeError, "AttributeError")
        self.assertRaises(AttributeError, getattr, sys, "hogehoge")
        self.raise_catch(EOFError, "EOFError")
       



if __name__ == "__main__":
    unittest.main()
