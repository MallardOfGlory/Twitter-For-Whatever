import tweepy

message = ("media test")
twitter_id = "1403631556799787021"
media = r"C:\Users\Epicd\Pictures\on the outside.JPG"
#This is where you need to put all your keys
#get them from https://developer.twitter.com/

api_key = 'Dla0xG4gs2DHHuKvMwPuaQcUV'
api_secret = '2HubLcTN3fd5nM8NvTPmyBHqHXnaROZdTZ8mDtU3HZuqYPf4xx'
acc_token = '1216274984747835392-cKoQSeKyDr0aqNMZ6rxsbVkIesT17g'
acc_secret = 'XObinwdCJtndHM5SFH4yscA8cDUZkdOjnZR1DKFdDaipE'


#ignore this stuff
thingy = tweepy.OAuthHandler(api_key, api_secret)
thingy.set_access_token(acc_token, acc_secret)
api = tweepy.API(thingy)

#This is where you can tweet what you want
#replace twitter_id with the tweet id and run the program
#THIS IS CURRENTLY SET UP TO TWEET AND REPLY TO A TWEET
#to just tweet, add a # infront of line 31
#to reply to a message, add a # infront of line 33
#images only work for tweets right now, I want to add them to replies but I also want to play fortnite
#For media, remove the # for line 29 and add # for lines 31 and 33

#Gets image and tweet and shoves them together
status = api.update_with_media(message, media)
#replies to a tweet
#reply_status = api.update_status(status = message, in_reply_to_status_id =twitter_id, auto_populate_reply_metadata=True)
#Tweets out (only use with replying/normally tweeting, dont use when you want to tweet an image)
#api.update_status(status=message)
