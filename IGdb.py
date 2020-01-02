#create table instadata (username varchar(100) primary key , follower boolean,following boolean, followdate date not null,unfollowdate date default null );
import mysql.connector
import IGprocessing
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
def fileInput(followersFile,followingFile):
    fileHandlingData=fileHandling.fileHandling(followersFile,followingFile)
    return fileHandlingData
def update(followersFile,followingFile):
    fileHandlingData=fileInput(followersFile,followingFile)
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
def unfollowersRecord(followersFile,followingFile):
    data=IGprocessing.basicData()
    followerList=data[0]   #in exixting database
    followerListFromFil=fileHandling.fileHandling(followersFile,followingFile)
    followerListFromFile=followerListFromFil[0]
    for i in followerList:
        if(i in followerListFromFile):
            pass
        else:
            try:
                myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin")
            except:
                return 0
            try:
                cur = myconn.cursor()
                cur.execute("use instadb")
                cur.execute("update instadata set follower=false where username = '" + i + "'")
                cur.execute("update instadata set follower=false,unfollowdate=sysdate() where username = '" + i + "'")
                print("Unfollowed :"+i)
                myconn.commit()
                myconn.close()
                return 1
            except:
                myconn.rollback()
                return 0
def refollowersRecord(followersFile,followingFile):
    data=IGprocessing.basicData()
    followingList=data[1] #from database
    for it in data[0]:
        followingList.append(it)
    followingList=set(followingList)
    followerListFromFil=fileHandling.fileHandling(followersFile,followingFile)
    followerListFromFile=followerListFromFil[0] #from file
    for k in followerListFromFile:
        if(k in followingList):
            try:
                myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin")
            except:
                return 0
            try:
                cur = myconn.cursor()
                cur.execute("use instadb")
                cur.execute("update instadata set follower=true where username = '" + k + "'")
                cur.execute("update instadata set follower=true,unfollowdate=null where username = '" + k + "'")
                myconn.commit()
                myconn.close()
                return 1
            except:
                myconn.rollback()
                return 0
