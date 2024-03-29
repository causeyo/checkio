"""
    From a set of ints you have to create a list of closed intervals as tuples,
so the intervals are covering all the values found in the set.
A closed interval includes its endpoints!
The interval 1..5, for example, includes each value x that satifies the condition 1 <= x <= 5.
Values can only be in the same interval if the difference between a value and the next smaller value in the set equals one,
otherwise a new interval begins. Of course, the start value of an interval is excluded from this rule.
A single value, that does not fit into an existing interval becomes the start- and endpoint of a new interval.

Input: A set of ints.

Output: A list of tuples of two ints, indicating the endpoints of the interval.
The Array should be sorted by start point of each interval
"""


def create_intervals(data):
    list_of_intervals = []
    interval_stop = 0
    data = sorted(list(data))
    if data:
        for i in data:
            if not interval_stop:
                interval_start = i
                interval_stop = i
            elif i == interval_stop + 1:
                interval_stop = i
            else:
                list_of_intervals.append((interval_start, interval_stop))
                interval_start = i
                interval_stop = i
        list_of_intervals.append((interval_start, interval_stop))
    else:
        list_of_intervals.append(data)
    return list_of_intervals


if __name__ == '__main__':
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    assert create_intervals({7, 8}) == [(7, 8)], "Third"
    assert create_intervals({}) == [[]], "Empty"
