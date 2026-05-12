
from abc import abstractmethod


class Notification:
   @abstractmethod
   def send(self, message):
     pass

class EmailNotification(Notification):
   def send(self, message):
     print(f"Sending email with message: {message}")
class SMSNotification(Notification):
   def send(self, message):
     print(f"Sending SMS with message: {message}")

email_notification = EmailNotification()
sms_notification = SMSNotification()
email_notification.send("Hello via Email!")
sms_notification.send("Hello via SMS!")
    