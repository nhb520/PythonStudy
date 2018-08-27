# 面向对象基础语法
# 一、dir内置函数（知道）
#     使用内置函数dir传入标识符/数据，可以查看对象内的所有属性及方法
#     常用的内置方法/属性
#     1 __new__ 方法 创建对象时，会被自动调用
#     2 __init__ 方法 对象被初始化时，会被自动调用
#     3 __del__ 方法 对象被从内存中销毁前，会被自动调用
#     4 __str__ 方法 返回对象的描述信息，print函数输出使用


# 二、定义简单的类（只包含方法）
#   面向对象是更大的封装，在一个类中封装多个方法，这样通过多个类创建出来的对象，就可以直接调用这些方法了
#   2.1定义只包含方法的类
#   class 类名：
#       def 方法1（self,参数列表）:
#           pass
#       def 方法2（self,参数列表）：
#           pass
#   第一个参数必须是self

#   2.2创建对象
#   当一个类定义完成之后，要使用这个类来创建对象，语法如下：
#       对象变量 = 类名（）
#   在面向对象的开发中，引用的概念是同样适用的

# 三、方法中的self属性
#   3.1给对象增加属性
#       1、使用  .属性名   利用赋值语句就可以了，不推荐使用
#   3.2self
#       哪一个对象调用的方法，self就是哪一个对象的引用
#       在类封装的方法内部，self就表示当前调用方法的对象自己
#       在方法内部：可以通过self. 访问对象的属性，也可以通过self. 调用其它的对象方法

# 四、初始化方法
#   4.1当使用类名（）创建对象时，会自动执行以下操作：
#       1.为对象在内存中分配空间--创建对象
#       2.为对象的属性设置初始值--初始化方法（init）
#   4.2初始化方法就是__init__方法
#   __init__方法是专门用来定义一个类具有哪些属性的方法
#   4.3在初始化方法内部定义属性
#       在__init__方法内部使用 self.属性名 = 属性的初始值 就可以定义属性
#       定义属性之后，再使用类创建的对象，都会拥有该属性
#   4.4改造初始化方法--初始化的同时设置初始值
#       在开发中，如果希望在创建对象的同时，就设置对象的属性，可以对__init__方法进行改造
#       1.把希望设置的属性值，定义成__init__方法的参数
#       2.在方法内部使用 self.属性 = 形参 接收外部传递的参数
#       3.在创建对象时，使用 类名（属性1，属性2...）调用
#   __str__方法
#       1.在python中，使用print输出对象变量，默认情况下，会输出这个变量引用的对象
#         是由哪一个类创建的对象，以及在内存中的地址（十六进制表示）
#       2.如果在开发中，希望使用print输出对象变量时，能够打印自定义的内容，就可以使用__str__方法
#         注意：__str__方法必须返回一个字符串

# 五、面向对象封装案例
#   5.1封装
#       1 面向对象编程的第一步--将属性和方法封装到一个抽象的类中
#       2 外界使用类创建对象，然后让对象调用方法
#       3 对象方法的细节都被封装在类的内部
class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s 的体重是 %.2f 公斤" % (self.name,self.weight)

    def run(self):
        print("%s爱跑步，跑步锻炼身体。" % self.name)

        self.weight -= 0.5

    def eat(self):
        print("%s是个吃货，吃完这顿再减肥。" % self.name)

        self.weight += 1

xiaoming = Person("小明",75.0)
xiaomei = Person("小美",45.0)

xiaoming.run()
xiaoming.eat()

xiaomei.run()
xiaomei.eat()

print(xiaoming)
print(xiaomei)
# 在对象的方法内部，是可以直接访问对象的属性的
# 同一个类创建的多个对象之间，属性互不干扰

class House:

    def __init__(self,house_type,area,):
        self.house_type = house_type
        self.area = area

        self.free_area = area
        self.item_list = []

    def __str__(self):

        return ("户型：%s\n总面积：%d平米\n剩余面积：%s平米\n家具：%s"
                % (self.house_type,self.area,
                   self.free_area,self.item_list))

    def add_item(self,item):

        if item.area > self.free_area:
            print("%s的面积太大了，无法添加" % item.name)
            return

        self.item_list.append(item.name)

        self.free_area -= item.area


class Houseitem:

    def __init__(self,name,area):

        self.name = name
        self.area = area

    def __str__(self):
        return "家具名称是%s，占地%d平米" % (self.name,self.area)


fangzi = House("豪宅",10000)
bed = Houseitem("席梦思",4)
chest = Houseitem("衣柜",2)
table = Houseitem("餐桌",1.5)

fangzi.add_item(bed)
fangzi.add_item(chest)
fangzi.add_item(table)

print(fangzi)