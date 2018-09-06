#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import cards_tools

#无限循环，由用户主动决定什么时候推出!
while True:

    # 显示功能菜单
    cards_tools.shou_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" %action_str)

    #1,2,3针对名片的操作
    if action_str in ["1","2","3"]:

        #新增名片
        if action_str == "1":
            cards_tools.new_card()


        #显示全部
        elif action_str == "2":
            cards_tools.shou_all()


        #查询名片
        elif action_str == "3":
            cards_tools.search_card()



    #0退出系统
    elif action_str == "0":
        print("欢迎继续使用【名片管理系统】！")

        break

    #其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请您重新输入！")