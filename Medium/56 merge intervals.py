"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method
signature.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        else:
            intervals.sort(key=lambda x: x[0])
            result = []
            current_interval = intervals[0]
            result.append(current_interval)

            for interval in intervals[1:]:
                current_interval_end = current_interval[1]
                next_interval_begin = interval[0]
                next_interval_end = interval[1]

                if next_interval_begin <= current_interval_end:
                    current_interval[1] = max(current_interval_end, next_interval_end)
                else:
                    result.append(interval)
                    current_interval = interval

            return result
