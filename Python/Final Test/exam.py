import requests
import argparse
import html
import re
import os

# Create folder
path = './exploit-db'
try:
    os.mkdir(path)
except FileExistsError as e:
    print("", end = "")

class MyArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

def exploit_func(id):
    if os.path.exists("./exploit-db/{}.txt".format(id)):
        # Nếu exploit đã có sẵn thì mở trực tiếp tệp chứ không gửi request đến exploit-db.com
        os.popen(os.getcwd() + "./exploit-db/{}.txt".format(id))
    else:
        # Lấy nội dung exploit trong exploit-db, lưu vào máy và mở bằng trình đọc của hệ điều hành
        url = 'https://exploit-db.com/exploits/{}'.format(id)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        res= requests.get(url, headers = headers)
        exploit = res.text[res.text.find('<code') : res.text.find('</code>')]
        exploit = html.unescape(exploit[exploit.find('">') +2 :])
        with open("./exploit-db/{}.txt".format(id), "w") as f:
            f.write(exploit)
            f.close()
        os.popen(os.getcwd() + "./exploit-db/{}.txt".format(id))

def page_func(id):
    # Sắp xếp theo thứ tự tăng dần về ID theo dạng int
    lst_dir = os.listdir(path)
    convert_int = lambda x: int(x[:-4])
    lst_dir = sorted(list(map(convert_int, lst_dir)))

    final_idx = len(lst_dir) - 1
    start_idx = 5*int(id)
    if start_idx + 5 <= final_idx:
        lst = lst_dir[start_idx : start_idx + 5]
    else:
        lst = lst_dir[start_idx : ]
    print(*lst, sep = '\n')

def search_func(keyword):
    key_pat = '|'.join(keyword.split())
    re_genre = r"(?:^|\s)({})(?=$|\s)".format(key_pat)
    regex_pattern = re.compile(re_genre)
    lst_dir = os.listdir(path)
    for fi in lst_dir:
        with open("./exploit-db/{}".format(fi), "r") as f:
            if re.search(regex_pattern, f.read()):
                print(("./exploit-db/{}").format(fi))
            f.close()

if __name__ == '__main__':
    try:
        parser = MyArgumentParser(description = 'Python Exam')
        parser.add_argument('--exploit', metavar = 'EXPLOIT', type = str, help = 'exploit ID')
        parser.add_argument('--page', metavar = 'PAGE', type = str, help = 'get page')
        parser.add_argument('--search', metavar = 'SEARCH', type = str, help = 'Search keyword')
        args = parser.parse_args()
        if args.exploit != None:
            # Người dùng có thể nhập vào dữ liệu có dạng ID của exploit hoặc URL đầy đủ ==> Yêu cầu
            # sử dụng regex
            exploit = ''.join(re.findall(r'[\d]+', args.exploit))
            exploit_func(exploit)
        elif args.page != None:
            page_func(args.page)
        elif args.search != None:
            search_func(args.search)
        else: # khi không truyền tham số ==> trả về trang hướng dẫn
            parser.print_help()
    # khi người dùng truyền sai, trang hướng dẫn được trả về
    except Exception as err:
        parser.print_help()