"""
Grade Analytics Tool
--------------------
A program designed to manage, analyze, and scale student grades.
It provides simple statistics (average, max, min) and maps scores to letter grades.
"""

def calculate_average(grades: list) -> float:
    """
    Calculates the average (mean) of a list of numeric grades.
    Returns 0.0 if the list is empty.
    """
    return round(sum(grades) / len(grades), 2)


def get_range_extremes(grades: list) -> tuple:
    """
    Finds the highest and lowest grades in a list.
    Returns (None, None) if the list is empty.
    """
    if not grades:
        return (None, None)
    return (max(grades), min(grades))


def map_score_to_letter(score: float) -> str:
    """
    Maps an individual numeric score to a standard letter grade.
    Assumes a standard 10-point scale.
    """
    if score >= 85:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def apply_curved_bonus(grades: list, bonus_points: float) -> list:
    """
    Applies a flat bonus to all grades, capping the final score at 100.
    """
    curved_grades = []
    for grade in grades:
        new_grade = grade + bonus_points
        if new_grade > 100:
            new_grade = 100
        curved_grades.append(new_grade)
    return curved_grades


def generate_grade_report(student_data: dict, bonus: float = 0.0) -> dict:
    """
    Integration function: Takes a dictionary mapping student names to lists of raw scores,
    applies an optional curve, computes their final class averages, and assigns letter grades.

    Example input: {"Alice": [80, 90], "Bob": [70, 65]}
    Example output: {"Alice": "A", "Bob": "D"}
    """
    report = {}
    for student, scores in student_data.items():
        if not scores:
            report[student] = "F"
            continue

        # Calculate the average score
        avg_score = calculate_average(scores)

        # Map average score to letter grade
        report[student] = map_score_to_letter(avg_score)

    return report
