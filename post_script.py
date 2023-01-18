import requests, random
from decimal import *
import time

# CURRENTLY USING TO TEST REQUEST FUNCTIONS ON A SERVER IN DEVELOPEMENT
URL = 'http://192.168.3.182:8000/enviornment/'

def raw_eq_soilless(raw):
    RAW = float(raw)
    vwc = (6.771*(10**(-10))*(RAW**3)) - (5.105*(10**(-6))*(RAW**2)) + (1.302*(10**(-2)) * RAW) - 10.848
    return vwc
def raw_eq(raw):
    RAW = float(raw)
    vwc = (3.879*(10**-4)) * RAW - 0.6956
    vwc = vwc * 100
    return vwc


def main():
    running = True
    while running:
        user = input('Press 1 to send temp/rh data, press 2 for Teros 12 data (0 to quit):\n')

        if int(user) == 1:
            count = 0
            sending = True
            while sending:
                if count > 1440:
                    sending = False
                    break
                choices = ['F1', 'F2', 'F3']
                send_data = {'TOKEN':'11619980', 'ROOM':'F', 'DEVICE_TYPE':'ENVIORNMENT', 'DEVICE_CODE':choices[0], 'TEMP':str(random.randint(5,10)), 'RH':str(random.randint(1, 5))}
                r = requests.post(URL, data=send_data, json=send_data)
                response = 'STATUS_CODE: ' + str(r.status_code) + ': ' + r.text
                print(response)
                time.sleep(0.1)
                send_data = {'TOKEN':'11619980', 'ROOM':'F', 'DEVICE_TYPE':'ENVIORNMENT', 'DEVICE_CODE':choices[1], 'TEMP':str(random.randint(5,10)), 'RH':str(random.randint(1, 5))}
                r = requests.post(URL, data=send_data, json=send_data)
                response = 'STATUS_CODE: ' + str(r.status_code) + ': ' + r.text
                print(response)
                time.sleep(0.1)
                send_data = {'TOKEN':'11619980', 'ROOM':'F', 'DEVICE_TYPE':'ENVIORNMENT', 'DEVICE_CODE':choices[2], 'TEMP':str(random.randint(5,10)), 'RH':str(random.randint(1, 5))}
                r = requests.post(URL, data=send_data, json=send_data)
                response = 'STATUS_CODE: ' + str(r.status_code) + ': ' + r.text
                print(response)
                time.sleep(10)
                count += 1

        if int(user) == 2:
            send_data = {'TOKEN':'11619980', 'DEVICE_TYPE':'SOIL', 'DEVICE_CODE':'TT', 'MOISTURE':str(random.randint(1,9)), 'TEMP':str(random.randint(1,9)), 'EC':str(random.randint(1,9))}
            r = requests.post(URL, data=send_data, json=send_data)
            response = 'STATUS_CODE: ' + str(r.status_code) + ': ' + r.text
            print(response)



        if int(user) == 4:
            raw = input('Enter raw VWC value:\n')
            print(raw_eq_soilless(raw))

        # BULK EC
        # if int(user) == 5:
        #     raw = float(input('Enter raw EC value:\n'))
        #     temp = float(input('Enter Temp value:\n'))
        #     bulkEC = raw/ (1.00 + 0.019)
        #     print(bulkEC)

        # DIALECTRIC PERMITTIVITY BULK SOIL
        if int(user) == 6:
            raw = float(input('Enter raw VWC value:\n'))
            Eb = (2.887 * (10**-9) * (raw**3) - 2.08 * (10**-5) * (raw**2) + 5.276 * (10**-2) * raw - 43.39)**2
            print(Eb)

        # DIALECTRIC PERMITTIVITY SOIL PORE WATER
        if int(user) == 7:
            temp = float(input('Enter temp:\n'))
            Ep = 80.3 - 0.37 * (temp - 20)
            print(Ep)

        # PORE EC
        if int(user) == 8:
            Ep = float(input('Enter Ep:\n'))
            Ab = float(input('Enter Ab:\n'))
            Eb = float(input('Enter Eb:\n'))
            Ap = (Ep * Ab) / (Eb - 4.1)
            print(Ap)

        if int(user) == 0:
            running = False
            break
    
        
if __name__ == '__main__':
    main() 
