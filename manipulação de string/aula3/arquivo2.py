import decimal
from decimal import Decimal, getcontext

print(Decimal(1) / Decimal(13))

getcontext().prec = 10

print(Decimal(0.03))

print(Decimal(1) / Decimal(7))

getcontext().rounding = decimal.ROUND_DOWN

print (Decimal(1) / Decimal(7))

print (dir(decimal))