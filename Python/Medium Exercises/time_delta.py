# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, 
# minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

import datetime as dt

def time_delta(t1,t2):
    # month in a year
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # time
    time1 = dt.datetime(int(t1[3]), month.index(t1[2]) + 1, int(t1[1]), int(t1[4][:2]), int(t1[4][3:5]), int(t1[4][6:]))
    time2 = dt.datetime(int(t2[3]), month.index(t2[2]) + 1, int(t2[1]), int(t2[4][:2]), int(t2[4][3:5]), int(t2[4][6:]))

    # timezone and difference timezone 
    tzone1 = int(t1[5][0] + str(int(t1[5][1:3]) * 3600 + int(t1[5][3:]) * 60))
    tzone2 = int(t2[5][0] + str(int(t2[5][1:3]) * 3600 + int(t2[5][3:]) * 60))
    diffTimezone = tzone1 - tzone2

    # change to the same timezone and find the difference time in seconds
    time2 = time2 + dt.timedelta(seconds = diffTimezone)
    diffTime = time1 - time2

    return int(abs(diffTime.total_seconds()))
    

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input().split()
        t2 = input().split()
        delta = time_delta(t1, t2)
        print(delta)