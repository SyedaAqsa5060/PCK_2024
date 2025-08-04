# import pandas as pd
# s=[10,20,30,40]
# x=pd.Series(s,index=['a','b','c','d'])
# print(x)
# print(x['c'])
# x['c']=25
# print(x)
# import pandas as pd 
# fruit=('apple','bannana','mango','grapes','orange')
# price=(20,30,40,50,60)
# s=pd.Series(price,index=fruit)
# print(s)
# print(s['mango'])
# s['pineapple']=90
# print(s)
# s['apple']=120
# print(s)
import pandas as pd
shan={'aqsa':[23,45,56],
      'qudsia':[67,54,89],
      'arooj':[90,23,78]}
s=pd.Series(shan)
print(s)
print(s.iloc[[0,1]])
print(s[0][2])
print(s.loc[['aqsa','arooj']])
print(s.loc[:])
