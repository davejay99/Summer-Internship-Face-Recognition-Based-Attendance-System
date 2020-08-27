import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='jay',
                                             user='jay',
                                             password='dj141199')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO python_employee
                          (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# insertBLOB(1, "Eric", "D:\\FRAS\\TrainingImage\\Aamir.3.1.jpg",
#            "C:\\Users\\DJ\\Desktop\\output.txt")
# insertBLOB(2, "Scott", "D:\\FRAS\\TrainingImage\\Aamir.3.2.jpg",
# #            "C:\\Users\\DJ\\Desktop\\file.txt")
# insertBLOB(3, "Attendance", "D:\\FRAS\\TrainingImage\\Aamir.3.1.jpg",
#           "D:\\FRAS\\Attendance\\Attendance_2020-07-27_15-14-47.csv")