import json
import argparse
import requests
import sys,time
from datetime import date

parser = argparse.ArgumentParser(description="Manual")
parser.add_argument("-t",dest="TARGET",help="Your Target",required=False)
arguments = parser.parse_args()
try:
    def main(host):
        time.sleep(1)
        print("started in {}".format(date.today()))
        time.sleep(1)
        print("testing the site ...")
        r = requests.get(host)
        if(r.status_code==200):
            time.sleep(1)
            print("website ok ...\ncertifying wordpress ...")
            time.sleep(1)
            r2 = requests.get(host+"/wp-login.php")
            if(r2.status_code==200):
                r3 = requests.get(host+"/wp-json/wp/v2/users")
                var_code = r3.content.decode("utf-8")
                global json
                json = json.loads(var_code)
                for x in json[0:20]:
                    print("\nUser: {}\nID: {}".format(x['name'],x['id']))
            else:
                print("this site does not have wordpress")
                sys.exit(0)
        else:
            print("website is not online")
            sys.exit(0)

    main(arguments.TARGET)

except:
     print("Error,arguments not found")
     sys.exit(0)
