#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import numpy as np

df = pd.read_csv('/Users/jennielee/Documents/PSU 2020-2021/WINTER2021/CS510/Labs/Data Validation/crashdata.csv')
df 

CrashesDF = df[df['Record Type'] == 1]
VehiclesDF = df[df['Record Type'] == 2]
ParticipantsDF = df[df['Record Type'] == 3]

CrashesDF = CrashesDF.dropna(axis=1,how='all')
VehiclesDF = VehiclesDF.dropna(axis=1,how='all')
ParticipantsDF = ParticipantsDF.dropna(axis=1,how='all')

#Testing assertion that every record has a serial number field
def testAssertSerial():
    for item, frame in df['Serial #'].iteritems():
        if pd.isnull(frame):
            return 0 

#Testing assertion that every record has a day field
def testAssertDay():
    for item, frame in df['Crash Day'].iteritems():
        if pd.isnull(frame):
            return 0 
        
#Testing assertion that the longitudinal degrees field should be a value between -116 to -124
def testAssertLongDeg():
    for item, frame in df['Longitude Degrees'].iteritems():
        if (frame >= -116 or frame <= -124):
            return 0
        return 1
    
#Testing assertion that the crash level field should be a value between 0 and 50
def testAssertCrashLev():
    for item, frame in df['Crash Level Event 1 Code'].iteritems():
        if (frame <= 0 or frame >= 50):
            return 0
    for item2, frame2 in df['Crash Level Event 2 Code'].iteritems():
        if (frame2 <= 0 or frame2 >= 50):
            return 0
    for item3, frame3 in df['Crash Level Event 3 Code'].iteritems():
        if (frame3 <= 0 or frame3 >= 50):
            return 0
        return 1
    
#Testing assertion that every crash has a unique record type
def testAssertUniqueType():
    for item, frame in df['Crash ID'].iteritems():
        for item2, frame2 in df['Record Type'].iteritems():
            if(frame == frame + 1):
                if (frame2 == frame2 + 1):
                    return 1
                return 0
            return 0

#Testing assertion that every crash has a unique serial number
def testAssertUniqueSerial():
    for item, frame in df['Crash ID'].iteritems():
        for item2, frame2 in df['Serial #'].iteritems():
            if(frame == frame + 1):
                if (frame2 != frame2 + 1):
                    return 1
                return 0
            return 0
        
#Assertion that every crash participant has a vehicle ID
def testAssertParticipantVehicle():
    for item, frame in df['Participant ID'].iteritems():
        if (pd.notnull(frame)):
            for item2, frame2 in df['Vehicle ID'].iteritems():
                if pd.isnull(frame2):
                    return 0
                return 1
        return 0
    
#Assertion that every crash ID has a crash type
def testAssertIdType():
    for item, frame in df['Crash ID'].iteritems():
        if (pd.notnull(frame)):
            for item2, frame2 in df['Crash Type'].iteritems():
                if pd.isnull(frame2):
                    return 0
                return 1
        return 0

#Calling functions to test our the assertions        
if (testAssertSerial() == 0):
    print("Assertion that every record has a serial number field is false")
else: 
    print("Assertion that every record has a serial number field is true")
    
if (testAssertDay() == 0):
    print("Assertion that every record has a crash day field is false")
else:
    print("Assertion that every record has a crash day field is true")
    
if (testAssertLongDeg() == 0):
    print("Assertion that all the longitudinal degrees field is a value between -116 and -124 is false")
else:
    print("Assertion that all the longitudinal degrees field is a value between -116 and -124 is true")
    
if (testAssertCrashLev() == 0):
    print("Assertion that all the crash level field is a value between 0 and 50 is false")
else:
    print("Assertion that all the crash level field is a value between 0 and 50 is true")
    
if (testAssertUniqueType() == 0):
    print("Assertion that every record crash has a unique record type is false")
else:
    print("Assertion that every record crash has a unique record type is true")
    
if (testAssertUniqueSerial() == 0):
    print("Assertion that every record crash has a unique serial number is false")
else:
    print("Assertion that every record crash has a unique serial is true")

if (testAssertParticipantVehicle() == 0):
    print("Assertion that every participant ID has a vehicle ID is false")
else:
    print("Assertion that every participant ID has a vehicle ID is true")

if (testAssertIdType() == 0):
    print("Assertion that every crash ID has a crash type is false")
else:
    print("Assertion that every crash ID has a crash type is true")

