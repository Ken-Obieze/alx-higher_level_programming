import os
import unittest
from  models.base import Base
from  models.rectangle import Rectangle
from  models.square import Square


class TestBase_instatntiotion(unittest.TestCase):
    """Test for instantiation of Base."""

    def test_auto_id(self):
        t1 = Base()
        self.assertIsNotNone(t1.id)

    def test_no_arg(self):
        t1 = Base()
        t2 = Base()
        t3 = Base()
        self.assertEqual(t1.id, t2.id - 1)
        self.assertEqual(t2.id + 1, t3.id)

    def test_id_none(self):
        t1 = Base(None)
        t2 = Base(None)
        t3 = Base(None)
        self.assertEqual(t1.id, t2.id -1)
        self.assertEqual(t3.id - 1, t2.id)

    def test_unique_id(self):
        self.assertEqual(Base(89).id, 89)

    def test_id_update(self):
        t1 = Base(16)
        t1.id = 89
        self.assertEqual(t1.id, 89)


if __name__ == "__main__":
    unittest.main()
