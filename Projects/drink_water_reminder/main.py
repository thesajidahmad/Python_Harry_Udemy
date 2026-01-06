import time
from plyer import notification
import osascript

while True:
    notification.notify(title="Water Reminder", message="Please sip some water!!", app_name="ASP", timeout=3)
    # print("Drink Water!!")
    # osascript.run("Test lock") #for mac os but i have not tested yet!!
    time.sleep(5)