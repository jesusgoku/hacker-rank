#!/usr/bin/env python

from functools import partial


def get_second_lowest_score(students):
    min_score = students[0][1]
    for i in students:
        if i[1] > min_score:
            min_score = i[1]
            break
    return min_score


sorted_by_score = partial(sorted, key=lambda x: x[1])
sorted_by_name = partial(sorted, key=lambda x: x[0])

# def sorted_by_score(students):
#     return sorted(students, key=lambda x: x[1])


# def sorted_by_name(students):
#     return sorted(students, key=lambda x: x[0])


def get_second_lowest_students(students):
    second_lowest_students = sorted_by_score(students)
    second_lowest_score = get_second_lowest_score(second_lowest_students)
    return sorted_by_name(filter(
                  lambda x: x[1] == second_lowest_score,
                  second_lowest_students))


if __name__ == '__main__':
    students = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        students.append([name, score])

    for s in get_second_lowest_students(students):
        print s[0]
