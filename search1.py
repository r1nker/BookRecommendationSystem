import pymysql
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='123456',
                       db='Book',
                       charset='utf8mb4')
# 创建游标
cursor = conn.cursor()
# 执行查询
cursor.execute("SELECT count(*) FROM bookrating")

# 获取所有记录列表
results = cursor.fetchall()

# 打印结果
for row in results:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()