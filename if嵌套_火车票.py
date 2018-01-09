ticket = 1
knifeLength = 48

if ticket==1:
	print("通过了检测")
	
	if knifeLength<=10:
		print("进入候车")
	else:
		print("刀太长")
else:
	print("先买票")
