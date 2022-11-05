'''
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: 
if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.
'''

t = int(input()) # the number of test cases
for _ in range(t):
    n = int(input()) # the number of cubes
    sideLengths = list(map(int,input().split())) # sideLengths of each cube

    idx_left = 0
    idx_right = len(sideLengths) - 1

    if sideLengths[idx_left] >= sideLengths[idx_right]:
        value = sideLengths[idx_left]
        idx_left += 1
    else:
        value = sideLengths[idx_right]
        idx_right -= 1

    while idx_left != idx_right:
        if sideLengths[idx_left] <= value and sideLengths[idx_right] <= value:
            if sideLengths[idx_left] >= sideLengths[idx_right]:
                value = sideLengths[idx_left]
                idx_left += 1
            else:
                value = sideLengths[idx_right]
                idx_right -= 1
        else:
            break

    if idx_left != idx_right:
        print("No")
    else:
        print("Yes")