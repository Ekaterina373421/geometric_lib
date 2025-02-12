import unittest
import circle
import rectangle
import square
import triangle


class CircleTests(unittest.TestCase):
    def test_integer_or_float(self):
        area_result1 = circle.area(3)
        area_result2 = circle.area(5.1)
        area_result3 = circle.area(10.234)
        perimeter_result1 = circle.perimeter(1)
        perimeter_result2 = circle.perimeter(5.4)
        perimeter_result3 = circle.perimeter(8.009)
        self.assertEqual(area_result1, 28.274333882308138)
        self.assertEqual(area_result2, 81.7128249198705)
        self.assertEqual(area_result3, 329.03394002511953)
        self.assertEqual(perimeter_result1, 6.283185307179586)
        self.assertEqual(perimeter_result2, 33.929200658769766)
        self.assertEqual(perimeter_result3, 50.322031125201306)

    def test_negative_and_zero(self):
        area_zero_result = circle.area(0)
        area_negative_result = circle.area(-2)
        perimeter_zero_result = circle.perimeter(0)
        perimeter_negative_result = circle.perimeter(-7)
        self.assertEqual(area_zero_result, "radius cannot be zero")
        self.assertEqual(area_negative_result, "radius cannot be negative")
        self.assertEqual(perimeter_zero_result, "radius cannot be zero")
        self.assertEqual(perimeter_negative_result, "radius cannot be negative")

    def test_not_integer_or_float_type(self):
        area_result1 = circle.area(True)
        area_result2 = circle.area('2')
        area_result3 = circle.area("3")
        area_result4 = circle.area([5])
        area_result5 = circle.area({7})
        perimeter_result1 = circle.perimeter(False)
        perimeter_result2 = circle.perimeter('4')
        perimeter_result3 = circle.perimeter("6")
        perimeter_result4 = circle.perimeter([8])
        perimeter_result5 = circle.perimeter({10})
        self.assertEqual(area_result1, "radius must be integer or float values")
        self.assertEqual(area_result2, "radius must be integer or float values")
        self.assertEqual(area_result3, "radius must be integer or float values")
        self.assertEqual(area_result4, "radius must be integer or float values")
        self.assertEqual(area_result5, "radius must be integer or float values")
        self.assertEqual(perimeter_result1, "radius must be integer or float values")
        self.assertEqual(perimeter_result2, "radius must be integer or float values")
        self.assertEqual(perimeter_result3, "radius must be integer or float values")
        self.assertEqual(perimeter_result4, "radius must be integer or float values")
        self.assertEqual(perimeter_result5, "radius must be integer or float values")


class RectangleTests(unittest.TestCase):
    def test_integer_or_float(self):
        area_result1 = rectangle.area(3, 5)
        area_result2 = rectangle.area(7, 5)
        area_result3 = rectangle.area(5.9, 15)
        area_result4 = rectangle.area(5.908, 2)
        area_result5 = rectangle.area(11, 17.203)
        area_result6 = rectangle.area(9, 6.1)
        area_result7 = rectangle.area(3.31, 7.7)
        area_result8 = rectangle.area(16.6, 10.27)
        perimeter_result1 = rectangle.perimeter(6, 15)
        perimeter_result2 = rectangle.perimeter(7, 6)
        perimeter_result3 = rectangle.perimeter(5.91, 15)
        perimeter_result4 = rectangle.perimeter(5.6, 2)
        perimeter_result5 = rectangle.perimeter(11, 17.23)
        perimeter_result6 = rectangle.perimeter(9, 6.1)
        perimeter_result7 = rectangle.perimeter(3.31, 6.17)
        perimeter_result8 = rectangle.perimeter(16.06, 10.2)
        self.assertEqual(area_result1, 15)
        self.assertEqual(area_result2, 35)
        self.assertEqual(area_result3, 88.5)
        self.assertEqual(area_result4, 11.816)
        self.assertEqual(area_result5, 189.233)
        self.assertEqual(area_result6, 54.9)
        self.assertEqual(area_result7, 25.487000000000002)
        self.assertEqual(area_result8, 170.482)
        self.assertEqual(perimeter_result1, 42)
        self.assertEqual(perimeter_result2, 26)
        self.assertEqual(perimeter_result3, 41.82)
        self.assertEqual(perimeter_result4, 15.2)
        self.assertEqual(perimeter_result5, 56.46)
        self.assertEqual(perimeter_result6, 30.2)
        self.assertEqual(perimeter_result7, 18.96)
        self.assertEqual(perimeter_result8, 52.519999999999996)

    def test_negative_and_zero(self):
        area_result1 = rectangle.area(-16, -2)
        area_result2 = rectangle.area(0, -7)
        area_result3 = rectangle.area(-15, 0)
        area_result4 = rectangle.area(0, 0)
        area_result5 = rectangle.area(-10, 7)
        area_result6 = rectangle.area(8, -5)
        area_result7 = rectangle.area(0, 11)
        area_result8 = rectangle.area(20, 0)
        perimeter_result1 = rectangle.perimeter(-8, -3)
        perimeter_result2 = rectangle.perimeter(-5, 0)
        perimeter_result3 = rectangle.perimeter(0, -7)
        perimeter_result4 = rectangle.perimeter(-12, 7)
        perimeter_result5 = rectangle.perimeter(9, -47)
        perimeter_result6 = rectangle.perimeter(0, 0)
        perimeter_result7 = rectangle.perimeter(16, 0)
        perimeter_result8 = rectangle.perimeter(0, 2)
        self.assertEqual(area_result1, "sides of rectangle must be natural")
        self.assertEqual(area_result2, "sides of rectangle must be natural")
        self.assertEqual(area_result3, "sides of rectangle must be natural")
        self.assertEqual(area_result4, "sides of rectangle must be natural")
        self.assertEqual(area_result5, "sides of rectangle must be natural")
        self.assertEqual(area_result6, "sides of rectangle must be natural")
        self.assertEqual(area_result7, "sides of rectangle must be natural")
        self.assertEqual(area_result8, "sides of rectangle must be natural")
        self.assertEqual(perimeter_result1, "sides of rectangle must be natural")
        self.assertEqual(perimeter_result2, "sides of rectangle must be natural")
        self.assertEqual(perimeter_result3, "sides of rectangle must be natural")
        self.assertEqual(perimeter_result4, "sides of rectangle must be natural")
        self.assertEqual(perimeter_result5, "sides of rectangle must be natural")
        self.assertEqual(perimeter_result6, "sides of rectangle must be natural")
        self.assertEqual(perimeter_result7, "sides of rectangle must be natural")
        self.assertEqual(perimeter_result8, "sides of rectangle must be natural")

    def test_not_integer_or_float_type(self):
        area_result1 = rectangle.area(True, 5)
        area_result2 = rectangle.area(9, False)
        area_result3 = rectangle.area([5, 7], True)
        area_result4 = rectangle.area('5', "12")
        perimeter_result1 = rectangle.perimeter(0, {0})
        perimeter_result2 = rectangle.perimeter(15, [3])
        perimeter_result3 = rectangle.perimeter("8", {0})
        perimeter_result4 = rectangle.perimeter(2, [14, 6, 7])
        self.assertEqual(area_result1, "sides of rectangle must be integer or float values")
        self.assertEqual(area_result2, "sides of rectangle must be integer or float values")
        self.assertEqual(area_result3, "sides of rectangle must be integer or float values")
        self.assertEqual(area_result4, "sides of rectangle must be integer or float values")
        self.assertEqual(perimeter_result1, "sides of rectangle must be integer or float values")
        self.assertEqual(perimeter_result2, "sides of rectangle must be integer or float values")
        self.assertEqual(perimeter_result3, "sides of rectangle must be integer or float values")
        self.assertEqual(perimeter_result4, "sides of rectangle must be integer or float values")


class SquareTests(unittest.TestCase):
    def test_integer_or_float(self):
        area_result1 = square.area(3)
        area_result2 = square.area(7.5)
        area_result3 = square.area(3.978)
        area_result4 = square.area(0.12)
        perimeter_result1 = square.perimeter(15)
        perimeter_result2 = square.perimeter(7.3)
        perimeter_result3 = square.perimeter(16.456)
        perimeter_result4 = square.perimeter(0.27)
        self.assertEqual(area_result1, 9)
        self.assertEqual(area_result2, 56.25)
        self.assertEqual(area_result3, 15.824484000000002)
        self.assertEqual(area_result4, 0.0144)
        self.assertEqual(perimeter_result1, 60)
        self.assertEqual(perimeter_result2, 29.2)
        self.assertEqual(perimeter_result3, 65.824)
        self.assertEqual(perimeter_result4, 1.08)

    def test_negative_and_zero(self):
        area_result1 = square.area(-16)
        area_result2 = square.area(0)
        area_result3 = square.area(-15.234)
        perimeter_result1 = square.perimeter(-8)
        perimeter_result2 = square.perimeter(0)
        perimeter_result3 = square.perimeter(-7.987)
        self.assertEqual(area_result1, "sides of square must be natural")
        self.assertEqual(area_result2, "sides of square must be natural")
        self.assertEqual(area_result3, "sides of square must be natural")
        self.assertEqual(perimeter_result1, "sides of square must be natural")
        self.assertEqual(perimeter_result2, "sides of square must be natural")
        self.assertEqual(perimeter_result3, "sides of square must be natural")

    def test_not_integer_or_float_type(self):
        area_result1 = square.area(True)
        area_result2 = square.area('2')
        area_result3 = square.area("3")
        area_result4 = square.area([5])
        area_result5 = square.area({7})
        perimeter_result1 = square.perimeter(False)
        perimeter_result2 = square.perimeter('4')
        perimeter_result3 = square.perimeter("6")
        perimeter_result4 = square.perimeter([8])
        perimeter_result5 = square.perimeter({10})
        self.assertEqual(area_result1, "sides of square must be integer or float values")
        self.assertEqual(area_result2, "sides of square must be integer or float values")
        self.assertEqual(area_result3, "sides of square must be integer or float values")
        self.assertEqual(area_result4, "sides of square must be integer or float values")
        self.assertEqual(area_result5, "sides of square must be integer or float values")
        self.assertEqual(perimeter_result1, "sides of square must be integer or float values")
        self.assertEqual(perimeter_result2, "sides of square must be integer or float values")
        self.assertEqual(perimeter_result3, "sides of square must be integer or float values")
        self.assertEqual(perimeter_result4, "sides of square must be integer or float values")
        self.assertEqual(perimeter_result5, "sides of square must be integer or float values")


class TriangleTests(unittest.TestCase):
    def test_integer_or_float(self):
        area_result1 = triangle.area(3, 5)
        area_result2 = triangle.area(7, 5)
        area_result3 = triangle.area(5.9, 15)
        area_result4 = triangle.area(5.908, 2)
        area_result5 = triangle.area(11, 17.203)
        area_result6 = triangle.area(9, 6.1)
        area_result7 = triangle.area(3.31, 7.7)
        area_result8 = triangle.area(16.6, 10.27)
        perimeter_result1 = triangle.perimeter(15, 32, 20)
        perimeter_result2 = triangle.perimeter(5, 4.23, 3)
        perimeter_result3 = triangle.perimeter(10, 13, 16.22)
        perimeter_result4 = triangle.perimeter(4, 4, 6.9)
        self.assertEqual(area_result1, 7.5)
        self.assertEqual(area_result2, 17.5)
        self.assertEqual(area_result3, 44.25)
        self.assertEqual(area_result4, 5.908)
        self.assertEqual(area_result5, 94.6165)
        self.assertEqual(area_result6, 27.45)
        self.assertEqual(area_result7, 12.743500000000001)
        self.assertEqual(area_result8, 85.241)
        self.assertEqual(perimeter_result1, 67)
        self.assertEqual(perimeter_result2, 12.23)
        self.assertEqual(perimeter_result3, 39.22)
        self.assertEqual(perimeter_result4, 14.9)

    def test_negative_and_zero(self):
        area_result1 = triangle.area(-16, -2)
        area_result2 = triangle.area(0, -7)
        area_result3 = triangle.area(-15, 0)
        area_result4 = triangle.area(0, 0)
        area_result5 = triangle.area(-10, 7)
        area_result6 = triangle.area(8, -5)
        area_result7 = triangle.area(0, 11)
        area_result8 = triangle.area(20, 0)
        perimeter_result1 = triangle.perimeter(-7, -13, -16)
        perimeter_result2 = triangle.perimeter(0, -23.98, -16.4)
        perimeter_result3 = triangle.perimeter(-15.9, -20, 0)
        perimeter_result4 = triangle.perimeter(-12, 0, 0)
        perimeter_result5 = triangle.perimeter(17, 20, 0)
        perimeter_result6 = triangle.perimeter(7, 5, -6)
        perimeter_result7 = triangle.perimeter(-10, 0, 16.8)
        perimeter_result8 = triangle.perimeter(0, 0, 0.23)
        self.assertEqual(area_result1, "sides and height of triangle must be natural")
        self.assertEqual(area_result2, "sides and height of triangle must be natural")
        self.assertEqual(area_result3, "sides and height of triangle must be natural")
        self.assertEqual(area_result4, "sides and height of triangle must be natural")
        self.assertEqual(area_result5, "sides and height of triangle must be natural")
        self.assertEqual(area_result6, "sides and height of triangle must be natural")
        self.assertEqual(area_result7, "sides and height of triangle must be natural")
        self.assertEqual(area_result8, "sides and height of triangle must be natural")
        self.assertEqual(perimeter_result1, "sides of triangle must be natural")
        self.assertEqual(perimeter_result2, "sides of triangle must be natural")
        self.assertEqual(perimeter_result3, "sides of triangle must be natural")
        self.assertEqual(perimeter_result4, "sides of triangle must be natural")
        self.assertEqual(perimeter_result5, "sides of triangle must be natural")
        self.assertEqual(perimeter_result6, "sides of triangle must be natural")
        self.assertEqual(perimeter_result7, "sides of triangle must be natural")
        self.assertEqual(perimeter_result8, "sides of triangle must be natural")

    def test_not_integer_or_float_type(self):
        area_result1 = triangle.area(True, 5)
        area_result2 = triangle.area(9, False)
        area_result3 = triangle.area([5, 7], True)
        area_result4 = triangle.area('5', "12")
        perimeter_result1 = triangle.perimeter(True, [0], 15)
        perimeter_result2 = triangle.perimeter(0, [0], 10)
        perimeter_result3 = triangle.perimeter({9}, False, 1)
        perimeter_result4 = triangle.perimeter(9, 9, "9")
        self.assertEqual(area_result1, "sides and height of triangle must be integer or float values")
        self.assertEqual(area_result2, "sides and height of triangle must be integer or float values")
        self.assertEqual(area_result3, "sides and height of triangle must be integer or float values")
        self.assertEqual(area_result4, "sides and height of triangle must be integer or float values")
        self.assertEqual(perimeter_result1, "sides of triangle must be integer or float values")
        self.assertEqual(perimeter_result2, "sides of triangle must be integer or float values")
        self.assertEqual(perimeter_result3, "sides of triangle must be integer or float values")
        self.assertEqual(perimeter_result4, "sides of triangle must be integer or float values")

    def test_triangle_exist(self):
        perimeter_result1 = triangle.perimeter(5, 15, 2)
        perimeter_result2 = triangle.perimeter(22, 5, 7)
        perimeter_result3 = triangle.perimeter(5, 15, 100)
        self.assertEqual(perimeter_result1, "triangle doesn't exist")
        self.assertEqual(perimeter_result2, "triangle doesn't exist")
        self.assertEqual(perimeter_result3, "triangle doesn't exist")


if __name__ == '__main__':
    unittest.main()
