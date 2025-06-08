dic = { '000':'0', '001':'1',  '010':'2', '011':'3', '100':'4', '101':'5', '110':'6', '111':'7'}
inputNum = input()
num1 = format(int(inputNum),',').split(',')
num2 = [dic[i.zfill(3)] for i in num1 if i.zfill(3) in dic]
print (int("".join(num2)))