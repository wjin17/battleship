from enum import Enum

class HitStatus(Enum):
    MISS = 1
    HIT = 2
    SINK = 3
    WIN = 4