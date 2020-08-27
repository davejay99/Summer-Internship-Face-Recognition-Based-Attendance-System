import csv

import cv2
import os

import sys
# print(sys.path)

# import libraries
# counting the numbers

import mysql.connector
#connecting to mysql server
#first create database and tables manually in mysql server.
#enter your details accordingly

mydb=mysql.connector.connect(host="localhost",user="user_name",passwd="password",database="db_name")

mycursor=mydb.cursor();




def mysqlTableEntry(idd,name):
    print(mydb.connection_id)
    q2="insert into student_details(ID,Name) values (%s,%s)"##Change your table name accrodingly
    t=(idd,name)
    try:
        mycursor.execute(q2,t)
    except:
        print("ID is already saved. Use another ID and try again!")
    mydb.commit()
    print("Personal information saved to mysql database")




def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False



# Take image function

def takeImages():
    

    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")
       
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(1)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                #incrementing sample number
                sampleNum = sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep +name + "."+Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                #display the frame
                cv2.imshow('frame', img)
            #wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 60
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        print(res)
        mysqlTableEntry(Id,name)
        row = [Id, name]
        with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        if(is_number(Id)):
            print("Enter Alphabetical Name")
        if(name.isalpha()):
            print("Enter Numeric ID")


