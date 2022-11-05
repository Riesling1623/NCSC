# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether 
# the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

n, m = input().split()
A = {}
for i in range(int(n)):
    element = input()
    if element in A:
        A[element].append(str(i+1))
    else:
        A[element] = [str(i+1)]

for i in range(int(m)):
    element = input()
    if element in A:
        print(' '.join(A[element]))
    else:
        print('-1')