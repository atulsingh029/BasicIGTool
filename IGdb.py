#create table instadata (username varchar(100) primary key , follower boolean,following boolean, followdate date not null,unfollowdate date default null );
import mysql.connector
import fileHandling
def getAll():
    try:
        myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin")
    except:
        return 0
    try:
        cur = myconn.cursor()
        cur.execute("use instadb")
        cur.execute("select username,follower,following from instadata")
        resultReturn=cur.fetchall()
        myconn.close()
        return resultReturn
    except:
        myconn.rollback()
        return 0


def fileInput():
    print("*Enter full path of files if not in same directory")
    followersFile=input("Enter Followers file name : ")
    followingFile=input("Enter Following file name : ")
    fileHandlingData=fileHandling.fileHandling(followersFile,followingFile)
    return fileHandlingData


def update():
    fileHandlingData=fileInput()
    allusernames_fromnewfile=[]
    for n1 in fileHandlingData[0]:
        allusernames_fromnewfile.append(n1)
    for n2 in fileHandlingData[1]:
        allusernames_fromnewfile.append(n2)
    allusernames_existingdatabas=getAll()
    allusernames_existingdatabase=set()
    for j in allusernames_existingdatabas:
        allusernames_existingdatabase.add(j[0])
    allusernames_fromnewfile=set(allusernames_fromnewfile)
    newUsernames=allusernames_fromnewfile-allusernames_existingdatabase
    for i in newUsernames:
        temp=addNewUsername(i)
        if (temp==0):
            print("error during insert statement execution")
            exit()
        if (i in fileHandlingData[0]):
            temp1=newUserDetailsFOLLOWERS(i)
            if(temp1==0):
                print("error occurred at update level for followers")
                exit()
        if (i in fileHandlingData[1]):
            temp2=newUserDetailsFOLLOWING(i)
            if (temp2 == 0):
                print("error occurred at update level for following")
                exit()
        temp3=nullSet(i)
        if(temp3==0):
            print("null setting failed")
            exit()
    return 1


def addNewUsername(incominguser):
    try:
        myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin")
    except:
        return 0
    try:
        cur = myconn.cursor()
        cur.execute("use instadb")
        sql="insert into instadata(username, follower, following, followdate) values('"+incominguser+"',null,null,sysdate())"
        cur.execute(sql)
        myconn.commit()
        myconn.close()
        return 1
    except:
        myconn.rollback()
        return 0


def newUserDetailsFOLLOWERS(username):
    try:
        myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin")
    except:
        return 0
    try:
        cur = myconn.cursor()
        cur.execute("use instadb")
        cur.execute("update instadata set follower=true where username = '"+username+"'")
        myconn.commit()
        myconn.close()
        return 1
    except:
        myconn.rollback()
        return 0


def newUserDetailsFOLLOWING(username):
    try:
        myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin")
    except:
        return 0
    try:
        cur = myconn.cursor()
        cur.execute("use instadb")
        cur.execute("update instadata set following=true where username = '"+username+"'")
        myconn.commit()
        myconn.close()
        return 1
    except:
        myconn.rollback()
        return 0


def nullSet(username):
    try:
        myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin")
    except:
        return 0
    try:
        cur = myconn.cursor()
        cur.execute("use instadb")
        cur.execute("update instadata set follower=false where follower=null")
        cur.execute("update instadata set following=false where following=null")
        myconn.commit()
        myconn.close()
        return 1
    except:
        myconn.rollback()
        return 0

