#匹配单个字符
.       匹配任意字符(除了\n)
[...]   匹配字符集
\d /\D  匹配数字/非数字
\s /\S  匹配空白/非空白字符
\w /\W  匹配单词字符[a-zA-Z0-9]/ 非单词字符



#.
import re
ma = re.match(r'a', 'abc')
print(ma.group())  #a
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'b', 'abc')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'.', 'abc')
print(ma.group())  #a
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'.', '123')
print(ma.group())  #1
print(type(ma))  #<class '_sre.SRE_Match'>

#如需匹配大括号内的任意字符，如：{a} ， 可以写
ma = re.match(r'{.}', '{a}')
print(ma.group())  #{a}
print(type(ma))   #<class '_sre.SRE_Match'>

ma = re.match(r'{.}', '{3}')
print(ma.group())  #{3}
print(type(ma))   #<class '_sre.SRE_Match'>

ma = re.match(r'{.}', '{aa}')  #一个.对应一个
print(type(ma))   #<class 'NoneType'>

ma = re.match(r'{.}', '{33}')  #一个.对应一个
print(type(ma))    #<class 'NoneType'>

ma = re.match(r'{...}', '{233}')
print(ma.group())  #{233}
print(type(ma))   #<class '_sre.SRE_Match'>



#[...]
#如需匹配大括号内的a-z字符集{[a-z]}，如：{[a]} ， 可以写
import re
ma = re.match(r'{[abc]}', '{a}')
print(ma.group())  #{a}
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'{[abc]}', '{c}')
print(ma.group())  #{c}
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'{[abc]}', '{d}')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'{[abc]}', '{ad}')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'{[abc]}', '{ac}')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'{[abc]}', '{bc}')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'[abc]', 'ac')
print(ma.group())  #a
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[abc]', 'ad')
print(ma.group())  #a
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[abc]', 'bc')
print(ma.group())  #b
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[abc]', 'da')
print(type(ma))  #<class 'NoneType'>

#[a-z]
ma = re.match(r'{[abc]}', '{d}')
print(type(ma))  #<class 'NoneType'> 

ma = re.match(r'{[a-z]}', '{d}')
print(ma.group())  #{d}
print(type(ma))  #<class '_sre.SRE_Match'>

#[A-Z]
ma = re.match(r'{[a-z]}', '{A}')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'{[a-zA-Z]}', '{A}')
print(ma.group())  #{A}
print(type(ma))  #<class '_sre.SRE_Match'>

#0-9
ma = re.match(r'{[a-z]}', '{1}')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'{[a-zA-Z0-9]}', '{1}')
print(ma.group())  #{1}
print(type(ma))  #<class '_sre.SRE_Match'>



#\w /\W
import re
ma = re.match(r'{\w}', '{1}')
print(ma.group())  #{1}
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'{\w}', '{12}')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'{\w}', '{ }')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'{\W}', '{ }')
print(ma.group())  #{ }
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'{\W}', '{  }')  #两个空格
print(type(ma))  #<class 'NoneType'>

#如需匹配中括号中加一个单词字符，需要注意转义
ma = re.match(r'[\w]', '[a]')  #错误
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'[[\w]]', '[a]')  #错误
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'\[[\w]\]', '[a]')  #正确
print(ma.group())  #[a]
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'\[[\w]\]', '[0]')  #正确
print(ma.group())  #[0]
print(type(ma))  #<class '_sre.SRE_Match'>



#匹配多个字符
*           匹配前一个字符0次或者无限次
+           匹配前一个字符1次或者无限次
?           匹配前一个字符0次或者1次
{m} /{m,n}  匹配前一个字符m次或者n次
*? /+? /??  匹配模式变为非贪婪(尽可能少匹配字符)



#*
#如需匹配以大写字母开头，后面是小写字母或者没有
import re
ma = re.match(r'[A-Z][a-z]', 'Az')
print(ma.group())  #Az
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[A-Z][a-z]', 'A')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'[A-Z][a-z]*', 'A')
print(ma.group())  #A
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[A-Z][a-z]*', 'Asdf')
print(ma.group())  #Asdf
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[A-Z][a-z]*', 'Asd123')
print(ma.group())  #Asdf
print(type(ma))  #<class '_sre.SRE_Match'>



#+
a = 1
_b = 2
# c = 3  #报错
#1d = 4  #报错
#'e = 5  #报错
#如匹配一个python的变量名（以下划线或者字母开头）
import re
ma = re.match(r'[_a-zA-Z]+[_\w]*', '10')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'[_a-zA-Z]+[_\w]*', '[as')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'[_a-zA-Z]+[_\w]*', '_10')
print(ma.group())  #_10
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[_a-zA-Z]+[_\w]*', 'asf')
print(ma.group())  #asf
print(type(ma))  #<class '_sre.SRE_Match'>



#？
#匹配0-99的数字
import re
ma = re.match(r'[1-9]?[0-9]', '99')
print(ma.group())  #99
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[1-9]?[0-9]', '10')
print(ma.group())  #10
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[1-9]?[0-9]', '1')
print(ma.group())  #1
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[1-9]?[0-9]', '0')
print(ma.group())  #0
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[1-9]?[0-9]', '01')
print(ma.group())  #0
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[1-9]?[0-9][0-9]', '01')
print(ma.group())  #01
print(type(ma))  #<class '_sre.SRE_Match'>



#{m} /{m,n}
#匹配6个字符
import re
ma = re.match(r'[a-zA-Z0-9]{6}', 'abc123')
print(ma.group())  #abc123
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[a-zA-Z0-9]{6}', 'abc1234')
print(ma.group())  #abc123
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[a-zA-Z0-9]{6}', 'abc12')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'[a-zA-Z0-9]{6}', 'abc12_')
print(type(ma))  #<class 'NoneType'>

#匹配163邮箱
import re
ma = re.match(r'[a-zA-Z0-9]{6}@163[.]com', 'abc123@163.com')  #.放在[]里面是只能匹配点，放在外边变成了匹配任意字符串
print(ma.group())  #abc123@163.com
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[a-zA-Z0-9]{6,10}@163[.]com', 'abc123@163.com')  #{6,10}
print(ma.group())  #abc123@163.com
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[a-zA-Z0-9]{6,10}@163[.]com', 'abcde1235@163.com')
print(ma.group())  #abcde1235@163.com
print(type(ma))  #<class '_sre.SRE_Match'>



#*? /+? /??
import re
ma = re.match(r'[0-9][a-z]*', '1bc')
print(ma.group())  #1bc
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[0-9][a-z]*?', '1bc')
print(ma.group())  #1  -->因为*最少是匹配0次
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[0-9][a-z]+', '1bc')
print(ma.group())  #1bc
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[0-9][a-z]+?', '1bc')
print(ma.group())  #1b
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[0-9][a-z]?', '1bc')
print(ma.group())  #1b
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[0-9][a-z]??', '1bc')
print(ma.group())  #1
print(type(ma))  #<class '_sre.SRE_Match'>

#非贪婪模式只截取第一次满足匹配的字符串，一旦满足就不在匹配。
#比如匹配以a开头以b结尾的字符串。非贪婪模式当匹配到第一b字符时就会停止匹配，
#贪婪模式只要你符合要求就会匹配，在这里会匹配所有的字符串。
ma = re.match(r'a.*?b', 'aaabcb')
print(ma.group())  #aaab
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'a.*b', 'aaabcb')
print(ma.group())  #aaabcb
print(type(ma))  #<class '_sre.SRE_Match'>



#边界匹配  指定字符串匹配的开头和结尾
^         匹配字符串开头
$         匹配字符串结尾
\A / \Z   指定的字符串匹必须出现在开头/结尾



#^和$
#匹配163邮箱
import re
ma = re.match(r'[\w]{6,10}@163[.]com', 'abcd1235@163.com')
print(ma.group())  #abcd1235@163.com
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[\w]{6,10}@163[.]com', 'abcd1235@163.comasd')
print(ma.group())  #abcd1235@163.com
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'[\w]{6,10}@163[.]com$', 'abcd1235@163.comasd')
print(type(ma))  #<<class 'NoneType'>

ma = re.match(r'^[\w]{6,10}@163[.]com$', 'abcd1235@163.comasd')
print(type(ma))  #<<class 'NoneType'>

ma = re.match(r'^[\w]{6,10}@163[.]com$', 'abcd1235@163.com')
print(ma.group())  #abcd1235@163.com
print(type(ma))  #<class '_sre.SRE_Match'>



#\A / \Z
#匹配imooc开头
import re
ma = re.match(r'\Aimooc[\w]*', 'imooc')
print(ma.group())  #imooc
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'\Aimooc[\w]*', 'imoocpython')
print(ma.group())  #imoocpython
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'\Aimooc[\w]*', 'imooc python')
print(ma.group())  #imooc
print(type(ma))  #<class '_sre.SRE_Match'>

ma = re.match(r'\Aimooc[\w]*', 'iimoocpython')
print(type(ma))  #<class 'NoneType'>

ma = re.match(r'\Aimooc[\w]*', 'imoopython')
print(type(ma))  #<class 'NoneType'>



#分组匹配
|           匹配左右任意一个表达式
(ab)        括号中表达式作为一个分组
\<number>   引用编号为num的分组匹配到的字符串
(?P<name>)  分组起一个别名
(?P=name)   引用别名为name的分组匹配字符串



#|
#






































