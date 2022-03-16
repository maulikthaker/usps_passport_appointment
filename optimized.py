import requests
import csv
import random
import time

santaclara_zip = ["94022","94022","94023","94024","94024","94035","94035","94039","94040","94041","94042","94043","94085","94086","94087","94088","94088","94089","94090","94301","94302","94303","94303","94304","94305","94305","94306","94309","94309","94310","95002","95008","95009","95011","95013","95014","95014","95014","95015","95020","95021","95026","95030","95030","95031","95032","95035","95036","95037","95038","95042","95044","95046","95050","95051","95052","95054","95055","95056","95070","95071","95101","95102","95103","95106","95108","95109","95110","95111","95112","95113","95114","95115","95116","95117","95118","95119","95120","95121","95122","95123","95124","95125","95126","95127","95128","95129","95130","95131","95132","95133","95134","95135","95136","95137","95138","95139","95140","95140","95141","95142","95148","95150","95151","95152","95153","95154","95155","95156","95157","95158","95159","95160","95161","95164","95170","95171","95172","95173"]
alameda_zip = ["94501","94502","94706","94707","94708","94709","94710","94720","94702","94703","94704","94705","94552","94546","94568","94555","94536","94538","94539","94541","94542","94544","94545","94550","94551","94560","94601","94602","94603","94605","94606","94607","94608","94609","94610","94611","94612","94613","94618","94619","94621","94566","94588","94577","94578","94579","94580","94586","94587" ]
sanmateo_zip = ["94027","94002","94005","94010","94014","94015","94404","94019","94020","94021","94025","94030","94037","94038","94044","94060","94028","94061","94062","94063","94065","94066","94070","94074","94401","94402","94403","94080","94128"]
allzip = santaclara_zip + alameda_zip + sanmateo_zip


print(len(allzip))
location = []
# This csv has the field that corresponds to the location id of USPS. 
with open('po.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:     
            # Change this loop to  
        if row[3] in allzip:
            print(row[0], row[3])
            location.append(row[0])


def getInfo(locid):
    with open('po.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if row[0] == locid:
                return ','.join(row[-4:-1])
    return locid



headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type':'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }


s = requests.Session()
url = 'https://tools.usps.com/UspsToolsRestServices/rest/v2/facilityScheduleSearch'


for dt in range(17,18):
    print(dt)
    for locid in location:
        # print("Location: ",locid)
        payload = {"poScheduleType":"PASSPORT","date":"202203"+str(dt),"numberOfAdults":"0","numberOfMinors":"1","radius":"60","zip5":"95008","city":"","state":""}
        # To escape bot identification
        random_number = random.randint(1, 2)
        time.sleep(random_number)
        res = s.post(url, json=payload, headers=headers).json()
        
        for facility in res["facilityDetails"]:
            for date in facility["date"]:
                if date['status'] == 'true'
                    print(facility['address']['city'],date['date'], date['status'])
