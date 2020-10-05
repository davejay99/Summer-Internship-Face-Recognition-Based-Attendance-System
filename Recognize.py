import datetime
import os
import time
# import fileuploadsql
import cv2
import pandas as pd
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="mysqluser",passwd="password",database="db_name")
mycursor=mydb.cursor();
print("connection id is "+str(mydb.connection_id));


def dbEntry(t):
   
    q="INSERT INTO attendance(ID,Name,Date,Time,Course_ID) VALUES (%s,%s,%s,%s,%s)" ##Change your table name accrodingly
    X=(str(t[0]),str(t[1]),str(t[2]),str(t[3]),str(t[4]))
    try:
        mycursor.execute(q,X)
    except:
        print("Okay")

    print("Taken for "+ t[1])
    mydb.commit()

#--------------------------
def recognize_attendence():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel"+os.sep+"Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails"+os.sep+"StudentDetails.csv")
    cam = cv2.VideoCapture(1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    course =input("Enter course name:")

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

            if(conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(
                    ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                dbEntry((Id, aa, date, timeStamp,course))

            else:
                Id = 'Unknown'
                tt = str(Id)
            if(conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown"+os.sep+"Image"+str(noOfFile) +
                            ".jpg", im[y:y+h, x:x+w])
            lossInPercentage = rounf(conf)
            accuracyInPercentage = 100 - lossInPercentage
            tt = tt+" "+ str(accuracyInPercentage)+"%"
            cv2.putText(im, str(tt), (x, y+h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance"+os.sep+"Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName, index=False)
    

    cam.release()
    cv2.destroyAllWindows()

    print("Attendance Successfull")
    # fileuploadsql.insertBLOB(5, "attendancefile", "D:\\FRAS\\TrainingImage\\Aamir.3.1.jpg",
    #       "D:\\FRAS\\Attendance\\"+str(fileName))