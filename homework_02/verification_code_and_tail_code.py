
# 规定给定的省份证号码数据为文本型或数值型

# 计算verification_code And tail_code
weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
# establish 映射 from 余数 to verification code
remainder = list(range(11))# 不可以[range(0,11)]
correspondence = ['1','0','X','9','8','7','6','5','4','3','2']# 规定映射后为字符
Mapping = dict(zip(remainder,correspondence))

#print(Mapping)
#print(Mapping[7]) #打印字符串没有‘’

def verification_tail_code(ID_number):
    ID_number = str(ID_number)
    ID_number = list(ID_number) # split 字符串 等价 字符串转列表
    
# -- step one --
    #front_17 = [ID_number[i] for i in range(17)] 利用切片
    front_17 = ID_number[0:17]
    
    # calculae the verification code
    list_ = [int(a)*int(b) for a,b in zip(front_17,weight)]
    list_ = sum(list_)
    value_remainder = list_ % 11
    
    # 得verification code
    verification_code = Mapping[value_remainder]
# -- step two --
    # 得tail_code
    behind_1 = ID_number[17]
    tail_code = behind_1
    
    return verification_code,tail_code
