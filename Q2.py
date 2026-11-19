marks_list = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks_list)
print("List  :", marks_list, "->", type(marks_list))
print("Tuple :", marks_tuple, "->", type(marks_tuple))
highest_mark = max(marks_list)
lowest_mark = min(marks_list)
print("Highest mark:", highest_mark)
print("Lowest mark :", lowest_mark)
students_passed = (
    (marks_list[0] >= 40)
    + (marks_list[1] >= 40)
    + (marks_list[2] >= 40)
    + (marks_list[3] >= 40)
    + (marks_list[4] >= 40)
)
print("Students who scored at least 40:", students_passed)
all_marks_valid = lowest_mark >= 0 and highest_mark <= 100
print("All marks within 0-100:", all_marks_valid)
marks_list[1] = 45
print("List after changing index 1 to 45:", marks_list)
print("Tuple is unchanged:", marks_tuple)
