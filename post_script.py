import requests, random

# CURRENTLY USING TO TEST REQUEST FUNCTIONS ON A SERVER IN DEVELOPEMENT
URL = 'http://127.0.0.1:8000/post/'


def main():
    send_data = {'API_KEY':'1111', 'DEVICE_CODE':'new_test', 'TEMP':str(random.randint(1,9)), 'RH':str(random.randint(1,9))}
    r = requests.post(URL, data=send_data, json=send_data)
    response = 'STATUS_CODE: ' + str(r.status_code) + ': ' + r.text  
    print(response)
        
if __name__ == '__main__':
    main() 
