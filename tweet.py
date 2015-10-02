import sys 
import markov
import os # To access our OS environment variables

import twitter 
# available on lab machines but otherwise must be pip 
# installed in an active virtual env

# Using Python os.environ to get at environmental variables
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# This will print info about credentials to make sure they're correct
# print api.VerifyCredentials()

# Generate a tweet from our MarkovMachine class
def tweet():
    filenames = sys.argv[1:]  # the filenames for your text that you typed in the command line
    generator = markov.MarkovMachine()
    generator.read_files(filenames)
    return generator.make_text()
# 

entered_stuff = ""

while entered_stuff != "q":
    entered_stuff = raw_input("Press enter to tweet or q+Enter to quit. ")
    if entered_stuff == "":
        # Send a tweet
        status = api.PostUpdate(tweet())
        print status.text
    else:
        pass
