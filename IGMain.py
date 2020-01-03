import IGdb
import IGprocessing
import sqlite3

try:
    myconn = sqlite3.connect("data.db")
    cur=myconn.cursor()
    cur.execute("create table instadata (username varchar(100) primary key , follower boolean,following boolean, followdate date,unfollowdate date default null );")
    myconn.commit()
    myconn.close()

except:
    print("")
    print("Please wait...")
    print("")
x = input("Input 1 to run database update else input 0 {/*warning*/ :Input Z to clear the database} : ")
if (x == '1'):
        print("*Enter full path of files if not in same directory")
        followersFile = input("Enter Followers file name : ")
        followingFile = input("Enter Following file name : ")
        IGdb.update(followersFile, followingFile)
        IGdb.unfollowersRecord(followersFile, followingFile)
        IGdb.refollowersRecord(followersFile, followingFile)
        IGdb.unfollowingRecord(followersFile, followingFile)
        IGdb.refollowingRecord(followersFile, followingFile)
        IGprocessing.test()
elif(x == "Z"):
    try:
        myconn = sqlite3.connect("data.db")
        cur = myconn.cursor()
        sql="delete from instadata"
        cur.execute(sql)
        myconn.commit()
        myconn.close()
        print("Database cleared.")

    except:
        myconn.rollback()
        print("<fatal error> Developer fix required.")
else:
        IGprocessing.test()