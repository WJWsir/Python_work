import legality as le
import verification_code_and_tail_code as v_t
import analysis as ana

def perID_analysis(ID_number):
    # 设计思想：
    # 为实现模块间的连接：使用抛出异常捕捉异常处理异常的异常处理机制
    # ID_number = 430421200008180019#235407195106112745
    try: # 流程控制
        le.legality_1(ID_number) #是否18的合法检验
        
        (verification_code,tail_code) = v_t.verification_tail_code(ID_number)
        
        le.legality_2(verification_code,tail_code,ID_number) #是否符合规范的合法检验
    except NameError:
        pass
    else:# 均合法继而实现解析功能
        print(f"基本信息：")
        
        (address_code,birth_code,sequence_code) = ana.divide_ID(ID_number)

        address = ana.Mapping_address(address_code)
        print(f"出生地址：{address}")
        
        birth_date = ana.Mapping_birth(birth_code)
        print(f"出生日期：{birth_date}")
        
        sex = ana.Mapping_sex(sequence_code)
        print(f"性别属性：{sex}")
