import matplotlib.pyplot as plt
import numpy as np
import pymysql

db = pymysql.connect(host='39.105.59.8', port=3306, user='root', passwd='713f7c236067773e', db='mfshop', charset='utf8')
cursor = db.cursor()
sql = """select goods_name, count(*) as count from mf_order_goods GROUP BY goods_id order by count desc limit 5"""
names = []
counts = []
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      names.append(row[0][:20])
      counts.append(row[1])
      # 打印结果
      print("fname=%s, lname=%s" % \
             (row[0], row[1]))
except:
   print("Error: unable to fecth data")
print(db.get_server_info())
# 关闭数据库连接
db.close()

names = np.array(names)
counts = np.array(counts)

explode = [0, 0.1, 0, 0, 0]

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.axes(aspect=1)
plt.pie(x=counts, labels=names, explode=explode, autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)

plt.show()