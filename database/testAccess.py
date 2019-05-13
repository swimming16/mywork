import unittest
import Access
from collections import OrderedDict


# class TestAccess(unittest.TestCase):
# 	def setUp(self):
# 	def testconnecte(self):


if __name__ == '__main__':
	ac1=Access.Accessor('127.0.0.1','root', '123456', 'testdb')
	ac1.connecte()
	attributeList=OrderedDict([('Date','DATE') , ('Open','int(10)'),('High','int(10)'),('low','int(10)'),('Close','int(10)'),('Adj_Close','int(10)'),('Volume','int(10)')])
	#ac1.createTable('BAtable',attributeList)
	#ac1.dropTable('BAtable')
	#ac1.insertRow('BA.csv','BAtable')
	#ac1.commit()
	ac1.addField('BAtable','avg5 double(16,8) ')
	ac1.addField('BAtable','avg10 double(16,8) ')
	ac1.showTable()

	unittest.main()
