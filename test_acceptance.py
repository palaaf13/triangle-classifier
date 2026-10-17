
from triangle import classify_triangle, is_valid_triangle


def test_customer_can_build_a_regular_triangle():
    """A valid triangle should be approved as buildable."""
    assert is_valid_triangle(4, 5, 6) is True
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_customer_is_warned_about_right_angle_reinforcement():
    """A right triangle should be identified for reinforced corners."""
    result = classify_triangle(3, 4, 5)
    assert result == "Right Scalene"


def test_customer_is_not_told_to_build_an_impossible_triangle():
    """Impossible side lengths must be rejected."""
    assert is_valid_triangle(1, 2, 3) is False
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_invalid_triangle_returns_a_result_without_crashing():
    """Invalid dimensions should return a result rather than raising an error."""
    result = classify_triangle(-1, 2, 3)
    assert result == "Invalid"


def test_customer_can_build_an_equilateral_triangle():
    """Three equal valid sides should be identified correctly."""
    assert is_valid_triangle(5, 5, 5) is True
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_right_triangle_is_detected_regardless_of_side_order():
    """Reordering dimensions must not change the right-angle warning."""
    assert classify_triangle(5, 3, 4) == "Right Scalene"
    assert classify_triangle(4, 5, 3) == "Right Scalene"
