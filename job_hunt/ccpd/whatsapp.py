import pywhatkit
from django.utils import timezone
from datetime import timedelta


def whatt(ph_no,message):
       phone_numer = ph_no
       group_id = 'ItIf1zGI4tE8jOyDGAl68z'
       message =message
       current_time = timezone.now()+timedelta(hours=5, minutes=32)
       time_hour = current_time.hour
       time_minute = current_time.minute
       waiting_time_to_send = 7
       close_tab = True
       waiting_time_to_close = 15
       mode = "contact"
       if mode == "contact":
          
           pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
       elif mode == "group":
           pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
       else:
           print("Error Message: Please select a mode to send your message.")