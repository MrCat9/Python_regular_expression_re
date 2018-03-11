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



#报错：urllib.error.HTTPError: HTTP Error 403: Forbidden
#之所以出现上面的异常,是因为如果用 urllib.request.urlopen 方式打开一个URL,服务器端只会收到一个单纯的对于该页面访问的请求,
#但是服务器并不知道发送这个请求使用的浏览器,操作系统,硬件平台等信息,而缺失这些信息的请求往往都是非正常的访问,例如爬虫.
#有些网站为了防止这种非正常的访问,会验证请求信息中的UserAgent(它的信息包括硬件平台、系统软件、应用软件和用户个人偏好),
#如果UserAgent存在异常或者是不存在,那么这次请求将会被拒绝(如上错误信息所示)
#所以可以尝试在请求中加入UserAgent的信息
#    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
#    req = urllib.request.Request(url='......', headers=headers)  
#    urllib.request.urlopen(req).read()



#爬虫过程报错：http.client.RemoteDisconnected: Remote end closed connection without response
#利用 urllib 发起的请求，UA 默认是 Python-urllib/3.5 
#而在 chrome 中访问 UA 则是 User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)
# AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36，因为服务器根据 UA 来判断拒绝了 python 爬虫。
#把 python 伪装成 chrome 去获取糗百的网页，可以顺利的得到数据。
#    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}  
#    req = request.Request(url='......', headers=headers)
