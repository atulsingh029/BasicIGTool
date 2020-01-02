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
    print("follower no : " + str(len(data[0])))
    print("following no : " + str(len(data[1])))
    print("mutual no : " + str(len(data[2])))
    print("followers :")
    print(data[0])
    print("following :")
    print(data[1])
    print("mutual")
    print(data[2])
    print("followersONLY")
    print(data[3])
    print("followingONLY")
    print(data[4])


