# PodShare

A social media for sharing short audio clips

## Installation

1. Clone this repo to your local machine

```bash
git clone https://github.com/krain9421/Podshare_v1.git
```

2. Navigate th the repo directory:

```bash
cd PodShare_v1
```

3. **Frontend Setup**:

Navigate to the frontend directory:

```bash
cd frontend
```

4. Create a virtual environment(Recommended):

```bash
python3 -m venv venv
```

5. Activate the virtual environment

- On macOS and Linux:

```bash
source venv/bin/activate
```

- On Windows (CMD):

```bash
venv\Scripts\activate.bat
```

- On Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

6. Install frontend dependencies:

```bash
pip3 install -r requirements.txt
```

7. Start frontend server

```bash
python3 wsgi.py
```

8. **Backend Setup**:

Navigate to the backend directory:

```cd ../backend```

9. Create a virtual environment(Recommended):

```bash
python3 -m venv venv
```

10. Activate the virtual environment

- On macOS and Linux:

```bash
source venv/bin/activate
```

- On Windows (CMD):

```bash
venv\Scripts\activate.bat
```

- On Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

11. Install backend dependencies:

```bash
pip3 install -r requirements.txt
```

12. Start backend server

```bash
python3 wsgi.py
```

The frontend server should now be running at http://localhost:3000.

The backend server should now be running at http://localhost:5000.

The purpose of this repository is to implement and test the backend components of the Podshare project. This README will be periodically updated to reflect changes made to the files

Console Commands

1. create
Description:
 Creates a User instance and prints the id. This instance will be saved in the path "./users/users.json"
Usage:
 create <username>
  prints "**username missing**" if username is not typed
  prints "**username must contain only characters and numbers !**" if username does not match regular expression for a standard username '[A-Za-z0-9]+'
  prints "**username already exists**" if username is present in the databases

2. post
Description:
 Creates a Post instance for a specified user. This instance will be saved in the path "./users/<username>/posts.json". <username> corresponds with the <user id> typed in the command.
Usage:
 post <user id> "<caption>"
  prints "**user id missing**" if <user id> is not typed
  prints "**user id not found**" if <user id> is not in database
  prints "**caption missing**" if <caption> is not typed

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

## Contributors

<a href="https://github.com/krain9421/Podshare_v1/graphs/contributors">
	<p align="center">
  		<img src="https://contrib.rocks/image?repo=krain9421/Podshare_v1" />
	</p>
</a>
