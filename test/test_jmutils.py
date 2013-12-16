import unittest
import jmutils

class Test(unittest.TestCase):
    """Unit tests for jmutils."""

    def test_Struct(self):
        """Test Struct()."""
        Foo = jmutils.Struct('Foo', ('a', 'b'))
        self.assertEqual(repr(Foo(a=5, b=6)),
                         'Foo(a=5, b=6)')
        self.assertEqual(repr(Foo(5)),
                         'Foo(a=5, b=None)')
        x = Foo(b=100)
        self.assertEqual(repr(x),
                         'Foo(a=None, b=100)')
        x.a = 'wut'
        self.assertEqual(repr(x),
                         "Foo(a='wut', b=100)")

if __name__ == "__main__":
    unittest.main()
