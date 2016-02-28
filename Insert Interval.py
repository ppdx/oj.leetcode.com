# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return "<%d, %d>"%(self.start,self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        return self.merge(intervals+[newInterval])

    def merge(self, intervals):
        if len(intervals)==0:
            return []
        intervals.sort(cmp=lambda x,y:x.start-y.start)
        ret=[intervals[0]]
        for i,n in enumerate(intervals,1):
            if n.start>ret[-1].end:
                ret.append(n)
            elif n.end>ret[-1].end:
                ret[-1].end=n.end
        return ret

def test(*arg):
    for l,n in arg:
        print(l, Solution().insert(l,n))
def make_intervals(l):
    intervals=[]
    for i in l:
        intervals.append(Interval(*i))
    return intervals

test((make_intervals([[1,3],[6,9]]),Interval(2,5)),
     (make_intervals([[1,2],[3,5],[6,7],[8,10],[12,16]]),Interval(4,9)))
