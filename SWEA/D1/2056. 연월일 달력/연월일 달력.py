t = int(input())
for i in range(1,t+1):
	li = str(input())
	a,b,c = li[0:4], li[4:6],li[6:]

	if b in ["01","03","05","07","08","10","12"]:
		print(f"#{i} {a}/{b}/{c}")
	elif b =="02":
		if c in ["29","30","31"]:
			print(f"#{i} -1")
		else:
			print(f"#{i} {a}/{b}/{c}")
	elif b in ["04","06","09","11"]:
		if c =="31":
			print(f"#{i} -1")
		else:
			print(f"#{i} {a}/{b}/{c}")
	else:
		print(f"#{i} -1")