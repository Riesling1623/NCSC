def fun(s):
    idx_at = s.index("@")
    idx_dot = s.index(".")
    # s = "lara@hackerrank.com"
    for c in s.[:idx_at]:
        if c.isidentifier() == False:
            if c != '-'



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)