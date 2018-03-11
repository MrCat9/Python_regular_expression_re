#步骤：
#1.抓取网页
#2.获取图片地址
#3.抓取图片内容并保存到本地

from urllib.request import urlopen
import re

req = urlopen('https://www.imooc.com/')
buf = req.read()
print(buf)

buf = buf.decode('utf-8')
# listurl = re.findall(r'src=.+\.jpg', buf)
# print(listurl)
# listurl = re.findall(r'http:.+\.jpg', buf)
# print(listurl)
listurl = re.findall(r'\//img.+?\.jpg', buf)
print(listurl)

i = 0
for url in listurl:
    if url is None:
        continue
    f = open('img'+str(i)+'.jpg', 'wb')  #'wb'-->使用二进制写方式打开文件
    fullurl = 'https:'+url
    req = urlopen(fullurl)
    buf = req.read()
    f.write(buf)
    f.close()
    i+=1



#增强版
from urllib.request import urlopen, Request
import re

headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
req = Request(url='https://tieba.baidu.com/p/5526193514', headers=headers)
buf = urlopen(req).read()  #将网页打开，存入buf
print(buf)

buf = buf.decode('utf-8')
# listurl = re.findall(r'src=.+\.jpg', buf)
# print(listurl)
# listurl = re.findall(r'http:.+\.jpg', buf)
# print(listurl)
listurl = re.findall(r'\//img.+?\.jpg', buf)  #把图片的url用正则表达式匹配出来，存入listurl中
print(listurl)

i = 0  #用于文件命名，从0开始
for url in listurl:
    if url is None:
        continue
    f = open('img'+str(i)+'.jpg', 'wb')  #新建文件  img(数字i).jpg  ，以二进制，写的方式打开
    fullurl = 'http:'+url  #补充url
       
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}    
    req = Request(url=fullurl, headers=headers)
    buf = urlopen(req).read()  #打开图片，存入buf
    
    f.write(buf)  #将图片写入文件中
    f.close()
    i+=1  #i+1，用于下一个文件的文件名
