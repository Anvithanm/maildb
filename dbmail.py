import smtplib
import getpass
import MySQLdb
#import sys
host = 'localhost'
username = 'root'
passwd = 'asm123'
db = 'mail'
db_con=MySQLdb.connect(host,username,passwd,db)
#db_cur=db_con.cursor()
db_cur=db_con.cursor(MySQLdb.cursors.DictCursor)
sql="select * from info"
db_cur.execute(sql)
sql1=db_cur.fetchall()
print sql1
str1=""
for i in sql1:
	#print i
	a="{id} {name}".format(**i)
	#print a
	str1= str1 + a + "\n"
print str1
host = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username='anvithanm22@gmail.com'
password=getpass.getpass()
server.login(username,password)
to=raw_input("to")
sub=raw_input("subject")
message=str1
#with open(mes,'r') as f:
	#f1=f.read()
	#message="subject:%s\n\n%s"%(sub,f1)
server.sendmail(username,to,message)

