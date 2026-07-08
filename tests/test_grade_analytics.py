# Run these tests with:
# uv run pytest

import pytest
from grade_analytics import (
    calculate_average,
    get_range_extremes,
    map_score_to_letter,
    apply_curved_bonus,
    generate_grade_report
)

# =====================================================================
# UNIT TESTS (Testing individual functions in isolation)
# =====================================================================

def test_calculate_average_normal():
    """Test calculate_average with standard non-empty lists."""
    assert calculate_average([100, 90, 80]) == 90.0
    assert calculate_average([75, 75, 75]) == 75.0
    assert calculate_average([80, 85]) == 82.5

def test_calculate_average_empty():
    """Test calculate_average handles empty lists gracefully without throwing ZeroDivisionError."""
    assert calculate_average([]) == 0.0

def test_get_range_extremes_normal():
    """Test get_range_extremes with standard lists."""
    assert get_range_extremes([95, 60, 84, 91]) == (95, 60)
    assert get_range_extremes([88]) == (88, 88)

def test_get_range_extremes_empty():
    """Test get_range_extremes returns (None, None) for empty inputs."""
    assert get_range_extremes([]) == (None, None)

@pytest.mark.parametrize("score, expected_letter", [
    (95, "A"),
    (90, "A"),
    (85, "B"),
    (80, "B"),
    (72, "C"),
    (60, "D"),
    (55, "F"),
    (0, "F")
])
def test_map_score_to_letter_boundaries(score, expected_letter):
    """Test standard score tiers and boundary edge cases using parametrization."""
    assert map_score_to_letter(score) == expected_letter

def test_apply_curved_bonus_normal():
    """Test curve function successfully modifies values without exceeding 100."""
    raw_grades = [70, 85, 96]
    bonus = 5.0
    # 96 + 5 becomes 101, which should be capped at 100
    assert apply_curved_bonus(raw_grades, bonus) == [75.0, 90.0, 100.0]


# =====================================================================
# INTEGRATION TESTS (Testing multiple components interacting together)
# =====================================================================

def test_generate_grade_report_no_curve():
    """Integration test checking data flow from scores to letter grades without any curves."""
    class_data = {
        "Alex": [90, 92, 94],  # Average = 92 -> A
        "Charlie": [70, 80, 75] # Average = 75 -> C
    }
    expected_output = {
        "Alex": "A",
        "Charlie": "C"
    }
    assert generate_grade_report(class_data) == expected_output

def test_generate_grade_report_with_curve():
    """Integration test ensuring the curve changes final grades properly through the whole workflow."""
    class_data = {
        "Jordan": [78, 78],     # Average = 78 -> C raw
        "Taylor": [55, 58]      # Average = 56.5 -> F raw
    }
    # Giving a 3-point curve will push Jordan to an 81 (B) and Taylor to 59.5 (F)
    expected_output = {
        "Jordan": "B",
        "Taylor": "F"
    }
    assert generate_grade_report(class_data, bonus=3.0) == expected_output

def test_generate_grade_report_empty_and_edge_cases():
    """Integration test handling missing values inside individual dictionary items."""
    class_data = {
        "MissingStudent": [],
        "PerfectStudent": [100, 100]
    }
    expected_output = {
        "MissingStudent": "F",
        "PerfectStudent": "A"
    }
    assert generate_grade_report(class_data) == expected_output
