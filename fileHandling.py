def fileHandling(followersfile, followingfile):
    followers=open(followersfile,'r')
    following=open(followingfile,'r')
    followingList=following.readlines()
    followersList=followers.readlines()
    followers.close()
    following.close()
    return followersList,followingList