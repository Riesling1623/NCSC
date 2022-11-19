regex_pattern = r"/^M{0,3}(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$"
'''

Cách viết chữ số La Mã:

# Đi từ trái sang phải, giá trị của các chữ số và nhóm chữ số giảm dần(M - D - C - L - X - V - I) tương ứng 
(1000 - 500 - 100 - 50 - 10 - 5 - 1)
-   Các chữ số I, X, C, M không được phép lặp lại quá 3 lần trong một phép tính # Using {0,3}
-   Các chữ số V, L, D chỉ được xuất hiệt một lần duy nhất # Using ? means there is zero or one occurrence
-   Nhóm chữ số đặc biệt: IV(4) - IX(9) - XL(40) - XC(90) - CD(400) - CM(900)


'''

import re
print(str(bool(re.match(regex_pattern, input()))))