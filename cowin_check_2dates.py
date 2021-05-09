# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:15:09 2021

@author: sbhattacharjee2
"""
import requests
import datetime
from datetime import timedelta
import json
import pandas as pd
import sched
import time
import sys
from playsound import playsound


# age_limit = 18
# dist_id = 294  (#BBMP)
                



def get_vaccine_availability(age_limit, dist_id, inp_date, vacc):
    
    base = pd.to_datetime(inp_date,dayfirst=True)
    tomorrow = base + timedelta(days = 1)
    enter_date1 = base.strftime("%d-%m-%Y")
    enter_date2 = tomorrow.strftime("%d-%m-%Y")
    #global a
    #a=a+1
    #print (a)
    #print(etag)
   
    URL1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(dist_id, enter_date1)
    URL2 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(dist_id, enter_date2)
    
    headers_s = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
                 #'Cache-Control': 'no-cache',
                 #'origin':'https://www.cowin.gov.in',
                 #'referer':'https://www.cowin.gov.in/',
                 #'if-none-match': etag,
                 #'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                 #'sec-ch-ua-mobile': '?0'
              
    response1 = requests.get(URL1, headers = headers_s)
    response2 = requests.get(URL2, headers = headers_s)
    print(URL1)
    print(URL2)
    if response1.status_code not in list(range(200,299)):
        print ("ERROR")
        playsound('.\\media\\error.mp3')
    if response2.status_code not in list(range(200,299)):
        print ("ERROR")
        playsound('.\\media\\error.mp3')
           
                
        
    
    try:
        data1 = response1.json()
        data2 = response2.json()
        data1.update(data2)
        #print(response.headers.get("ETag"))
        #etag = response.headers.get("ETag")
        #print(response.headers.get("x-cache"))
        #print (response.json)
    except:
        print (response1)
        print (response2)
    session_list =data1['sessions']
    
    
    print("searching...")
    #print(vacc)
    
    
    for i in range(len(session_list)):
            if vacc == "ALL":
                
                if (session_list[i]['min_age_limit'] == age_limit) & (session_list[i]['available_capacity'] > 1):
                    # print (session_list[i])
                    print (session_list[i]['pincode'],session_list[i]['vaccine'],session_list[i]['name']
                           +"  available  ",session_list[i]['available_capacity'],"  ON ",session_list[i]['date'])
                    
                    playsound('.\\media\\alert.mp3')
            elif vacc != "ALL" :
                
                if (session_list[i]['min_age_limit'] == age_limit) & (session_list[i]['available_capacity'] > 1) & (session_list[i]['vaccine'] == vacc):
                    
                    print (session_list[i]['pincode'],session_list[i]['vaccine'],session_list[i]['name']
                           +"  available  ",session_list[i]['available_capacity'],"  ON ",session_list[i]['date'])
                    
                    playsound('.\\media\\alert.mp3')
                
                
                


if __name__ == "__main__":
    
    age_limit = int(sys.argv[1])
    dist_id = int(sys.argv[2])
    inp_date = str(sys.argv[3])
    vacc = str(sys.argv[4])
    while True:
        
        get_vaccine_availability(age_limit, dist_id, inp_date, vacc)
        time.sleep(7)   
                
                

        
        