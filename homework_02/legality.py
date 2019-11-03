

#判断身份证是否合法

# 1)判断是否为18位身份证（不考虑15位）
import math
# 规定给定的省份证号码数据为文本型或数值型
def legality_1(ID_number):
    '''
    try:    # ID_number可能抛出不为字符串的异常即ID为整数
        if len(ID_number) != 18:
            print(f"{ID_number}：非18位身份证号码")
            raise NameError('非18位身份证号码')
    except TypeError:
        if int(math.log10(ID_number))+1 != 18:
            print(f"{ID_number}: 非18位身份证号码")
            raise NameError('非18位身份证号码')
    '''
    ID_number = str(ID_number)
    if len(ID_number) != 18:
        print(f"{ID_number}：非18位身份证号码")
        raise NameError('非18位身份证号码')
# 2)判断是否为合法的18位身份证
def legality_2(verification_code,tail_code,ID_number):
    if verification_code == tail_code:
        print(f"{ID_number}:合法身份证")
    else:
        print(f"{ID_number}:违法身份证")
        raise NameError('违法身份证')

# 新想法：地址码若不存在相应的地址，请求使用该功能者输入相应地址信息，保存以备后用
# 3)判断地址码是否存在对应城市地址信息

# 可改进：将提示语句print部分放入main的except中    

