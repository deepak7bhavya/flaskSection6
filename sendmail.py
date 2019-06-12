
import smtplib
from email.message import EmailMessage

def sendMail(SENDER_ID,SENDER_PASS,RECEIVER_ID,subject,body):
    # SENDER_ID  = 'd9572712747@gmail.com'
    # SENDER_PASS = 
    # RECEIVER_ID = 'deepak986698@gmail.com'
    print("inside Send Mail")

    # subject = 'Gaurav Bhaiya Mail Subject With an Image Attachment'
    # body = 'Please Find the Image Attached'


    #Setting Message Body
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From']  = SENDER_ID
    msg['To'] = RECEIVER_ID
    msg.set_content(body)


    #Creating A Text file and Sending It

    file = open("responseData.txt","w+")
    file.write(body);
    file.close();
    file = None

    #Setting Attachment
    files = ['responseData.txt']
    for file in files:
        with open(file,'rb') as f:
            file_data = f.read();
            file_name = f.name
            #file_type = imghdr.what(file_name) # NOT NEEDED NOW

        #msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
        msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)



    #msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
    #msg.add_attachment(file_data,maintype='text',subtype='octet-stream',filename=file_name)

    print("Files Attached")


    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        #with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            # try:
            #     smtp.ehlo()
            # except:
            #     print("smtp.ehlo() me galata hai")
            # try:
            #     smtp.starttls()
            # except:
            #     print("smtp.starttls() me galat hai")
            # try:
            #     smtp.ehlo()
            # except:
            #     print("Second wala smtp.ehlo() me galata hai")
            try:
                smtp.login(SENDER_ID,SENDER_PASS)
            except Exception as e:
                print("login me galat hai")
                print(e)
                print("login me galat hai")
            
            smtp.send_message(msg)
            print("Success")
        return True;
    except:
        print("GarBad ho gya")
        return True

