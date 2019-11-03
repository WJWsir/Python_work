from perID_analysis import perID_analysis as per_ana
import re

# 快速查询单个ID_number的信息
#'''
while True:
    ID_number = input('q to quit!  请输入ID_number:')
    if ID_number == 'q':
        break
    per_ana(ID_number)
#'''

# 批量查询处理ID_number的信息

# 法一
# 要求如Test_data中的数据形式
'''
file = open("./Test_data.txt")
lines = file.readlines()
file.close

pattern = '\d{18}'
for line in lines:
    ID_number_line = re.findall(pattern,line)
    per_ana(ID_number_line[0])
'''
# 法二
# 不要求Test_data中的数据形式，但是要求是18位连续身份证
'''
file = open("./Test_data.txt")
data = file.read()
file.close

pattern = '\d{18}'
ID_number_grouplist = re.findall(pattern,data)
for i in range(0,len(ID_number_grouplist)):
    per_ana(ID_number_grouplist[i])
'''
