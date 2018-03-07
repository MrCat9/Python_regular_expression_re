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






























































