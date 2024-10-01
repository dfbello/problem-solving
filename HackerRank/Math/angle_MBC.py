# Math - find angle MBC
import math

AB = int(input())
BC = int(input())

AC = math.hypot(AB,BC)

print("{}{}".format(round(math.degrees(math.atan(AB/BC))), chr(176)))



