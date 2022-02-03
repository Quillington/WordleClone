import discord

userDict = {}

class Users:
    def __init__(self, user):
        self.userID = user.id
        self.name = user.display_name
        self.gameActive = False
        self.activeGameKey = None
        #might also do colorblind mode
        self.guessArray = []
        self.guessCount = 0
        self.points = 0
        self.accuracy = 0

    @staticmethod
    def get_user (user):
        if not (id in userDict):
            user = Users(user)
            #sql_retrieve(user, id)
            userDict.update({id : user})
        return userDict[id] 
        
