import math

def is_valid_triangle(a, b, c) -> bool:
    """Return True if the three positive side lengths form a triangle."""
    if a <= 0 or b <= 0 or c <= 0:
        return False

    return (
        a + b > c 
        and a + c > b 
        and b + c > a
    )

def classify_triangle(a, b, c) -> str:
    """Classify a triangle based on its side lengths and right angle property."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        classification = "Equilateral"
    elif a == b or b == c or a == c:
        classification = "Isosceles"
    else:
        classification = "Scalene"

    sides = sorted((a, b, c))

    if math.isclose(
        sides[0] ** 2 + sides[1] ** 2,
        sides[2] ** 2,
        rel_tol=1e-9,
        abs_tol=1e-9,
    ):
        return f"Right {classification}"

    return classification