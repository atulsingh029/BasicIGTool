import IGprocessing
def fileHandling(followersfile, followingfile):
    try:
        followers=open(followersfile,'r')
        following=open(followingfile,'r')
        followingList=following.readlines()
        followersList=followers.readlines()
        followers.close()
        following.close()
        return followersList,followingList
    except:
        print("/*File not found, running tool on existing data.*/")
        retval=IGprocessing.basicData()
        return retval[0],retval[1]
