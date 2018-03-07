#字符串匹配
#Linux



#找到imooc开头的语句

root@kali:~/Desktop# vi imooc.txt  -->新建一个测试文本，写入一下内容
imooc Java
imooc Html
imooc Python

C
C#
Go
VB

esc  :wq  -->写入并退出

root@kali:~/Desktop# cat imooc.txt  -->查看下imooc.txt
imooc Java
imooc Html
imooc Python

C
C#
Go
VB

root@kali:~/Desktop# vi find_imooc.py  -->写一个脚本，内容如下
f = open('imooc.txt')

for line in f:
    if line.startswith('imooc'):
        print(line)

esc  :wq  -->写入并退出

root@kali:~/Desktop# python find_imooc.py   -->运行脚本
imooc Java

imooc Html

imooc Python

root@kali:~/Desktop# vi find_imooc.py   -->编辑
def find_start_imooc(fname):
    f = open(fname)
    for line in f:
        if line.startswith('imooc'):
            print(line)

find_start_imooc('imooc.txt')

esc  :wq  -->写入并退出

root@kali:~/Desktop# python find_imooc.py   -->运行脚本
imooc Java

imooc Html

imooc Python



#找到imooc开头和结尾的语句

root@kali:~/Desktop# vi imooc.txt  -->编辑测试文本，写入一下内容
imooc Java
imooc Html
imooc Python imooc

C
C#
Go
VB

esc  :wq  -->写入并退出

root@kali:~/Desktop# python find_imooc.py 
imooc Java

imooc Html

imooc Python imooc

root@kali:~/Desktop# vi find_imooc.py   -->编辑
def find_start_imooc(fname):
    f = open(fname)
    for line in f:
        if line.startswith('imooc'):
            print(line)

def find_in_imooc(fname):
    f = open(fname)
    for line in f:
        if line.startswith('imooc') and line[:-1].endswith('imooc'):
            print(line)

#find_start_imooc('imooc.txt')

find_in_imooc('imooc.txt')

esc  :wq  -->写入并退出

root@kali:~/Desktop# python find_imooc.py 
imooc Python imooc



#匹配一个下划线和字母开头的变量名

a = '_value'  #True
a = None  #False
a = ''  #False
a = '1_value'  #False

if a is None or len(a) == 0:
    print('False')
else:
    print(a[0]=='_' or 'a'<=a[0]<='z' or 'A'<=a[0]<='Z')



#
str1 = '1 imooc python'

print(str1.find('imooc'))  #2
print(str1.find('c'))  #6
print(str1.find('1'))  #0

print(str1.startswith('imooc'))  #False
print(str1.startswith('1'))  #True
