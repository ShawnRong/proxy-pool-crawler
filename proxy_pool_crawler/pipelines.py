# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class ProxyPoolCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

# 存储到mysql数据库
class ProxyPoolCrawler2mysql(object):
    # # 测试ip是否有效，有效再插入数据库
    
    # def test_alive(proxy):
    #     http_url = "http://www.baidu.com"
    #     proxy_url = "http://{0}".format(proxy)
    #     try:
    #         proxy_dict = {
    #             "http": proxy_url,
    #         }
    #         response = requests.get(http_url, proxies=proxy_dict, timeout=5)
    #     except Exception as e:
    #         # print("invalid ip and port")
    #         return False
    #     else:
    #         code = response.status_code
    #         if code >= 200 and code < 300:
    #             # print("effective ip")
    #             return True
    #         else:
    #             # print("invalid ip and port")
    #             return False


    def process_item(self, item, spider):
        address = item['address']
        
        connection = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',  # 自己的mysql用户名
            passwd='',  # 自己的密码
            db='proxypool',  # 数据库的名字
            charset='utf8mb4',  # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # 创建更新值的sql语句
                sql = """INSERT INTO proxy(address)
                            VALUES (%s)"""
                # 执行sql语句
                # excute 的第二个参数可以将sql缺省语句补全，一般以元组的格式
                cursor.execute(
                    sql, (address))
    
            # 提交本次插入的记录
            connection.commit()
        finally:
            # 关闭连接
            connection.close()

        return item