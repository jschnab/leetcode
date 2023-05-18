"""
leetcode 2512: reward top k students

We are given two string arrays 'positive_feedback' and 'negative_feedback',
containing the words denoting positive and negative feedback, respectively.
Note that no word is both positive and negative.

Initially every student has 0 points. Each positive word in a feedback report
increases the points of a student by 3, whereas each negative word decreases
the points by 1.

We are given n feedback reports, represented by a string array 'report' and an
integer array 'student_id' where student_id[i] represents the ID of the student
who has received the feedback report report[i]. The ID of each student is
unique.

Given an integer k, return the top k students after ranking them in
non-increasing order by their points. In case more than one student has the
same points, the one with the lower ID ranks higher.
"""
from collections import defaultdict


def top_students(positive_feedback, negative_feedback, report, student_id, k):
    """
    We assume that all students receive feedback, in other words all student
    IDs are present in the array student_id.
    """
    student_scores = defaultdict(int)
    positive_feedback = set(positive_feedback)
    negative_feedback = set(negative_feedback)
    for sid, rep in zip(student_id, report):
        for word in rep.split():
            if word in positive_feedback:
                student_scores[sid] += 3
            elif word in negative_feedback:
                student_scores[sid] -= 1
            else:
                # if feedback is neutral, we still need to register the student
                # id in the dictionary student_scores
                student_scores[sid] += 0
    return [
        sid for sid, _ in sorted(
            student_scores.items(), key=lambda x: (x[1], -x[0]), reverse=True
        )[:k]
    ]


def test1():
    pos = ["smart", "brilliant", "studious"]
    neg = ["not"]
    report = ["this student is studious", "the student is smart"]
    student_id = [1, 2]
    k = 2
    assert top_students(pos, neg, report, student_id, k) == [1, 2]
    print("test 1 successful")


def test2():
    pos = ["smart", "brilliant", "studious"]
    neg = ["not"]
    report = ["the student is not studious", "the student is smart"]
    student_id = [1, 2]
    k = 2
    assert top_students(pos, neg, report, student_id, k) == [2, 1]
    print("test 2 successful")


def test3():
    pos = ["good"]
    neg = ["bad"]
    report = ["good word", "pretty bad", "nothing to report"]
    student_id = [1, 2, 3]
    k = 2
    assert top_students(pos, neg, report, student_id, k) == [1, 3]
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
