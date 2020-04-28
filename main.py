import send_mail
import check_stock

i = 0

while(i < 3):
    if(check_stock.available() == True):
        send_mail.sendmail()
        i += 1
    else:
        pass




