# -*- coding: utf-8 -*-
'''
功能：从文件中读取数据，并写入数据库
适用：文件内容格式来源于同样的数据库表结构
例如：将从数据库A中通过查询语句 select * from tableName 得到的内容写入数据库B中同样的表结构中
起源：服务器端的数据库内容不允许通过mysqldump方式直接拷贝，只能同过查询的方式查看，但是又需要将数据拷到本地做测试
'''


import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb as mysql

config = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'user',#用户名
    'passwd' : 'pwd',#密码
    'db' : 'db',#数据库名称
    'charset' : 'utf8'
}

filepath = ‘’#文件路径
table = ‘’#数据表名称

###把数据写入mysql数据库中
try:
    conn = mysql.connect(**config)
    cur = conn.cursor()
    f = open(filepath, 'r')
    for eachline in f:
        rawdata = eachline.strip('\r\n').split('\t')
        data = ''
        for rd in rawdata:
            if str(rd) == 'NULL':
                data = data + 'null' + ','
            else:
                data = data + "'" + str(rd) + "',"
        sql = 'INSERT INTO ' + table + ' values (' + data[: -1] + ')'
        print sql
        cur.execute(sql)
    f.close()
    conn.commit()
    cur.close()
    conn.close()
except mysql.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
