import math

import pytest

from triangle import classify_triangle, is_valid_triangle


@pytest.mark.parametrize(
    "sides",
    [
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
        (-1, 2, 3),
        (2, -1, 3),
        (3, 2, -1),
    ],
)
def test_is_valid_triangle_rejects_zero_and_negative_side_lengths(sides):
    """Checks that zero-length and negative side lengths are never accepted as valid triangles."""
    assert is_valid_triangle(*sides) is False


@pytest.mark.parametrize(
    "sides",
    [
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
        (-1, 2, 3),
        (2, -1, 3),
        (3, 2, -1),
    ],
)
def test_classify_triangle_rejects_zero_and_negative_side_lengths(sides):
    """Checks that invalid side lengths are classified as Invalid instead of a triangle type."""
    assert classify_triangle(*sides) == "Invalid"


@pytest.mark.parametrize("sides", [(1, 2, 3), (2, 3, 5), (5, 5, 10)])
def test_is_valid_triangle_rejects_degenerate_triangles(sides):
    """Checks the triangle inequality rule: if two sides sum exactly to the third, the shape is degenerate and invalid."""
    assert is_valid_triangle(*sides) is False


@pytest.mark.parametrize("sides", [(1, 2, 3), (2, 3, 5), (5, 5, 10)])
def test_classify_triangle_rejects_degenerate_triangles(sides):
    """Checks that a degenerate triangle is classified as Invalid, not as Equilateral/Isosceles/Scalene."""
    assert classify_triangle(*sides) == "Invalid"


def test_is_valid_triangle_accepts_equilateral_triangle():
    """Checks that an equilateral triangle with all equal positive sides is valid."""
    assert is_valid_triangle(5, 5, 5) is True


def test_classify_triangle_identifies_equilateral_triangle():
    """Checks that all-equal sides are classified as Equilateral."""
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_is_valid_triangle_accepts_isosceles_triangle():
    """Checks that a triangle with two equal positive sides is valid when the triangle inequality holds."""
    assert is_valid_triangle(5, 5, 7) is True


def test_classify_triangle_identifies_isosceles_triangle():
    """Checks that a triangle with two equal sides is classified as Isosceles."""
    assert classify_triangle(5, 5, 7) == "Isosceles"


def test_is_valid_triangle_accepts_scalene_triangle():
    """Checks that a valid scalene triangle with three distinct positive sides passes validation."""
    assert is_valid_triangle(3, 4, 6) is True


def test_classify_triangle_identifies_scalene_triangle():
    """Checks that three unequal sides are classified as Scalene."""
    assert classify_triangle(3, 4, 6) == "Scalene"


def test_is_valid_triangle_accepts_right_scalene_triangle():
    """Checks that the classic 3-4-5 right triangle is valid and satisfies the Pythagorean condition."""
    assert is_valid_triangle(3, 4, 5) is True


def test_classify_triangle_identifies_right_scalene_triangle():
    """Checks that a right triangle with three different side lengths is reported as Right Scalene."""
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_is_valid_triangle_accepts_right_isosceles_triangle_with_float_sides():
    """Checks that a 45-45-90 triangle with sides 5, 5, 5*sqrt(2) is valid despite floating-point rounding."""
    hypotenuse = 5 * math.sqrt(2)
    assert is_valid_triangle(5, 5, hypotenuse) is True


def test_classify_triangle_identifies_right_isosceles_triangle_using_tolerance():
    """Checks that the right-angle test uses floating-point tolerance rather than exact equality for 5, 5, 5*sqrt(2)."""
    hypotenuse = 5 * math.sqrt(2)
    assert classify_triangle(5, 5, hypotenuse) == "Right Isosceles"


@pytest.mark.parametrize(
    "sides",
    [
        (3, 4, 5),
        (4, 3, 5),
        (5, 3, 4),
    ],
)
def test_classify_right_scalene_triangle_regardless_of_side_order(sides):
    """Checks that side order does not affect right-triangle classification."""
    assert classify_triangle(*sides) == "Right Scalene"

def test_classify_non_right_scalene_triangle():
    """Checks that a buildable scalene triangle is not incorrectly flagged as right."""
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_classify_right_triangle_with_hypotenuse_first():
    """Checks that the hypotenuse can be supplied as the first argument."""
    assert classify_triangle(5, 3, 4) == "Right Scalene"