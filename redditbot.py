# coding: utf-8
import praw

reddit = praw.Reddit(client_id='sBx6U_qoUZzelw',
client_secret='y841Y85Zcsslxxj-UozcsFdoKwc',
password='r3o809h',
user_agent= 'factscript by /u/ponkbrown',
username='ponkbrown')


subreddit = reddit.subreddit('todayilearned')
#count = 1
#for submission in subreddit.hot(limit=1000):
#    print('[{}]'.format(count), end='')
#    print ('===' * 10)
#    print()
#    print(submission.title)
#    print(submission.id)
#    print(submission.url)
#    count += 1
#    input()
#    
#til = reddit.subreddit('todayilearned')
#arizona = til.search('Sonora', limit=5)
#for sub in arizona:
#    print(sub.title)
#    print(sub.url)
#    print(sub.id)
#    print()
#    
