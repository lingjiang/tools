# tools
工具性质的小程序
***
#ReadDataFromFileAndWriteToDB.py

* 功能：从文件中读取数据，并写入数据库
* 适用：文件内容格式来源于同样的数据库表结构
* 例如：将从数据库A中通过查询语句 select * from tableName 得到的内容写入数据库B中同样的表结构中
* 起源：服务器端的数据库内容不允许通过mysqldump方式直接拷贝，只能同过查询的方式查看，但是又需要将数据拷到本地做测试
