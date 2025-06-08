import sys
import decimal
coupon = {'R':45, 'G':30, 'B':20, 'Y':15, 'O':10, 'W':5,}
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
n = int(sys.stdin.readline())
o = [sys.stdin.readline().split()[:4] for _ in range(n)]
for i in range(n):
    o[i][0] = float(o[i][0]) * ((100-coupon[o[i][1]])/100)
    if o[i][2] == 'C':
        o[i][0] *= 0.95
    a = decimal.Decimal(str(o[i][0]))
    if o[i][3] == 'P':
        o[i][0] = round(a,2)
    else:
        o[i][0] = round(a-decimal.Decimal(0.01),1)
    print('${:.2f}'.format(o[i][0]))
