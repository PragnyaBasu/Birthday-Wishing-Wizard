import pandas as pd
import datetime
import smtplib
import os
os.chdir(r"D:\python birthday_wisher project")

#Enter your authentication details
GMAIL_ID = 'Your mail address'
GMAIL_PSWD = 'Password'

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject : {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)

    s.sendmail(GMAIL_ID, to, f"Subject : {sub}\n\n{msg}")
    s.quit()

if __name__=="__main__":
    df=pd.read_excel("data.xlsx")
    
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
   
    writeInd=[]
    for index, item in df.iterrows():
        bday=item['Birthday'].strftime("%d-%m")
        
        if(today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)
    
    for i in writeInd:
        yr=df.loc[i, 'Year']
        
        df['Year'] = df['Year'].astype(str)
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)

    df.to_excel('data.xlsx', index=False)