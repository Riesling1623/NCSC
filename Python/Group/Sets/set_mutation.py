def execute_operation(Ele, operation, other_set):
    if 'intersection_update' in operation:
        Ele.intersection_update(other_set)
    elif 'symmetric_difference_update' in operation:
        Ele.symmetric_difference_update(other_set)
    elif 'difference_update' in operation:
        Ele.difference_update(other_set)
    else:
        Ele.update(other_set)
    return Ele

A = int(input())
Ele = set(map(int,input().split()))
N = int(input())
for _ in range(N):
    operation = input()
    other_set = set(map(int,input().split()))
    Ele = execute_operation(Ele, operation, other_set)
print(sum(Ele))