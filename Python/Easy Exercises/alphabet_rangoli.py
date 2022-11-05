# You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
# (Rangoli is a form of Indian folk art based on creation of patterns.)

def print_rangoli(size):
    if size == 1:  
        print('a') 
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        m = 4*(size-1)+1
        for i in range(size):
            number_alphabet_row = 2 * i + 1
            number_of_left_dash = int((m - (2 * number_alphabet_row - 1))/2)
            print('-'*number_of_left_dash, end="")
            for j in range(size-1,size-1-i-1,-1):
                print(alphabet[j] + '-', end = "")
            for k in range(size-i,size):
                if i == size-1 and k == size - 1:
                    print(alphabet[k],end="")
                else:
                    print(alphabet[k] + '-', end="")
            print('-'*(number_of_left_dash - 1))
        for i in range(size-2,-1,-1):
            number_alphabet_row = 2 * i + 1
            number_of_left_dash = int((m - (2 * number_alphabet_row - 1))/2)
            print('-'*number_of_left_dash, end="")
            for j in range(size-1,size-1-i-1,-1):
                print(alphabet[j] + '-', end = "")
            for k in range(size-i,size):
                print(alphabet[k] + '-', end="")
            print('-'*(number_of_left_dash - 1))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)