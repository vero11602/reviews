data=[]
count = 0
with open ('reviews.txt' , 'r') as f:
	for line in f :
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print (len(data))
print ("整筆資料總數為" , len(data) , "筆")



