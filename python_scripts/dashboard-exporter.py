import json
import os
import requests
from pathlib import Path
from zipfile import ZipFile

#######################################
# Requires: requests |  $ pip install requests
# This script will promt for a APIKEY
# then create a .json for all the users dashboards
#######################################

APIKEY = 'APIKEY'   
HOST = 'https://www.hostedgraphite.com/api/v2/grafana/'
NPATH = "HG_dashboard_exports"
OUTPUT_PATH = "./"+NPATH+"/"
ZIP_NAME = NPATH+".zip"

dashboards = []

def main():
    """
    Requests a users API and writes all the users dashboards
    to a new folder /<NPATH>/<dashboard-name>.json.
    Also creates a .zip
    """

    # Prompt for users API key...
    print("Please enter API-Key: ")
    APIKEY = input()

    # Request API webserver for response
    r = requests.get(HOST + "search?", auth=(APIKEY, ""))

    # Check if the request failed (bad APIKEY)
    if not r:
        print("Invalid API key. Bye-bye")
        return

    # Status update ;P
    print("Hold on, Exporting dashboards...")

    # Go through request data for dashboards
    data = r.json()
    for dash in data:
        # Ignore folders
        if dash['type'] != "dash-folder":
            # Ignore png
            if "png" in dash['title']:
                continue
            else:
                # Add the dashboard to the list
                dashboards.append(dash['uri'])

    count = 0
    Path(NPATH).mkdir(exist_ok=True)

    # Go though all dashboards d = db/<dashboard_name>
    for d in dashboards:
        # Isolate the name
        dash_name = d.replace("db/","")
        request_url = HOST + "dashboards/" + dash_name

        # Request API for dashboard data by name
        r = requests.get(request_url, auth=(APIKEY, ""))
        # Turn request to .json
        j = r.json()

        # Write the dashboard data to <dashboard-name>.json with clean formatting
        with open(OUTPUT_PATH + dash_name + '.json', 'w', encoding='utf-8') as f:
            json.dump(j['dashboard'], f, ensure_ascii=False, indent=4)

        print("File created | " + OUTPUT_PATH + dash_name + ".json")
        count += 1

    # Display export count and create a .zip
    print(str(count) + " dashboards were exported to /exports")
    make_Zip(ZIP_NAME, OUTPUT_PATH)
    print("Zip created : " + ZIP_NAME)
   
    #End Main
    return

def make_Zip(zip_name, dir_path):
    """ 
    This makes .zips?
    @param: zip_name = name of the output file
            dir_path = dir to zip
    """
    zf = ZipFile(zip_name, "w")
    for dirname, subdirs, files in os.walk(dir_path):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
    return


# Start main
if __name__ == "__main__":
    main()
