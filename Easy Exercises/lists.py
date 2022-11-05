# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of 
# the 7 types listed above. Iterate through each command in order and perform the corresponding operation 
# on your list.

if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        command = input()
        lst_command = command.split()
        if 'append' in lst_command:
            lst.append(int(lst_command[len(lst_command)-1]))
        elif 'print' in lst_command:
            print(lst)
        elif 'remove' in lst_command:
            lst.remove(int(lst_command[len(lst_command)-1]))
        elif 'sort' in lst_command:
            lst.sort()
        elif 'pop' in lst_command:
            lst.pop()
        elif 'reverse' in lst_command:
            lst.reverse()
        else:
            lst.insert(int(lst_command[len(lst_command)-2]),int(lst_command[len(lst_command)-1]))