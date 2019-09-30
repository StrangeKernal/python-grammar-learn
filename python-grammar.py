# -*- coding: utf-8 -*-

# 1. 第一个程序
# print('hello python!')

# 2. 输出字符串
#    遇到逗号且无转义字符时会输出一个空格
# print('The quik brown fox', 'jumps over', 'the lazy dog')

# 3. 输出数字或计算结果
# print(100+300)
# print('100 + 300', '=', 100+300)

# 4. 输入
#    仅在python命令行环境下直接写变量名可以输出变量值
# name = input()
# print(name)
# name

# 5. 结合test_1到test_4编写hello.py
# print("请输入您的名字：")
# name = input()
# print('hello', name)

# 6. 转义字符
#    python中字符串需要使用‘’或“”括起来，如果需要同时输出‘与“这两个符号本身时，使用转义字符\进行标示，同时转义字符\也可以用\\进行输出
# print('I\'m OK!')
# print('I\'m \"OK\"!')
# print('I\'m \"OK\"! \\')
# print('I\'m \tlearning Python \nnow')

# 7. 默认不转义
#    在字符串开头‘前增加r字母，可以使该部分字符串默认不转义，但是仅对该一串字符串有效
# print(r'\\\\\\\\\\\n\t', 'flame\nhot')

# 8. 换行符\n的另一种写法
#    可以写成'''...'''的方式，其中...为需要换行的输出信息
# print('''line1
# line2
# line3''')
#    多行字符串还可以增加r     
# print(r'''lin1\n
# lin2
# lin3''')

# 9. 字符串与编码
#    最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
# print('包含汉字的str')

# 10. 字符与编码的转换
#     ord()函数可以将字符转换为Unicode编码，chr()函数可以使Unicode编码转换为字符
# print(ord('A'))
# print(chr(66), chr(25912))

# 11. bytes类型数据
#     Python的字符串类型为str，在内存中使用Unicode表示，以这种编码方式存储的话，1个字符对应若干个字节(Byte)，对存储与传输不利
#     因此，如果要在网络上传输，或者保存到磁盘上，需要将str数据转换为bytes数据
#     bytes数据与str数据的区别在于，bytes数据中每个字符只占用 1 字节
#     Python对于bytes数据用带b前缀的‘’或“”表示
#     str转换bytes使用encode()函数； bytes转换str使用decode()函数
# print('ABCD'.encode('ascii'))
# print('中文'.encode('utf-8'))
# print(b'ABCD'.decode('utf-8'))

# 12. len()函数
#     len()对str数据计算字符串的字符数，对bytes数据计算字节数
#     1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
# print(len('ABCDEFG'))
# print(len(b'ABC'))
# print(len('中文'.encode('utf-8')))

# 13. 格式化
#     Python中格式化方式与C语言一致，同样使用%进行实现
#     你可能猜到了，%运算符就是用来格式化字符串的。
#     在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
#     常用的占位符：%s字符串    %d整数    %f浮点数    %x十六进制数
#     当字符串中需要使用%符号本身时，需要对%进行转义：%%
# print('嘿%s,你的分数是%d' % ('张三', 87))
# print('中国人口占世界人口比例：%d%%' % (30))

# 14. format格式化
#     format会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多，需要注意起始下标为0
#     使用format方式进行格式化，而非使用占位符%时，字符串中%不需要使用%%进行转义
#     目前理解：由于.的格式，format与encode应该都是类似于字符串对象本身自带的方法（或者称为函数）
# print('{0}的成绩提升了{1:.1f}%'.format('李四', 37.1))

# s1 = 72
# s2 = 85
# res = (s2 - s1)/s1*100
# print('{0:.1f}'.format(res))
# print('%.1f%%' % res)

# 15. 布尔值
#     Python是大小写敏感的语言，布尔值只有True和False
#     Python的逻辑运算使用英文单词：and or not
# para1 = 3>2
# para2 = 4>5
# print('para1:', para1)
# print('para2:', para2)
# print('para1 & para2:', para1 and para2)
# print('para1 | para2:', para1 or  para2)
# print('not para1:{0}, not para2:{1}'.format(not para1, not para2))

# 16. 空值
#     Python中空值并不是常见的NULL，而是None，注意开头N是大写
# para = None
# print(para)
# print('Type of para:', type(para))

# 17. 常量
#     Python中通常使用全大写的变量名表示常量
#     但是实际上全大写变量名依旧表示变量，Python没有机制保证真常量，但这种写法可以提示代码阅读人员这是一个常量
# PI = 3.1415926

# 18. 列表：list
#     list是Python内置的一种数据结构，表示的是有序集合，随时可以对list中数据进行CRUD操作
#     list的表示方式为[]
# classmate = ['张三', '李四', '赵五']
# print('classmate:', classmate)
#     当操作对象是list时，len函数返回的是list内元素的数量
# print('list的长度为:', len(classmate))
#     list元素访问的方法：使用索引，这里索引与C语言中下标index的意义一样，且同样是从0开始
# print('list中第1个元素为:', classmate[0])
#     list索引中有特殊的用法：可以使用-1作为索引，取出的是list中倒数第1个元素
#     依此类推，-2表示倒数第2个元素，-3表示倒数第3个元素，这种使用方法同样需要考虑边界问题(out of range)
# print('list中最后1个元素为:', classmate[-1])
#     list是一个可变的有序集合，所以可以追加元素进入list末尾，使用append方法
# classmate.append('郑老师')
# print('classmate:', classmate)
#     list也支持指定位置插入元素，使用insert方法,insert($NUM,DATA)表示将 DATA 插入到第 $SUM 的位置
# classmate.insert(1,'郑弟弟')
# print('classmate:', classmate)
#     list删除方法，使用pop方法弹出末尾元素
# classmate.pop()
# print('classmate:', classmate)
#     list的pop方法支持指定位置删除元素，方法是在()中填写弹出元素的下标index
# classmate.pop(0)
# print('classmate:', classmate)
#     list元素的修改(重新赋值)，直接使用index,注意是[]不是()，这是习惯问题，将list视为数组、vector之类的数据结构就容易接受
# classmate[0]='修改后的郑弟弟'
# print('classmate:', classmate)
#     list内元素类型可以不一致，1个list中可以同时包含多种不同数据类型的元素，也可以包含list
# lis = ['python', 'java', ['c', 'c++', 'c#'], 12306, True]
# print(lis)
#     list中的list，可以视为多维数组，增加index维数进行取值
# print(lis[2][0], lis[2][1], lis[2][2])
#     list中不含任意元素时，称为空list，长度为0
# lis_none = []
# print('lis_none:', lis_none)
# print('空list的长度:', len(lis_none))

# 19. 元组：tuple
#     元组tuple也是Python内置的一种数据结构。tuple与list不同在于，tuple一旦经过初始化，后续无法进行修改。
#     因为元组不可变，所以对于程序设计来说虽然不方便修改，但更为安全，能使用tuple的情况下，尽量使用tuple替换list
# classmate = ('郑弟弟', '郑老师', 'zmt')
# print(classmate, '\n', classmate[0], '\n', classmate[-1])
#     tuple存在的陷阱：tuple初始化时如果只有一个元素，由于()既可以表示tuple，又可以表示数学公式中的小括号
#     这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算。因此一个元素时不是tuple
# tp = (1)
# print('Type of tp:', type(tp))
#     如果试图消除这种歧义，定义1个元素的tuple时，需要增加“，”进行区别处理
# tp = (1,)
# print('Type of tp:', type(tp))
#     tuple本身是不可变的，但当tuple中元素为list时，这个list元素可以变化，这是由于tuple保证指向的list元素未变，并不保证list中存储的元素不变
#     可以理解为指针本身并未发生变化，即并未指向其他元素，但指针指向的list，其中包含的list元素指针发生了变化
# tp = (1, 2, ['a', 'b'])
# tp[2][0] = 'c'
# print(tp)

# 20. 条件判断
#     Python与C一样采用if进行条件判断，需要注意的是格式发生了变化
#     Python中，if后的条件不需要使用()，同时条件完成后需要使用:表示条件结构开始
#     Python中，if语句的条件结构部分不需要使用{}，Python解释器通过4个空格或者缩进(需要设置)判断是否是条件结构
#     Python中，elseif变为elif，else并未发生变化，elif与else后都需要:
# age = 17
# if age > 18:
#     print('成年人')
# elif age > 12:
#     print('青少年')
# else:
#     print('儿童')
#     if还可以进行缩写，比如 if x 当x为非零数值、非空字符串、非空list等，就判断为True，否则为False
# x = 'abc'
# if x:
#     print('True')
# else:
#     print('False')

# 21. str转换int
#     Python提供int()方法实现str到int的转换，同时会检查int()方法的输入是否合法
# str_1 = '123'
# str_2 = 'abc'
# print(int(str_1))

# 22. 循环
#     Python的循环结构也分为2种：for in 与 while
# classmate = ['shy', 'zmt', 'ylt', 'zy', 'yhy']
# for index in classmate:
#     print('name:', index)
# num = len(classmate)
# while num > 0:
#     print('name:', classmate[num-1])
#     num = num - 1
#     Python同样提供了break与continue两种循环中常用的方法

# n = 1
# while n > 0:
#     if n > 100:
#         break
#     print(n)
#     n = n + 1
# print('End')
    
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)

# 23. range方法
#     Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
# print(range(5))
# print(list(range(5)))

# 24. 字典：dict
#     字典dict是Python内置的一种数据结构，dict提供若干个 key-value 键值对的元素
#     字典dict的优势在于查找速度极快，字典的查找方式为 dic[key]，字典dict的key必须是不可变量，所以list不可以作为key
#     字典dict内部的存放顺序与key放入的顺序没有关系
#     字典dict与列表list的区别在于：dict占用内存大，查询速度快。list的查询与插入速度随元素数量增加而延长。因此dict是一种用空间换时间的数据结构
# dic = {'shy':100, 'zmt':99, 'ylt':88}
# print(dic['shy'])
#     当key不存在于dict结构中时，会报错，因此可以先使用in方法判断key是否存在于dict中
# print('zmt' in dic)
#     也可以通过get方法安全取元素，默认不存在时get返回None，也可以指定返回值，通过第二参数进行设置
# print(dic.get('kkk'))
# print(dic.get('sss', -1))
#     dict的删除使用pop(key)方法
# dic.pop('ylt')
# print(dic)
#     dict的增加方法为直接使用赋值：dic[key]=value
# dic = {'shy':100, 'zmt':99, 'ylt':88}
# dic['flame'] = 70
# print(dic)

# 25. 集合：set
#     set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#     要创建一个set，需要提供一个list作为输入集合
#     注意，传入的参数[1,2,3,4,5,6,7,8,9]是一个list，而显示的{1, 2, 3, 4, 5, 6, 7, 8, 9}只是告诉你这个set内部有1-9这9个元素
#     显示的顺序也不表示set是有序的
# s = set([1,2,3,4,5,6,7,8,9])
# print(s)
#     set存储的是key，key是唯一的，所以set中并不存在相同的元素,重复的元素会被过滤
# s = set([1,2,2,3,4,5,6,7,8,9])    
# print(s)
#     通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
#     add(key)只接受1个值传入，不能使用s.add(1,2)这种方式
# s = set([1,2,2,3,4,5,6,7,8,9]) 
# s.add(0)
# s.add(2)
# s.add('s')
# print(s)
#     set的删除方法不是pop(key)，而是remove(key)，这一点需要和dict，list，tuple 3种数据结构区分开
# s = set([1,2,2,3,4,5,6,7,8,9]) 
# s.remove(4)
# print(s)
#     set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
#     需要注意的是交集操作是 & 并集操作是 | ，并不是 and 和 or 这两种逻辑操作
# s1 = set([1,2,3,4,5])
# s2 = set([0,1,2,3,4])
# print('s1 & s2:', s1 & s2)
# print('s1 | s2:', s1 | s2)
#     set中元素全部为key，以list为key使用add(key)方法时会报错，提示list是unhashable type
#s = set([1,2,3])
#s.add([1,2,3,4])

# 26. 字符串的replace方法
#     str提供str.replace(old,new)方法，用new替换old，但是需要注意一些定义
#     如下所示，replace方法返回的是1个新的str对象，str对象是不可变型数据，所以s1指向的字符串‘abc’本身是不会发生变化的
#     所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
#     相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
# s1 = 'abc'
# s2 = s1.replace('a', 'A')
# print('s1:', s1, '\ns2:', s2)

# 27. 调用函数
#     Python调用函数的方式与其他语言一致，同样需要提供函数名与参数值
# a = -192
# b = abs(a)
# print('a:{0},b:{1}'.format(a, b))
# c = 10
# print('max of [a,b,c]:', max(a,b,c))

# 28. 数据类型转换
#     Python常用的数据类型转换方法：
#     int(),float(),hex(),str(),bool(),list()……
# a = 128
# hex_a = hex(a)
# print('a:{0},hex of a:{1}'.format(a, hex_a))

# 29. 定义函数
#     Python定义函数的方法为 def $FUN_NAME($PARAS):
# def my_max(x,y):
#     if x > y:
#         return x
#     else:
#         return y
# a = 2
# b = 5
# print('max of [a,b]:', my_max(a,b))

# 30. 空函数
#     Python提供pass语句定义一个无任何操作的空函数
#     实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
#     pass也可以使用在if条件结构以及for in甚至while循环条件中
# def none_fun(para):
#     pass

# 31. 数据类型检查
#     Python内置isinstance()方法检查对象的数据类型
# def my_max(para_1, para_2):
  #   if not (isinstance(para_1, (int, float)) and isinstance(para_2, (int, float))):
    #     # print('输入的参数并非为整型数或浮点数！')
    #     # return -1
    #     raise TypeError('输入参数类型错误！')
    # else:
    #     if para_1 > para_2:
    #         return para_1
    #     else:
    #         return para_2
# a = 'A'
# b = 10
# print(my_max(a,b))

# 32. 函数返回多个值
#     Python支持函数返回多个result，其实现方法是返回一个tuple
# def mov(x, y, ax, ay):
#     x = x + ax
#     y = y + ay
#     return x, y
# x = 1
# y = 2
# a = -1
# b = 3
# res = mov(x,y,a,b)
# print('res:{0}, Type of res:{1}'.format(res, type(res)))

# 33. 函数的默认参数
#     Python支持函数的参数具有缺省值，其具体实现为 def $FUN($PARA = $DEFAULT):
# def my_pow(x, num=2):
#     tmp = x
#     while num > 1:
#         num = num - 1
#         x = x * tmp
#    return x
# print(my_pow(2))
#     从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#     1) 必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#     2) 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#     默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
#     先定义一个函数，传入一个list，添加一个END再返回：
# def fun(L=[]):
#     L.append('End')
#     return L
# l = [1,2,3]
# print('l:{0}\nfun(l):{1}'.format(l, fun(l)))
#     正常传入非默认值时，函数运行正常，但如果使用默认值，即传入空字符串时会出现错误的逻辑
# print(fun())
# print(fun())
# print(fun())
#     Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
#     每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#     定义默认参数要牢记一点：默认参数必须指向不变对象！
#     要修改上面的例子，我们可以用None这个不变对象来实现：
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print(add_end())
# print(add_end())
# print(add_end())

# 33. 可变参数
#     在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
#     Python提供定义可变参数的方式是 def $FUN(*$PARA):
#     定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#     在函数内部，参数num接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
# def my_sum(*num):
#     sum = 0
#     for index in num:
#         sum = sum + index
#     return sum
# print('sum of [1,2,3,4,5]:', my_sum(1,2,3,4,5))
#     Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
# def my_sum(*num):
#     sum = 0
#      for index in num:
#          sum = sum + index
#     return sum
# lis = [1,2,3,4,5]
# print('sum of [1,2,3,4,5]:', my_sum(*lis))

# 34. 关键字参数
#     可变参数允许传入0或若干个参数，这些可变参数会在函数调用时自动组装成一个tuple对象。
#     关键字参数允许传入含0或若干个含参数名的参数，这些参数在函数调用时自动组装成一个dict对象。
#     关键字参数的形式为 **$PARA    即参数名之前有2个*号（可变参数是1个*号）
#     函数调用时，可以仅输入必选参数，忽略关键字参数
#     函数调用时，可以输入任意个关键字参数
#     关键字参数输入的格式为 key = value
# def person(name, age, **key_word):
#     print('name:{0}\nage:{1}\nothers:{2}'.format(name, age, key_word))
# person('zhengmt', '25')
# person('songhy', '24', gender='male', college='NUAA')    #gender与college均为关键字参数
#     与可变参数可以对list加*号变成*list作为可变参数输入这一方式相似，dict增加**也可以作为关键字参数进行参数传输
# def person(name, age, **key_word):
#     print('name:{0}\nage:{1}\nothers:{2}'.format(name, age, key_word))
# d = {'gender':'male', 'college':'NUAA'}
# person('songhy', 24, **d)

# 35. 命名关键字参数    
#     如果要限制关键字参数的输入，例如只想保留gender在key_word中，可以采用 def fun(必选参数, *, kw_1, kw_2): 此类格式实现
#     采用这一类方式时，特殊分隔符号*之后的为命名关键字参数
#     可以理解为命名关键字参数是带约束的关键字参数，要注意它和位置参数的区别
# def person(name, age, *, gender):
#     print('name:{0}\nage:{1}\nothers:{2}'.format(name, age, gender))
# d = {'gender':'male', 'college':'NUAA'}
# person('songhy', 24, gender='male')
#     如果参数中已经存在可变参数，可变参数前必有*号，因此后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
# person('songhy', 24, city='Shanghai', job='ICBC')
#     命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
# person('Jack', 24, 'Beijing', 'Engineer')
#     命名关键字参数可以有缺省值，从而简化调用：
# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job)
#     由于命名关键字参数city具有默认值，调用时，可不传入city参数：
# person('Jack', 24, job='Engineer')
#     使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
# def person(name, age, city, job):
     # 缺少 *，city和job被视为位置参数
#    pass

# 36. 参数组合
#     Pyhton函数参数有：必选参数、默认参数、可变参数、关键字参数与命名关键字参数5种类型。
#     Python函数定义时，参数定义的顺序必须按照：必选参数、默认参数、可变参数、命名关键字参数、关键字参数 的顺序进行定义
#     虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
# def f1(a, b, c=0, *args, **kw):
#     print('a={0},b={1},c={2},arg={3},kw={4}'.format(a, b, c, args, kw))
# def f2(a, b, c=0, *, d, **kw):
#     print('a={0},b={1},c={2},d={3},kw={4}'.format(a, b, c, d, kw))
# f1(1, 2)
# f1(1, 2, 3)
# f1(1, 2, c=3)
# f1(1, 2, 3, 'a', 'b')
# f1(1, 2, 3, 'a', 'b', x='kw1', y='kw2')
# f2(1, 2, d=99, ext=None)
# f2(1, 2, d='_name_kw', x='kw1', y='kw_2')

# 37. 递归函数
#     函数内部调用自身本身，就是递归函数
#     举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# num = [1,2,5,7,10]
# for index in num:
#    print('fact({0}):{1}'.format(index, fact(index)))
#     使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的。
#     每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# print(fact(1000))   # 此时报错 RecursionError: maximum recursion depth exceeded in comparison 是栈溢出的提示

# 38. 尾递归
#     尾递归用于解决递归函数的栈溢出问题，实际上，尾递归与循环的作用类似，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#     尾递归是指，在函数返回的时候，调用函数自身本身，且return语句不包含表达式，即没有 n * fact(n-1) 这种形式。
#     遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(n, m):
#     if n==1:
#         return m
#     else:
#         return fact_iter(n-1, m * n)
# print('fact(1000):', fact(1000))

# 39. 切片(Slice)操作
#     Python提供切片操作，用于解决取指定范围索引的操作
#     l[0:3]表示index从0开始取，直到3为止，但并不包含index=3的元素
# classmate = ['songhy', 'yinlt', 'zhengmt', 'zhaoy', 'yehy', 'jiac']
# slc_1 = classmate[0:3]      #不包含classmate[3]
# slc_2 = classmate[:4]       #不包含classmate[4]
# slc_3 = classmate[-3:-1]    #不包含classmate[-1]
# slc_4 = classmate[-4:]      #包含classmate[-1]
# print('slc_1:{0}\nslc_2:{1}\nslc_3:{2}\nslc_4:{3}'.format(slc_1,slc_2,slc_3,slc_4))
#     tuple也是一种list，不过是不可变的list，因此tuple也支持切片操作，切片处理后返回的仍然是tuple类型数据
# classmate = (1, 2, 3, 4, 5)
# cla_1 = classmate[0:2]
# cla_2 = classmate[:2]
# cla_3 = classmate[-3:-1]
# cla_4 = classmate[-3:]
# print('cla_1:{0}\ncla_2:{1}\ncla_3:{2}\ncla_4:{3}'.format(cla_1,cla_2,cla_3,cla_4))
#     字符串str同样也支持切片操作
# string = 'abcdefg'
# str_1 = string[0:2]
# str_2 = string[:3]
# str_3 = string[-3:-1]
# str_4 = string[-3:]
# print('str_1:{0}\nstr_2:{1}\nstr_3:{2}\nstr_4:{3}'.format(str_1,str_2,str_3,str_4))

# 40. 迭代
#     Python的迭代是通过for in结构实现的
#     Python中只要是可迭代对象(Iterable)，都可以使用for in进行迭代，dict由于存储顺序并非list的顺序，所以迭代结果可能不一致
#     Iterable可迭代对象的概念要注意，它表示一种类型，这种类型可以通过isinstance(xxx, Iterable)进行判断
#     Iterable类型包含在collections模块中
# from collections import Iterable
# print(isinstance('abcDFG', Iterable))   #字符串是Iterable
# print(isinstance([1,2,3], Iterable))    #list是Iterable
# print(isinstance(233, Iterable))        #整数并非Iterable
#     Python实现类似Java的下标循环：使用enumerate()方法
# lis = ['a', 'b', 'c', 'd']
# for index, value in enumerate(lis):
#     print(index, value)
#     Python中多变量循环是很常见的
# lis = [(1,2), (2,3), (3,4)]
# for x, y in lis:
#     print(x, y)
# lis = [[(1,2), (2,3)],(3,4),(4,5)]
# for x, y in lis:
#    print(x, y)

# 41. 列表生成式
#     Python提供列表生成式简化循环生成列表    
#     常见的循环生成list
# lis_1 = []
# for index in list(range(1,11)):
#     lis_1.append(pow(index, 2))
# print(lis_1)
#     写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
# lis_2 = [index * index for index in range(1, 11)]
# print(lis_2)
#     还可以使用2层循环生成全排列,注意2个变量之间要写符号+
# lis_3 = [x + y for x in 'abc' for y in '123']
# print(lis_3)
#     使用列表生成式能够简洁的列出指定文件目录下所有的文件
# import os
# _file_name = [index for index in os.listdir('/Users/soukouki/Desktop')]       #os.listdir()方法需要填入一个字符串表示搜寻的路径
# print(_file_name)
#     for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
# dic = {'a':'1', 'b':'2', 'c':'3'}
# lis = [key + '=' + value for key,value in dic.items()]
# print(lis)
# print(dic.items())

# 42. 生成器
#     受内存大小限制，list不可能无限增加，Python提供了一种一边循环一边计算的机制，称为generator
#     generator的生成方法一：将列表生成式的[]更换成()
# lis = [x * x for x in range(1,11)]
# gen = (x * x for x in range(1,11))
# print(lis)
# print(gen)
#     generator保存的是算法（元素计算规则），无法直接打印元素，若想要打印元素，需要使用next(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
#     genarator本身也是一种Iterable，因此可以使用for in的方式提取元素
# for index in gen:
#     print(index)
#     generator的生成方法二：函数定义中使用yield关键字
#     函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#     而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# def gfnc():
#     print("step1:")
#     yield 1
#     print("step2:")
#     yield 3
#     print("step3:")
#     yield 5

# gen = gfnc()
# for index in gen:
#     print(index)

# 43. 迭代器Iterator
#     迭代器不但可以接受for in循环，同时也可以被next()方法不断调用下一个值，因此生成器属于迭代器
# from collections import Iterator
# gen = (x * x for x in range(1,11))      
# print(isinstance(gen, Iterator))        # generator是Iterator
# lis = [x * x for x in range(1,11)]     
# print(isinstance(lis, Iterator))        # list不是Iterator
# string = 'aBcDeFG'
# print(isinstance(string, Iterator))     # str不是Iterator
#     迭代器同样有类型转换的方法iter()
# print(iter(lis))
# lis = iter(lis)
# print(next(lis))
# print(next(lis))
# print(next(lis))

# 44. 函数式编程
#     自我理解：面向函数编程Functional Programming，更接近于数学计算

# 45. 高阶函数
#     函数本身也可以赋值给变量，同时可以通过这个被赋值的变量调用函数
# a = abs(-1)
# b = abs
# c =b(-2)
# print(a, b, c)
#     函数可以接受另一个函数作为参数，这种函数就称为高阶函数
# def high_fun(x, y, f):
#     return f(x) + f(y)
# print(high_fun(-1, 12, abs))

# 46. map/reduce
#     map()接受2个参数,一个是函数，一个是Iterable，map会将Iterable中所有元素使用传入的函数进行处理
#     map()返回的是一个Iterator
# lis = list(range(1, 10))
# res = map(abs, lis)
# for index in res:
#    print(index)
#    对list直接使用str转换格式方法会出现出乎我们意料的结果，list中[]括号也会被转换为字符
# lis = [1,2,3,4,5]
# lis = str(lis)
# print(type(lis))
# print(lis[0])
#    如果使用map则方便很多
# lis = [1,2,3,4,5]
# res = list(map(str, lis))
# print(res)
#     reduce和map格式一样，需要接受2个参数，第一个参数是函数，第二个参数是Iterable
#     reduce会将当前计算结果与下一个元素做累积计算，即reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# def fun(x, y):
#     return x * 10 + y
# from functools import reduce
# res = reduce(fun, [1,2,3,4,5])
# print(res)

# from functools import reduce
# def char2int(string):
#     dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return dic[string]
# def sum(x, y):
#     return x*10 + y
# res = reduce(sum, map(char2int, '12306'))
# print(res)

# 47. lambda函数
#     lambda x:x+1可以认为lambda函数作为一个表达式，包含了一个匿名函数：
#     def g(x):
#       return x+1
#     即参数与函数体（包含返回）
# g = lambda x: x * x
# print(g(2))

# 48. filter
#     filter()同样接受一个函数，一个Iterable参数
#     filter会对Iterable逐个进行函数操作，同时判断返回结果是True或False，仅保留返回为True的元素
# def is_odd(n):
#     return n%2 == 1
# res = filter(is_odd, [1,2,3,4,5,6,7])
# print(list(res))
# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
