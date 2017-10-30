import getFriends
import getFollowers
import json

class Interactions:
	def __init__(self, sourceFile=None, sourceFile2=None):
		self.followers = []
		self.friends = []
		self.notFollower = []
		self.notFollowing = []
		self.people = {}
		if sourceFile:
			self.load_friends(sourceFile)
		if sourceFile2:
			self.load_followers(sourceFile2)
		if sourceFile and sourceFile2:
			self.friendNotFollower()
			self.followerNotFriend()


	def load_friends(self, fileName):
		self.freinds = self.loadJSON(fileName)

	def load_followers(self, fileName):
		self.followers = self.loadJSON(fileName)


	def loadJSON(self, fileName):
		with open(fileName, 'r') as fileHandler:
			jsonData = json.load(fileHandler)
		return jsonData

	def friendNotFollower(self):
		for friend in self.friends:
			if friend not in self.followers:
				self.notFollower.append(friend)
		with open("FriendNotFollower", 'w') as saveFile:
			json.dump(self.notFollower, saveFile)
	def followerNotFriend(self):
		for follower in self.followers:
			if follower not in self.freinds:
				self.notFollowing.append(follower)
		with open("FollowingNotFriends",'w') as saveFile:
			json.dump(self.notFollowing,saveFile)

	def compilePeople(self):
		for friend in self.friends:
			if friend not in self.people:
				self.people[friend] = 1
		
		for follower in self.follower:
			if follower not in self.people:
				self.people[follower] = 1



