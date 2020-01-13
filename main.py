import requests
import threading 

url = "https://result.dghs.gov.bd/mbbs/"
# controller
flag = -1

def search(roll):
    session = requests.Session()
   
    payload = 'roll='+roll+'&Result='
    
    headers = {
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'Origin': "https://result.dghs.gov.bd",
        'Upgrade-Insecure-Requests': "1",
        'Content-Type': "application/x-www-form-urlencoded",
        'Sec-Fetch-User': "?1",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "navigate",
        'Referer': "https://result.dghs.gov.bd/mbbs/",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Host': "result.dghs.gov.bd",
        'Content-Length': "19",
        'cache-control': "no-cache"
    }

    response = session.post(url, data=payload, headers=headers)

    webpage = str(response.text)

    #   whom result you looking for (name)
    if (webpage.find('<name>') == -1):
        return -1
    else:
        return roll

# ____________________ MAIN METHOD ____________________ #

def from_start1():
    global flag 
    for n in range(199999, 110001, -1):
        roll = str(n)

        print("Now trying: ", roll)

        # check the current code is satisfying or not
        result = search(roll)

        if result != -1:
            print("Success with code: ", code)
            print(result)
            flag = 0 

        if flag != -1:
            break

def from_start2():
    global flag 
    for n in range(220000, 200001, -1):
        roll = str(n)

        print("Now trying: ", roll)

        # check the current code is satisfying or not
        result = search(roll)

        if result != -1:
            print("Success with code: ", code)
            print(result)
            flag = 0 

        if flag != -1:
            break
        
def from_start3():
    global flag 
    for n in range(220001, 260000):
        roll = str(n)

        print("Now trying: ", roll)

        # check the current code is satisfying or not
        result = search(roll)
        
        if result != -1:
            print("Success with code: ", code)
            print(result)
            flag = 0 

        if flag != -1:
            break    

def from_start4():
    global flag 
    for n in range(280000, 260001, -1):
        roll = str(n)

        print("Now trying: ", roll)

        # check the current code is satisfying or not
        result = search(roll)

        if result != -1:
            print("Success with code: ", code)
            print(result)
            flag = 0 

        if flag != -1:
            break
        
def from_end():
    global flag 

    for n in range(2800001, 300000):
        roll = str(n)

        print("Now trying: ", roll)

        # check the current code is satisfying or not
        result = search(roll)

        if result != -1:
            print("Success with code: ", code)
            print(result)
            flag = 0 

        if flag != -1:
            break


#threading 
thread1 = threading.Thread(target=from_start1)
thread2 = threading.Thread(target=from_start2)
thread3 = threading.Thread(target=from_start3)
thread4 = threading.Thread(target=from_start4)
thread5 = threading.Thread(target=from_end)

# Brute force
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

# wait until all threads finish 
thread1.join() 
thread2.join() 
thread3.join() 
thread4.join() 
thread5.join() 

print("finish")