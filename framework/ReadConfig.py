# encoding: utf-8
"""
@Author  : nqp
@desc    :
"""

from configparser import ConfigParser
import os
import sys

# 配置文件路径
configPath = os.path.join(os.path.dirname(os.path.dirname(__file__)) , 'config/config.ini')

class ReadConfig:
	def __init__(self):
		self.cf = ConfigParser()
		self.cf.read(configPath, encoding='UTF-8')

	def get_browser_type(self):
		browserName = self.cf.get("BROWSERTYPE", "browserName")
		return browserName

	def get_browser_attribute(self):
		implicitly_wait = self.cf.get("BROWSERATTRIBUTE", "implicitly_wait")
		return implicitly_wait

	def get_test_server(self):
		url = self.cf.get("TESTSERVER", "url")
		return url

	def get_test_account(self):
		account = self.cf.get("TESTACCOUNT", "account")
		password = self.cf.get("TESTACCOUNT", "password")
		name = self.cf.get("TESTACCOUNT", "name")
		value ={'account':account,'password':password,'name':name}
		return value

	def get_database(self):
		user = self.cf.get("DATABASE", "user")
		password = self.cf.get("DATABASE", "password")
		database = self.cf.get("DATABASE", "database")
		host = self.cf.get("DATABASE", "host")
		port = self.cf.get("DATABASE", "port")
		value = {'user':user,'password':password,'database':database,'host':host,'port':port}
		return value

	def get_test_data(self, *args):
		"""
		从配置文件中获取测试数据，接收可变数量的参数
		:param args:
		:return: 返回字典
		"""
		a={}
		for i in args:
			a[i]=self.cf.get("TESTDATA", i)
		return a
