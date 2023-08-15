The purpose of this repository is to implement and test the backend components of the Podshare project. This README will be periodically updated to reflect changes made to the files

Console Commands
1. create
Description:
	Creates a User instance and prints the id. This instance will be saved in the path "./users/users.json"
Usage: 
	create <username>
		prints "** username missing **" if username is not typed
		prints "** username must contain only characters and numbers ! **" if username does not match regular expression for a standard username '[A-Za-z0-9]+'
		prints "** username already exists **" if username is present in the databases

2. post
Description:
	Creates a Post instance for a specified user. This instance will be saved in the path "./users/<username>/posts.json". <username> corresponds with the <user id> typed in the command.
Usage:
	post <user id> "<caption>"
		prints "** user id missing **" if <user id> is not typed
		prints "** user id not found **" if <user id> is not in database
		prints "** caption missing **" if <caption> is not typed

3. users
Description:
	Prints out all the usernames and corresponding ids
Usage:
	users

Data Models
All models inherit from the BaseModel class
1. User
Attributes:
	username (string)
	email (string)
	password (string)
	first_name (string)
	last_name (string)
	posts (dict): dictionary containing all Post instances created by the User
	followers (list): list that contains all other Users following the User
	following (list): list that contains all other Users followed by the User
	likes (dict): dictionary containing all instances of Posts liked by the User

Methods/Action:
	createPost(): creates a Post instance for a user.

2. Post
Attributes:
	audioId (string): link to the audio file.
	caption (string): text caption for the post.
	userId (string): id of the User instance that created the post.
	likes (list): list that contains all User instances that liked the post.
	numberOfPlays (int): number of times a Post audio has been played.

3. Comment
Inherits all attributes from the Post model.
