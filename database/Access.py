import mysql.connector
import collections

class Accessor(object):
    def __init__(self,host,userName,passwd,databaseName):
        self.host=host
        self._userName=userName
        self._passwd=passwd
        self._databaseName=databaseName
        #self._attribute=attribute    #it is a dict
        self.conn=None
        self.cursor=None
    def connecte(self):
        try:
            self.conn = mysql.connector.connect(user=self._userName, password=self._passwd, database=self._databaseName)
            self.cursor = self.conn.cursor()
        except:
            raise "DataBase connect error,please check the db config."
    def close(self):
        # if not  self.conn:
        self.conn.close()
        # else:
        #     raise "DataBase doesn't connect,close connectiong error;please check the db config."
    def createTable(self,tableName,attribute):
        os=''
        for key in attribute.keys():
            os=os+key+' '+attribute[key]+' '+',' 
            #print(os)
        os=os[:-2]
        print(os)
        self.cursor.execute('create table '+tableName+'('+os+')')
        print("create table sucessfully!")
    def addPrimaryKey(self,tableName,attribute):
        self.cursor.execute("ALTER TABLE "+tableName+" ADD " +attribute+" INT PRIMARY KEY AUTO_INCREMENT ")
    def dropTable(self,tableName):
        print('DROP TABLE IF EXIST '+tableName)
        self.cursor.execute('DROP TABLE IF EXISTS '+tableName)
        print('drop table sucessfully')
    def insertData(self,data,tableName,fieldName):
        #os = 'insert into '+tableName+'('+fieldName+')'+'values(%s)\',['+str(data)+']'
        #print(os)
        self.cursor.execute('insert into user7(avg5)values(%s)',[0.823045])
    def selectData(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        listSelect=[]
        for x in result:
            x=str(x)
            x=x.strip('(,)')
            print(x)
            if x !=None:
                listSelect.append(float(x))
        return listSelect
    def updateData(self,sql):
        self.cursor.execute(sql)
    def deleteData(self,sql):
        self.cursor.execute(sql)
    def insertRow(self,filename,tableName):
        with open('./'+filename,encoding='utf-8')as f:
            lines=f.readlines()
            #print(lines)
        dataList=[]#save all of the data as list
        a=[]#save everyrow's data
        for l in lines:
            ls=l.strip().split(',',6)
            #print(ls[6])
            # n1,n2,n3,n4,n5,n6,n7=ls[0],ls[1],ls[2],ls[3],ls[4].ls[5],ls[6]
            # n=[n1,n2,n3,n4,n5,n6,n7]
            for i in range(7):
                if ls[i] is '':
                    a = None
                    break
                else:
                    a.append(ls[i])
            if a is not  None:
                dataList.append(a)
            a=[]
        #print(dataList[14030])
        dataList=dataList[1:]
        #print(dataList)
        for i in range(len(dataList)):
            tempList=dataList[i*1000:(i+1)*1000]
            self.cursor.executemany('insert into '+ tableName +' (Date,Open,High,Low,Close,Adj_Close,Volume) values (%s,%s,%s,%s,%s,%s,%s)',tempList)
    def avgCompute(self):
        listClose=[]
        listClose=ac1.selectData('select close from user7')
        print(listClose)
        for i in range(len(listClose)):
            if i<4:
                avg5=listClose[i]
            else:
                listAvg5=listClose[i-4:i+1]
                avg5=sum(listAvg5)/len(listAvg5)
            if i<9:
                avg10=listClose[i]
            else:
                listAvg10=listClose[i-9:i+1]
                avg10=sum(listAvg5)/len(listAvg10)
            ac1.insertData(avg5,'user7','avg5')
    def commit(self):
        self.conn.commit()
    # def tableIsExisting(self):
        
    def showTable(self):#show the exiting tables
        self.cursor.execute("show tables")
        #print(self.cursor)
        for x in self.cursor:
            print(x)
    def addField(self,tableName,addAttribute):
        os="alter table "+ tableName +' add '+ addAttribute
        print(os)
        self.cursor.execute("alter table "+ tableName +' add '+ addAttribute)
    def operate(self,a,sql=''):
        if a=='1':
            self.selectData(sql)
        if a=='2':
            self.insertData(sql)
        if a=='3':
            self.deleteData(sql)
        if a=='4':
            self.updateData(sql)
        if a=='5':
            self.createTable(sql)
        if a=='6':
            self.showTable()
    #def setTime():
        
if __name__ == '__main__':
    # sql=''
    ac1=Accessor('127.0.0.1','root', '123456', 'testdb') 
    ac1.connecte()#connecte database
    #attributeList={'id':'varchar(20)' , 'name': 'varchar(20)'}#table's attribute
    attributeList=collections.OrderedDict([('Date','DATE') , ('Open','double(16,8)'),('High','double(16,8)'),('low','double(16,8)'),('Close','double(16,8)'),('Adj_Close','double(16,8)'),('Volume','double(16,8)')])
    #ac1.createTable('user7',attributeList)#parameter are tableName and attribute
    #ac1.addPrimaryKey('user4','id')
    #ac1.dropTable('user7')
    #ac1.insertRow('BA.csv','user7')
    ac1.avgCompute()#compute avg5 and avg10
    ac1.insertData(avg5,'user7','avg5')
    ac1.commit()
    #ac1.addField('user7','avg5 double(16,8) ')
    ac1.showTable()
    L=['1','2','3','4']
    a=input('choose function: 1.select 2.insert 3.delete 4.update 5.createTable 6.showTable : ')
    if a in L:
        sql=input('input sql: ')
        ac1.operate(a,sql)
    else:
        ac1.operate(a)
    ac1.commit()
    ac1.close()
    

    
