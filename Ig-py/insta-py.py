import os
import glob
import time
from tkinter.scrolledtext import ScrolledText

cookie_del = glob.glob("config/*cookie.json")
if cookie_del: os.remove(cookie_del[0])
import sys
from instabot import Bot
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


def notification1():
    result.delete(0.0, END)
    result.insert(END, "Running")
    return


def notification2():
    result.delete(0.0, END)
    result.insert(END, "Done")
    return


def notification3():
    result.delete(0.0, END)
    result.insert(END, "Log in successful")
    return


def notification4():
    result.delete(0.0, END)
    result.insert(END, "try again later!")
    return


def upload_photo():
    cookie_del = glob.glob("config/*cookie.json")
    if cookie_del: os.remove(cookie_del[0])

    notification1()
    us = str(username.get())
    usp = str(Password.get())
    message = str(caption.get("1.0", "end-1c"))
    sys.path.append(os.path.join(sys.path[0], "../"))

    bot = Bot()
    time.sleep(5)
    try:
        bot.login(username=us, password=usp)
        notification3()
    except exception:
        notification4()
    bot.upload_photo(photo, caption=message)
    notification2()

    return


def unfollow_nonfollowers():
    cookie_del = glob.glob("config/*cookie.json")
    if cookie_del: os.remove(cookie_del[0])

    notification1()
    us = str(username.get())
    usp = str(Password.get())
    sys.path.append(os.path.join(sys.path[0], "../"))

    bot = Bot()
    time.sleep(5)
    try:
        bot.login(username=us, password=usp)
        notification3()
    except exception:
        notification4()
    bot.unfollow_non_followers()
    notification2()

    return


def post_story():
    cookie_del = glob.glob("config/*cookie.json")
    if cookie_del: os.remove(cookie_del[0])

    notification1()
    us = str(username.get())
    usp = str(Password.get())
    sys.path.append(os.path.join(sys.path[0], "../"))

    bot = Bot()
    time.sleep(5)
    try:
        bot.login(username=us, password=usp)
        notification3()
    except exception:
        notification4()
    bot.upload_story_photo(photo)

    return


def follow_user_followers():
    cookie_del = glob.glob("config/*cookie.json")
    if cookie_del: os.remove(cookie_del[0])

    notification1()
    us = str(username.get())
    usp = str(Password.get())
    users = str(User.get())
    sys.path.append(os.path.join(sys.path[0], "../"))

    bot = Bot(
        filter_users=True,
        filter_private_users=False,
        filter_previously_followed=True,
        filter_business_accounts=True,
        filter_verified_accounts=True, )
    time.sleep(5)
    try:
        bot.login(username=us, password=usp)
        notification3()
    except exception:
        notification4()
    bot.follow_followers(users)
    notification2()

    return


def follow_user_following():
    cookie_del = glob.glob("config/*cookie.json")
    if cookie_del: os.remove(cookie_del[0])

    notification1()
    us = str(username.get())
    usp = str(Password.get())
    users = str(User.get())
    sys.path.append(os.path.join(sys.path[0], "../"))

    bot = Bot(
        filter_users=True,
        filter_private_users=False,
        filter_previously_followed=True,
        filter_business_accounts=True,
        filter_verified_accounts=True, )
    time.sleep(5)

    try:
        bot.login(username=us, password=usp)
        notification3()
    except exception:
        notification4()
    bot.follow_following(users)
    notification2()

    return


def follow_users_from_file():
    cookie_del = glob.glob("config/*cookie.json")
    if cookie_del: os.remove(cookie_del[0])

    notification1()
    us = str(username.get())
    usp = str(Password.get())
    filepath = str(file_path.get())
    sys.path.append(os.path.join(sys.path[0], "../"))

    bot = Bot(filter_users=False)
    time.sleep(5)

    users_to_follow = bot.read_list_from_file(filepath)

    if not users_to_follow:
        exit()
    else:
        print("Found %d users in file." % len(users_to_follow))

    try:
        bot.login(username=us, password=usp)
        notification3()
    except exception:
        notification4()
    bot.follow_users(users_to_follow)
    notification2()

    return


def delete_all_medias():
    cookie_del = glob.glob("config/*cookie.json")
    if cookie_del: os.remove(cookie_del[0])

    notification1()
    us = str(username.get())
    usp = str(Password.get())

    sys.path.append(os.path.join(sys.path[0], "../"))
    bot = Bot()
    time.sleep(5)
    try:
        bot.login(username=us, password=usp)
        notification3()
    except exception:
        notification4()
    medias = bot.get_total_user_medias(bot.user_id)
    bot.delete_medias(medias)
    notification2()

    return


def like_timeline():
    cookie_del = glob.glob("config/*cookie.json")
    if cookie_del: os.remove(cookie_del[0])

    notification1()
    us = str(username.get())
    usp = str(Password.get())
    sys.path.append(os.path.join(sys.path[0], "../"))
    bot = Bot()
    time.sleep(5)
    try:
        bot.login(username=us, password=usp)
        notification3()
    except exception:
        notification4()
    bot.like_timeline()
    notification2()
    return


window = Tk()
window.geometry("350x400")  # the size of the window
window.title("IG-py | ©Bamidele 2021")
window.iconbitmap(r"C:\Users\bamid\Desktop\BamSpace\Data_Science_Tutorial\Python Codes\GUIs\IG-py\IG-png.ico")

Programname = Label(window, font=('Verdana', 12, 'bold'), text="IG-PY | Manage Instagram Offline",
                    fg="blue")

Programname.grid(row=1, column=6, padx=30, pady=10)

Choosepath = Label(window, font=('Verdana', 8, 'italic'),
                   text="Choose an image to post or cancel",
                   fg="red")
Choosepath.place(relx=.01, rely=.12)

Username_label = Label(window, text="Username", font=('Copperplate Gothic', 10))
Username_label.place(relx=.01, rely=.18)

username = Entry(window)
username.place(relx=.01, rely=.24)

Password_label = Label(window, text="Password", font=('Copperplate Gothic', 10))
Password_label.place(relx=.01, rely=.30)

Password = Entry(window, show="*")
Password.place(relx=.01, rely=.36)

message_label = Label(window, text="Caption  (optional)", font=('Copperplate Gothic', 10))
message_label.place(relx=.01, rely=.42)

caption = ScrolledText(window, height=3, width=40, wrap=WORD)
caption.place(relx=.01, rely=.48)

upload = Button(window, text="Post", command=upload_photo, fg='blue')  # link this to the function
upload.place(relx=.02, rely=.90)

post_story = Button(window, text="Post Story", command=post_story, fg='blue')  # link this to the function
post_story.place(relx=.13, rely=.90)

# follow and unfollow

User_label = Label(window, text="Ext-User (optional)", font=('Copperplate Gothic', 10))
User_label.place(relx=.02, rely=.65)

User = Entry(window)
User.place(relx=.02, rely=.70)

users_filepath_label = Label(window, text="Users file (optional)", font=('Copperplate Gothic', 10))
users_filepath_label.place(relx=.02, rely=.75)

file_path = Entry(window)
file_path.place(relx=.02, rely=.80)

account_label = Label(window, text="Manage Account", font=('Copperplate Gothic', 10))
account_label.place(relx=.50, rely=.18)

unfollow_unfollowing = Button(window, text="Unfollow Nonfollowers", command=unfollow_nonfollowers,
                              fg='red')  # link this to the function
unfollow_unfollowing.place(relx=.50, rely=.24)

follow_users_followers = Button(window, text="Follow followers",
                                command=follow_user_followers)  # link this to the function
follow_users_followers.place(relx=.51, rely=.64)

follow_users_followings = Button(window, text="Follow followings",
                                 command=follow_user_following)  # link this to the function
follow_users_followings.place(relx=.50, rely=.72)

follow_users_from_file = Button(window, text="Follow Users in File",
                                command=follow_users_from_file)  # link this to the function
follow_users_from_file.place(relx=.50, rely=.80)

# delete_all_medias

Delete_all_medias = Button(window, text="Delete all medias", command=delete_all_medias,
                           fg='red')  # link this to the function
Delete_all_medias.place(relx=.38, rely=.90)

# like_timeline

like_timeline = Button(window, text="Like Timeline", command=like_timeline)  # link this to the function
like_timeline.place(relx=.50, rely=.36)

# Success?

result = Text(window, height=1, width=10, wrap=WORD)
result.place(relx=.71, rely=.91)

photo = askopenfilename()

window.mainloop()  # to keep the window open continuously
