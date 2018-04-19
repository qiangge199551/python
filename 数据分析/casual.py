import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import re


data = pd.read_csv('./lagoudata.csv', encoding='utf-8')
# print(data.head())
# print(data.tail())
# myfont = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\sinhei.ttf')
# mpl.rcParams['axes.unicode_minus'] = False
# plt.figure('学历要求')
# data['学历要求'].value_counts().plot(kind='barh', rot=0)
# plt.figure('工作经验')
# data['工作经验'].value_counts().plot(kind='bar', rot=0)
# plt.figure('详细地址')
# data['详细地址'].value_counts().plot(kind='pie', autopct='%1.2f%%')
print(pd.DataFrame(
	list(map(
		lambda x:(data['详细地址'][x], eval(re.split('k|k', data['薪资'][x])[0])*1000), range(len(data))
		))
	))
plt.show()
