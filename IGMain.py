import IGdb
import IGprocessing
x=input("enter 1 if new files else 0")
if(x=='1'):
    print("*Enter full path of files if not in same directory")
    followersFile = input("Enter Followers file name : ")
    followingFile = input("Enter Following file name : ")
    IGdb.update(followersFile,followingFile)
    IGdb.unfollowersRecord(followersFile,followingFile)
    IGdb.refollowersRecord(followersFile,followingFile)
else:
    IGprocessing.test()