import ftplib
import os
from datetime import date

def ftp_get_refund():
    ftplib.FTP.port = 21
    ftp = ftplib.FTP_TLS(host='hostsite',user='username', passwd='password')#Connection to host,
    ftp.getwelcome()
    ftp.cwd('dirname') #change into '' directory
    ftp.retrlines('LIST') #list contents of directory
    grab_date = date.today() #get todays date
    format_date = grab_date.strftime('%Y%m%d') #format date into yyyymmdd
    filename_refund = 'filename_{date}.txt'.format(date=format_date)  #create filename var
    local_dl = os.path.join('C:\\TEMP\\', filename_refund) #writes it to temp folder on c drive
    open_local = open(local_dl, 'wb')
    ftp.retrbinary('RETR ' + filename_refund, open(filename_refund, 'wb').write)
    ftp.quit()
    open_local.close()



ftp_get_refund()
