import requests
import sys
from urls import urls_list
import time

scr, base_url, token = sys.argv

head = {'Authorization': 'Token {}'.format(token)}
response_data = [["Endpoints", "Type", "Time", "Status"]]

longest_cols = [(max([len(row) for row in urls_list]) + 3)]
row_format = "{:>" + str(longest_cols[0]) +  "} {:>10} {:>10} {:>10}"
print('\n',row_format.format(*response_data[0]),'\n')
# print('\n')
for idx,uri in enumerate(urls_list):
    start = time.time()
    resp = requests.get(f'https://{base_url}/api/v2/{uri}', headers=head)
    end = time.time()
    print(row_format.format(*[uri, 'GET', str(round(end-start, 2)), 'true' if int(resp.status_code) == 200 else resp.status_code]))
print('\n')

