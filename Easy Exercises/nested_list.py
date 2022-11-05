# Given the names and grades for each student in a class of N students, store them in a nested list and 
# print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and 
# print each name on a new line.



if __name__ == '__main__':
    class_list = []

    # New type of input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        class_list.append([name,score])

    change_order_Class_List = [ [s,n] for n,s in class_list ]
    sort_score = sorted(change_order_Class_List)
    min_score = sort_score[0][0]
    for i in range(1,len(sort_score)):
        if sort_score[i][0] != min_score:
            second_min_socre = sort_score[i][0]
            break
    for i in range(1,len(sort_score)):
        if sort_score[i][0] == second_min_socre:
            print(sort_score[i][1])