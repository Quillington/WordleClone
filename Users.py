userDict = {}

class Users:
    def __init__(self, userID):
        self.userID = userID
        self.gameActive = False
        #might also do colorblind mode
        self.guessCount = 0
        self.points = 0
        self.accuracy = 0

    @staticmethod
    def get_user (userId):
        if not (id in userDict):
            user = Users(userId)
            #sql_retrieve(user, id)
            userDict.update({id : user})
        return userDict[id] 
        
