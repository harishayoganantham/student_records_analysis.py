"""
STUDENT RECORDS ANALYSIS SYSTEM
Pass rule: PASS if every subject mark is 40 or above.
Sample ages are assumed because ages were not supplied in the example.
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Student:
    name: str
    age: int
    department: str
    marks: List[float]
    attendance: float

    def average_mark(self) -> float:
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def has_passed(self, pass_mark: float = 40) -> bool:
        return bool(self.marks) and all(mark >= pass_mark for mark in self.marks)


def display_all_students(students: List[Student]) -> None:
    print("\nSTUDENT DETAILS")
    for s in students:
        print(f"{s.name} | Age: {s.age} | {s.department} | "
              f"Marks: {s.marks} | Attendance: {s.attendance:.0f}%")


def display_averages(students: List[Student]) -> None:
    print("\nSTUDENT AVERAGES")
    for s in students:
        print(f"{s.name}: {s.average_mark():.1f}%")


def display_results(students: List[Student]) -> None:
    print("\nRESULT")
    for s in students:
        print(f"{s.name} - {'PASS' if s.has_passed() else 'FAIL'}")


def find_top_performer(students: List[Student]) -> Optional[Student]:
    return max(students, key=lambda s: s.average_mark(), default=None)


def filter_by_attendance(students: List[Student], limit: float) -> List[Student]:
    return [s for s in students if s.attendance < limit]


def filter_by_average(students: List[Student], minimum: float) -> List[Student]:
    return [s for s in students if s.average_mark() >= minimum]


def display_class_summary(students: List[Student]) -> None:
    print("\nCLASS SUMMARY")
    print(f"Total Students: {len(students)}")
    marks = [mark for s in students for mark in s.marks]
    if not marks:
        print("Average Class Mark: N/A")
        print("Top Performer: N/A")
        return
    print(f"Average Class Mark: {sum(marks) / len(marks):.1f}%")
    top = find_top_performer(students)
    print("Top Performer:")
    print(f"{top.name} - Average: {top.average_mark():.1f}%")


def main() -> None:
    # Illustrative ages; replace these records with actual student data.
    students = [
        Student("Dass", 20, "CSE", [78, 85, 72], 91),
        Student("Chandra", 21, "CSE", [65, 71, 68], 84),
        Student("Parvathi", 20, "ECE", [45, 52, 48], 72),
    ]

    display_all_students(students)
    display_averages(students)
    display_results(students)

    print("\nATTENDANCE BELOW 75%")
    for s in filter_by_attendance(students, 75):
        print(f"{s.name} - {s.attendance:.0f}%")

    print("\nAVERAGE MARK AT LEAST 70%")
    for s in filter_by_average(students, 70):
        print(f"{s.name} - {s.average_mark():.1f}%")

    display_class_summary(students)


if __name__ == "__main__":
    main()
