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
