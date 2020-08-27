import yagmail
import os
import fileuploadsql


receiver = "receiver@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2020-07-26_11-57-52.csv"  # attach the file

# mail information
yag = yagmail.SMTP("user@gmail.com", "123455")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
