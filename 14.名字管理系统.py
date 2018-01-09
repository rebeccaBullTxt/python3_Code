#1.打印功能提示
print("="*50)
print("    名字关系系统 v8.6")
print("1.添加一个新名字")
print("2.删除一个名字")
print("3.修改一个名字")
print("4.查询一个名字")
print("5.显示所有的名片")
print("6.退出系统")
print("="*50)

names = []#定义空列表存储添加名字
card_infors = []

while True:

#2.获取用的选择
	numStr = (input("请输入功能序号"))
	if numStr.isdigit():
		num = numStr
	else:
        	num = 6

#3.根据用户选择,执行相应功能
	if num==1:
		new_name = input("请输入名字")
		new_qq = input("输入新的QQ:")
		new_weixin = input("输入新微信:")
		new_addr = input("输入新住址")

		#定义字典存储新的名片
		new_infor = {}
		new_infor['name'] = new_name
		new_infor['qq'] = new_qq
		new_infor['weixin'] = new_weixin
		new_infor['addr'] = new_addr

		card_infors.append(new_infor)
		print(card_infors)
		
		#names.append(new_name)
		#print(names)	
	elif num==2:
		pass
	elif num==3:
		pass
	elif num==4:
		find_name = input("输入要查询的名字")
		
		find_flag = 0#默认没有找到

		
		for temp in card_infors:
			if find_name == temp["name"]:
				print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
		find_flag=1#找到
		break

		#if find_name in names:
			#print("找到了你要的人")
		#else:
		if find_flag == 0:
			print("查无此人")
	elif num==5:
		print("姓名\tQQ\t微信\t住址")
		for temp in card_infors:
			print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
	elif num==6:
		break;
	else:
		print("您输入的数据有误,重新输入")

	print("")
