# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:15:09 2021

@author: sbhattacharjee2
"""
import requests
import datetime
import json
import pandas as pd
import sched
import time
import sys
from playsound import playsound


# age_limit = 18
# dist_id = 294  (#BBMP)
                



def get_vaccine_availability(age_limit, dist_id, vacc):
    
    base = datetime.datetime.today()
    inp_date = base.strftime("%d-%m-%Y")
    
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(dist_id, inp_date)
    
    headers_s = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                 'Cache-Control': 'no-cache',
                 'origin':'https://www.cowin.gov.in',
                 'referer':'https://www.cowin.gov.in/',}
    response = requests.get(URL, headers = headers_s)
    
    if response.status_code not in list(range(200,299)):
        print ("ERROR")
        playsound('.\\media\\error.mp3')
                
       
          
    try:
        data = response.json()
        print(response.headers.get("ETag"))
        
        print(response.headers.get("x-cache"))
        #print (response.json)
    except:
        print (response)
        

    center_list =data['centers']
    
    
    print("searching...")
    #print(vacc)
    
    for i in range(len(center_list)):
        
        session_list = center_list[i]['sessions']
        for j in range(len(session_list)):
            if vacc == "ALL":
                
                if (session_list[j]['min_age_limit'] == age_limit) & (session_list[j]['available_capacity'] > 0):
                    # print (session_list[i])
                    print (center_list[i]['pincode'],session_list[j]['vaccine'],center_list[i]['name']
                           +"  available  ",session_list[j]['available_capacity'],"  ON ",session_list[j]['date'])
                    
                    playsound('.\\media\\alert.mp3')
            elif vacc != "ALL" :
                
                if (session_list[j]['min_age_limit'] == age_limit) & (session_list[j]['available_capacity'] > 0) & (session_list[j]['vaccine'] == vacc):
                    
                    print (center_list[i]['pincode'],session_list[j]['vaccine'],center_list[i]['name']
                           +"  available  ",session_list[j]['available_capacity'],"  ON ",session_list[j]['date'])
                    
                    playsound('.\\media\\alert.mp3')
                
                
                
    
    


if __name__ == "__main__":
    
    age_limit = int(sys.argv[1])
    dist_id = int(sys.argv[2])
    vacc = str(sys.argv[3])
    while True:
    
        get_vaccine_availability(age_limit, dist_id, vacc)
        time.sleep(5)   
            
                

        
        