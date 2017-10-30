from sys import argv
import time
import json
 
from api import getAPI
 
REQUEST_DELAY = 7
MAX_REQUESTS = 100
 
def main():
    try:
        arg = argv[1]
        api = getAPI()
        friendResults = []
        count = 0
        
        for request in range(MAX_REQUESTS):
            for friend in api.friends(screen_name=arg):
                #user = api.get_user(friend)
                count += 1
                friendResults.append(friend.screen_name)
            time.sleep(REQUEST_DELAY)
        print(count)
    except IndexError:
        print("Program Missing Arg. Twitter Handle")
    except Exception as e:
        print("Program Failure. Error: {}".format(e))
    finally:
        with open("{}Friends".format(arg), 'w') as saveFile:
            json.dump(friendResults, saveFile)
 
if __name__ == '__main__':
    main()