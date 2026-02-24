import pymysql
from password_utilize import *
def sqlconn():

""" when we connect sql DB we need user and pass
but passsword highly sesitive where admin only can see it will hlp when we create with password +binary encrpted that will password
hide using function get_decrypted_password"""




 conn = pymysql.connect(
   host='localhost',
   user='',
   password=get_decrypt_password(),
   database='')

 print("connection successful")
 conn.close()
if __name__=="__main__":

    sqlconn()
