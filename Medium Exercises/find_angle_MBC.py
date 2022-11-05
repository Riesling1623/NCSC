import math

degree_sign = u"\N{DEGREE SIGN}"
# print(type(degree_sign))
AB, BC = int(input()), int(input())

# MB is an median line w.r.t AC
# MB = MB
# angle MBC = angle MCB
# So we need to find angle MCB
tan_MCB = AB / BC
# print(math.atan(tan_MCB))
res = (180 / math.pi) * math.atan(tan_MCB)
print(str(round(res)) + degree_sign)