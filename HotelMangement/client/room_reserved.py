import requests

endpoint = 'http://127.0.0.1:8000/hotel/reserved/'

get_response = requests.post(
    endpoint,
    json={'number': 2}
)

print('\n------------  JSON  ------------\n')
print(get_response.json())
print('\n------------------')
print('STATUS-CODE: ' + str(get_response.status_code))
print('------------------\n')