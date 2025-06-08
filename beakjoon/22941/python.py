import math
import sys
whp, watk, dkhp, dkatk = map(int, sys.stdin.readline().split())
p, s = map(int, sys.stdin.readline().split())
wdc = math.ceil(whp / dkatk)
if p + (dkhp % watk) < watk:
    dkdc = math.ceil(dkhp / watk)
else:
    dkdc = math.ceil((dkhp - p)/watk) if (dkhp - p) % watk <= 0 else math.ceil((dkhp - p) / watk) + 1
    _dkhp = dkhp - dkdc * watk
    _dkhp += s if _dkhp + s <= dkhp else dkhp
    dkdc += math.ceil(_dkhp/watk)
if (wdc >= dkdc):
    print("Victory!")
else:
    print("gg")
