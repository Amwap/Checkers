from dataclasses import dataclass
from typing import List

@dataclass
class Point:
    x: int = 0
    y: int = 0
    


# @dataclass
# class Position(Point):
#     pass

# @dataclass
# class Offset(Point):
#     pass

# @dataclass
# class PosList:
#     points: List[Position]

# @dataclass
# class OffsetList:
#     points: List[Offset]

# s = OffsetList([(1,1), (-1,1), (-1,-1), (1,-1), (1,1), (-1,1)])
# for i in s.points:
#     print(i)
