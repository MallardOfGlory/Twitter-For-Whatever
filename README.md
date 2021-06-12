# Twitter For Whatever
Use this to tweet from custom messages


# What does this do?
This allows you to create custom platform messages 

![image](https://user-images.githubusercontent.com/65434066/121770902-7ce48b00-cbaf-11eb-8b33-f139b8471ba9.png)


# How to use it
You need to head to https://developer.twitter.com/en/portal/dashboard and create a new app
from there you can name it what you want it to display under your tweets

After that, save the keys and put them into the program, it should be self explanatory

(put them here)

![image](https://user-images.githubusercontent.com/65434066/121771251-a0a8d080-cbb1-11eb-8055-5889e48c8d1e.png)

Access token:
![image](https://user-images.githubusercontent.com/65434066/121770955-cb922500-cbaf-11eb-9d6c-e5158babeeb4.png)
Api and secret location 
![image](https://user-images.githubusercontent.com/65434066/121770966-d947aa80-cbaf-11eb-9f78-bab4c8b0a7f9.png)

After everthing is added, write what you to tweet out by replacing the "test" in message = "test" and run the program

# Replying to tweets

Replying to tweets is simple, you just need the tweet id which is located in the url

https://twitter.com/MallardOfGlory/status/1403631556799787021 the id is the numbers at the end

To make it more clear :
![image](https://user-images.githubusercontent.com/65434066/121771120-c2558800-cbb0-11eb-97ca-cb6e20ff8420.png)

then you need to head down to the bottom of the program and put a # in front of "api.update_status(status=message)" and remove the # from in front of 
"reply_status = api.update_status(status = message, in_reply_to_status_id =twitter_id, auto_populate_reply_metadata=True)"

![image](https://user-images.githubusercontent.com/65434066/121771155-fdf05200-cbb0-11eb-8809-835d01d3b0e1.png)

To head back to tweeting, just do the opposite of this

Questions, concerns? Dm me on twitter @mallardofglory

Also this program is like 2 years old, im fairly certain some of this code is not mine, I just dont know where I got it from. If you find something similar, dm me on twitter so I can add the proper credits. 



These api keys have been revoked, dont bother using them. The ones in the program are to show what they look like incase you get stuck. 
