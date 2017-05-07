# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html




import json
import codecs
import MySQLdb
import MySQLdb.cursors


class JsonWithEncodingCnblogsPipeline(object):
    def process_item(self, item, spider):
        return item


    def __init__(self):
        self.file = codecs.open('test.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()




url = "127.0.0.1"
dbname = "biyao"
username = "root"
password = "123456"
charset = "utf-8"

class MySQLStorePipeline(object):

	def __init__(self):

		self.conn = MySQLdb.connect(user=username, passwd=password, db=dbname, host=url, use_unicode=True)
		self.cursor = self.conn.cursor()

		#清空表：
		self.cursor.execute("truncate table goods;")
		self.conn.commit()

	def process_item(self, item, spider):
		try:
			self.cursor.execute("""INSERT INTO goods (name,price,link,image)
							VALUES (%s, %s, %s, %s)""",
							(
								item['name'],
								item['price'],
								item['link'],
								item['image']
							)
			)
			self.conn.commit()
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		return item