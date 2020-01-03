import IGdb
def basicData():
    followersList=[]
    followingList=[]
    basicResult=IGdb.getAll()
    if(basicResult==0):
        print("Error Occurred : data from Database Module is ZERO, failed at Database Module.")
        exit()
    for i in basicResult:
        if(i[1]==1):
            followersList.append(i[0])
        if(i[2]==1):
            followingList.append(i[0])
    return followersList,followingList
def dataSet():
    data=basicData()
    followerset = set(data[0])                          #changes list of followers to set of followers          [0]
    followingset = set(data[1])                         #changes list of following to set of following          [1]
    mutual = followerset.intersection(followingset)     #set of mutual followers                                [2]
    followersOnly=followerset-followingset              #set of followers whom I don't follow                   [3]
    followingOnly = followingset - followerset          #set of usernames I follow but they don't follow back   [4]
    return followerset,followingset,mutual,followersOnly,followingOnly
def test():
    data = dataSet()
    print("")
    print("Followers : " + str(len(data[0]))+"\t",end="\t")
    print("Following : " + str(len(data[1]))+"\t",end="\t")
    print("Mutual Followers : " + str(len(data[2]))+"\t",end='\t')
    print("")
    print("Followers Only : " + str(len(data[3])) + "\t", end='\t')
    print("Following Only : " + str(len(data[4])) + "\t", end='\t')
    print("")
    print("")
    print("Followers List :")
    print(data[0])
    print("Following List :")
    print(data[1])
    print("Mutual List :")
    print(data[2])
    print("Followers You Don't follow back :")
    print(data[3])
    print("following who don't follow you back :")
    print(data[4])


