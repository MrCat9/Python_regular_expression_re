#正则表达式概念
1:使用单个字符串来描述匹配一系列符合某个句法规则的字符串
2: 是对字符串操作的一种逻辑公式
3: 应用场景: 处理文本和数据
4: 正则表达式过程: 依次拿出表达式和文本中的字符比较，如果每一个字符都能匹配，则匹配成功; 否则匹配失败。



import re  #导入python正则表达式模块
pa = re.compile(r'imooc\n')  #pa = re.compile('imooc\\n')  -->生成pattern的实例
print(pa)  #re.compile('imooc\\n')
print(type(pa))  #<class '_sre.SRE_Pattern'>

pa = re.compile(r'imooc')
print(pa)  #re.compile('imooc')
print(type(pa))  #<class '_sre.SRE_Pattern'>

str1 = 'imooc python'
print(pa.match(str1))  #<_sre.SRE_Match object; span=(0, 5), match='imooc'>

ma = pa.match(str1)
print(ma.group())  #imooc  -->group()返回str或者tuple
print(ma.span())  #(0, 5)  -->匹配的位置

print(ma.string)  #imooc python  -->被匹配的字符串会放在string中
print(ma.re)  #re.compile('imooc')  -->Pattern实例会放在re中

pa1 = re.compile(r'_')
ma1 = pa1.match('_value')
print(ma1.group())  #_
print(ma1.string)  #_value

#如需匹配忽略大小写时
pa = re.compile(r'imooc', re.I)  #忽略大小写
print(pa)  #re.compile('imooc', re.IGNORECASE)
ma = pa.match('imooc python')
print(ma.group())  #imooc
ma = pa.match('ImoOc python')
print(ma.group())  #ImoOc
print(ma.string)  #ImoOc python

#ma.groups()
pa = re.compile(r'(imooc)', re.I)
print(pa)  #re.compile('(imooc)', re.IGNORECASE)
ma = pa.match('imooc python')
print(ma.group())  #imooc
print(ma.groups())  #('imooc',)

ma = re.match(r'imooc', 'imooc python', re.I)  #要多次匹配的时候建议生成pattern对象
print(ma)  #<_sre.SRE_Match object; span=(0, 5), match='imooc'>
print(ma.group())  #imooc
print(ma.groups())  #()  -->r'imooc'  没加()，所以返回空



#match方法会从头开始匹配

#re模块的search方法  -->在一个字符串中查找第一个匹配
#re.search(pattern, string, flags)
#如：查找str1中的数字
import re
str1 = 'imooc videonum = 1000'
print(str1.find('1000'))  #17

info = re.search(r'\d+', str1)
print(info.group())  #1000

str1 = 'imooc videonum = 2000'
info = re.search(r'\d+', str1)
print(info.group())  #2000



#findall方法  -->找到匹配，返回所有匹配部分的列表  #所有！
#re.findall(pattern, string, flags)
import re
str2 = 'c++ = 100, java = 90, python = 80'
info = re.search(r'\d+', str2)
print(info.group())  #100

info = re.findall(r'\d+', str2)
print(info)  #['100', '90', '80']
print(sum([int(x) for x in info]))  #270



#sub方法  -->将字符串中匹配正则表达式的部分替换为其他值
#re.sub(pattern, repl, string, count, flags)  #repl可以是一个string（会替换成该string），也可以是个方法（会替换成方法的返回值）
#repl是一个string时
import re
str3 = 'imooc videonum = 1000'
info = re.sub(r'\d+', '1001', str3)
print(info)  #imooc videonum = 1001

#repl是一个方法时
import re
str3 = 'imooc videonum = 1000'

def add1(match):
    val = match.group()
    num = int(val)+1
    return str(num)
    
info = re.sub(r'\d+', add1, str3)
print(info)  #imooc videonum = 1001

str3 = 'imooc videonum = 10'
info = re.sub(r'\d+', add1, str3)
print(info)  #imooc videonum = 11



#split方法  -->根据匹配，分割字符串，返回分割字符串组成的列表
#re.split(pattern, string, maxsplit, flags)  #maxsplit是分割次数
import re
str4 = 'imooc:C C++ Java Python'
info = re.split(r':| ', str4)
print(info)  #['imooc', 'C', 'C++', 'Java', 'Python']

str4 = 'imooc:C C++ Java Python,C#'
info = re.split(r':| |,', str4)
print(info)  #['imooc', 'C', 'C++', 'Java', 'Python', 'C#']
