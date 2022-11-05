# Given the participants' score sheet for your University 
# Sports Day, you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the 
# score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int,input().split())
    score_list = list(arr)
    sort_score_list = sorted(score_list)
    first_winner = max(sort_score_list)
    for i in range(len(sort_score_list)-2,-1,-1):
        if sort_score_list[i] != first_winner:
            print(sort_score_list[i])
            break