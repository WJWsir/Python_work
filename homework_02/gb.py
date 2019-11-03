# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("http://www.mca.gov.cn/article/sj/tjyb/qgsj/2019/201909291543.html").read().decode('utf-8')

res1 = re.findall("<td class=xl7026399>(\d{2}0000)</td>\s.*?<td class=xl7026399>([\u4e00-\u9fa5]+)</td>",html, flags=re.DOTALL)
gb_sheng = dict(res1)

res2 = re.findall("<td class=xl7026399>(\d{4}00)</td>.*?<td class=xl7026399><span.*?</span>(\w+)</td>",html, flags=re.DOTALL)
gb_shi = dict(res2)

res3 = re.findall("<td class=xl7126399>(\d+)</td>.*?<td class=xl7126399><span.*?</span>(\w+)</td>",html, flags=re.DOTALL)
gb_qu = dict(res3)
