#Notification system
class notification:#parent class
    def send(self):
        print("notification")
class Emailnotification(notification):
    def send(self):#method override
        print("Email notification sent")
class smsnotification(notification):
    def send(self):
        print("Sms notification sent")
class whatsappnotification(notification):
    def send(self):
        print("Whatsapp notification sent")
notification1=notification()
email=Emailnotification()
sms=smsnotification()
whatsapp=whatsappnotification()
notification1.send()
email.send()
sms.send()
whatsapp.send()
