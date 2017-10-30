from sys import argv
import time
import json
 
from api import getAPI
 
REQUEST_DELAY = 5
MAX_REQUESTS = 100
 
def main():
    try:
        arg = argv[1]
        api = getAPI()
        followerResults = []
        count = 1
        for request in range(MAX_REQUESTS):
            for follower in api.followers(screen_name=arg):
                #print(count,follower.screen_name)
                #count += 1
                followerResults.append(follower.screen_name)
            time.sleep(REQUEST_DELAY)
    except IndexError:
        print("Program Missing Arg. Twitter Handle")
    except Exception as e:
        print("Program Failure. Error: {}".format(e))
    finally:
        with open("{}Followers".format(arg), 'w') as saveFile:
            json.dump(followerResults, saveFile)
 
if __name__ == '__main__':
    main()