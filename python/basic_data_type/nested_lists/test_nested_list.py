import unittest

import nested_list


class NestedList(unittest.TestCase):
    def setUp(self):
        self.students = [
            ['Harry', 37.21],
            ['Berry', 37.21],
            ['Tina', 37.2],
            ['Akriti', 41.0],
            ['Harsh', 39.0]
        ]

    def test_sorted_by_score(self):
        self.assertEqual(
            nested_list.sorted_by_score(self.students)[0][1],
            37.2)

    def test_sorted_by_name(self):
        self.assertEqual(
            nested_list.sorted_by_name(self.students)[0][0],
            'Akriti')

    def test_get_second_lowed_score(self):
        self.assertEqual(
            nested_list.get_second_lowest_score(
                nested_list.sorted_by_score(self.students)
            ),
            37.21
        )

    def test_get_second_lowed_students(self):
        self.assertEqual(
            nested_list.get_second_lowest_students(self.students)[0][0],
            'Berry'
        )


if __name__ == '__main__':
    unittest.main()
