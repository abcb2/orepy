# -*- coding: utf-8 -*-
import os
import unittest
import posixpath
from posixpath import realpath, abspath, dirname, basename
from test import support

ABSTFN = abspath(support.TESTFN)

def safe_rmdir(dirname):
    try:
        os.rmdir(dirname)
    except OSError:
        pass

class PosixPathTest(unittest.TestCase):

    def setUp(self):
        self.tearDown()

    def tearDown(self):
        for suffix in [ "", "1", "2" ]:
            support.unlink(support.TESTFN + suffix)
            safe_rmdir(support.TESTFN + suffix)

    def test_join(self):
        self.assertEqual(posixpath.join("/foo", "bar", "/bar", "baz"), "/bar/baz")
        self.assertEqual(posixpath.join("foo", "bar"), "foo/bar")
        self.assertEqual(posixpath.join("foo", "bar/"), "foo/bar/")
        self.assertEqual(posixpath.join("foo", "bar", ""), "foo/bar/")
        self.assertEqual(posixpath.join("foo", "/bar", ""), "/bar/")
        self.assertEqual(posixpath.join("/foo", "bar", "baz.txt"), "/foo/bar/baz.txt")
        self.assertEqual(posixpath.join("/foo/", "bar", "baz.txt"), "/foo/bar/baz.txt")
    def test_split(self):
        self.assertEqual(posixpath.split("/foo/bar"), ("/foo", "bar"))
        self.assertEqual(posixpath.split("/"), ("/", ""))
        self.assertEqual(posixpath.split("////foo"), ("////", "foo"))
        self.assertEqual(posixpath.split("//foo//bar"), ("//foo", "bar"))

    def splitextTest(self, path, filename, ext):
        self.assertEqual(posixpath.splitext(path), (filename, ext))
        self.assertEqual(posixpath.splitext("/" + path), ("/" + filename, ext))
        self.assertEqual(posixpath.splitext("abc/" + path), ("abc/" + filename, ext))
        self.assertEqual(posixpath.splitext("/abc.def/" + path), ("/abc.def/" + filename, ext))
        self.assertEqual(posixpath.splitext(path + "/"), (filename + ext + "/", ""))

    def test_splitext(self):
        self.splitextTest("foo.bar", "foo", ".bar")
        self.splitextTest("/foo.bar", "/foo", ".bar")
        
    
        

if __name__ == "__main__":
    unittest.main()
