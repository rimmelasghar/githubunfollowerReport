from github import Github
import csv
from github.GithubException import UnknownObjectException

# add your configs here
username = ""
password = ""

g = Github(username,password)

try:
    user = g.get_user(username)

    followers = user.get_followers()
    followings = user.get_following()

    followers = [follower.login for follower in followers]
    followings = [following.login for following in followings]

    unfollow_lst =[]

    for i in followings:
        if i not in followers:
            text = f'https://github.com/{i}'
            unfollow_lst.append([i,text])

    cols = ["Username","url"]
    file = open('unfollowers.csv','w',newline='')
    filewriter = csv.writer(file)
    filewriter.writerow(cols)
    filewriter.writerows(unfollow_lst)

    file.close()

except UnknownObjectException:
    print("Sorry, This user can't be found")