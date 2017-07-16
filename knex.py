import requests

URL = 'http://www.knex.com/instructions'

r = requests.get(URL)

with open('output.txt', 'w') as output:
    for x in range(1, 100000):
        val = "%05d" % x
        payload = { 'SearchCriteria' : val}
        session = requests.session()
        res = requests.post(URL, data=payload)
        with open('temp.txt', 'w') as temp:
            temp.write(res.content)
        with open('temp.txt', 'r') as temp:
            for line in temp:
                if line.find('ProductBuildInstructions'):
                    output.write(line)