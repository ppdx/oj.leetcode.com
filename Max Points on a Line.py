# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return "(x = %d, y = %d)" % (self.x, self.y)

class Solution:
    # @param points, a list of Points
    # @return an integer

    def maxPoints(self, points):
        if len(points) in [0, 1, 2]:
            return len(points)
        ret = 0
        for i in range(0, len(points)):
            data = { }
            column = 0
            samePoints = 1
            for j in range(i + 1, len(points)):
                try:
                    data[(points[i].y - points[j].y)
                         * 1.0 / (points[i].x - points[j].x)] += 1
                except KeyError:
                    data[(points[i].y - points[j].y)
                         * 1.0 / (points[i].x - points[j].x)] = 1
                except ZeroDivisionError:
                    if points[i].y == points[j].y:
                        samePoints += 1
                    else:
                        column += 1
            try:
                tmpmax = max(data.values())
            except Exception:
                tmpmax = 0
            ret = max([tmpmax + samePoints, column + samePoints, ret])
        return ret

def tests(*pointss):
    for p in pointss:
        print(p, Solution().maxPoints(p))

def points(*ps):
    return [Point(*i) for i in ps]

tests(points((0, 0)), points((0, 0), (1, 1), (1, -1)))
