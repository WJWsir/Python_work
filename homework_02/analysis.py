import gb

# divide the ID_number into three parts
def divide_ID(ID_number):
    ID_number = str(ID_number)
    ID_number = list(ID_number)
    front_6 = ID_number[0:6]
    middle_8 = ID_number[6:14]
    behind_3 = ID_number[14:17]
    # [a 第一个数的偏移量，b第二个数的实际序数]其中b - a = size of sequence

    address_code = front_6
    birth_code = middle_8
    sequence_code = behind_3
    
    return address_code,birth_code,sequence_code


# establish Mapping from 地址码[6] to 具体地址
def Mapping_address(address_code):
    address_code = ''.join(address_code)
    try:
        address1 = address_code[0:2]+'0000'
        address1 = gb.gb_sheng[address1]
        print(address1)
        try:
            address2 = address_code[0:4]+'00'
            address2 = gb.gb_shi[address2]
        except:
            address2 = ''
        address3 = gb.gb_qu[address_code]
        address = address1+' '+address2+' '+address3
        return address
    except:
        print('该地址码没有对应的地址')
        return None
    







# establish Mapping from 出生日期码[8] to 出生日期
def Mapping_birth(birth_code):
    birth_code = ''.join(birth_code)
    birth_date = birth_code[0:4] + '年' + birth_code[4:6] +'月' + birth_code[6:8] + '日'

    return birth_date # 字符串


# establish Mapping from 顺序码[3] to 性别
def Mapping_sex(sequence_code):
    Judge_code = int(sequence_code[2]) % 2
    if Judge_code == 0:
        sex = '女'
    else:
        sex = '男'
    return sex
    
