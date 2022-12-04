import pymysql
 
class MyImg:
    def __init__(self):
        pass
    
    def getImg(self):
        ret = []
        db = pymysql.connect(host='localhost:3306', user='root', db='img', password='1q2w3e4r5t%^', charset='utf8')
        curs = db.cursor()
        
        sql = "select * from emp";
        curs.execute(sql)
        
        rows = curs.fetchall()
        for e in rows:
            temp = {'id':e[0],'src':e[1] }
            ret.append(temp)
        
        db.commit()
        db.close()
        return ret
    
    def insImg(self, id, src):
        db = pymysql.connect(host='localhost',port=3306, user='root', db='img', password='1q2w3e4r5t%^')
        curs = db.cursor()
        
        sql = '''insert into img (id, src) values(%s,%s)'''
        curs.execute(sql,(id, src))
        db.commit()
        db.close()
    
    def updImg(self, id, src): 
        db = pymysql.connect(host='localhost:3306', user='root', db='img', password='1q2w3e4r5t%^', charset='utf8')
        curs = db.cursor()
        
        sql = "update img set src=%s where id=%s"
        curs.execute(sql,(src, id))
        db.commit()
        db.close()
    def delImg(self, id):
        db = pymysql.connect(host='localhost',port = 3306, user='root', db='img', password='1q2w3e4r5t%^')
        curs = db.cursor()
        
        sql = "delete from img where id=%s"
        curs.execute(sql,id)
        db.commit()
        db.close()
 
if __name__ == '__main__':
    #MyEmpDao().insEmp('aaa', 'bb', 'cc', 'dd')
    #MyEmpDao().updEmp('aa', 'dd', 'dd', 'aa')
    #MyEmpDao().delEmp('aaa')
    emplist = MyImg().getImg();
    print(emplist)