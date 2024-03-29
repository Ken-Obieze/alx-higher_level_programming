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


class TestBase_to_json(unittest.TestCase):
    """test to create json string."""

    def test_base_to_json_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_base_to_json_emptylist(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_base_to_json_specifics_reloads(self):
        d = [{'x': 11, 'y': 23, 'width': 321, 'id': 54,
             'height': 30}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{"froth": 988}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"froth": 988}]')

        d = [{"froth": 988}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"froth": 988}, {"abc": 123}, {"HI": 0}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 100, 'y': 123, 'width': 321, 'id': 543,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}, {}]')


class TestBase_from_json(unittest.TestCase):
    """ test to read from json file."""

    def test_from_json_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_specific_records(self):
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 123, "width": 321, "id": 54, "height": 34}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 123, 'width': 321, 'id': 54,
             'height': 34}]
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"froth": 98}, {"abc": 123}, {"HI": 0}]
        s = '[{"froth": 98}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"froth": 98}]
        s = '[{"froth": 98}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 101, 'y': 123, 'width': 321, 'id': 54,
             'height': 34}]
        s = '[{"x": 101, "y": 123, "width": 321, "id": 54, \
"height": 34}]'
        self.assertEqual(Base.from_json_string(s), d)

        list_in = [
            {'id': 89, 'width': 8, 'height': 9},
            {'id': 7, 'width': 7, 'height': 7}
        ]
        list_out = Rectangle.from_json_string(
            Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)

if __name__ == "__main__":
    unittest.main()
