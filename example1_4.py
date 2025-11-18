"""time conversion"""
# Time Conversion
# Question:
# Write a function that converts time from 12-hour format to 24-hour format.
# Example:
# Input: "07:45 PM" → Output: "19:45"

#timezone
# IST >> UTC+5:30 >> India
# PST >> UTC-8:00 >> California,USA
# CET >> UTC+1:00 >> Central Eroupe
# JST >> UTC+9:00 >> Japan
#iceland has same utc time in all year
# uk-london has same utc time during winter and if summer means UTC+1:00

#timezone(timezone.utc) used for only utc
#if want ist means, i can use zoneinfo("Asia/Kolkata")
#if i want to convert utc to other timezone means, use .astimezone()



from datetime import datetime, timezone # pip install tzdata
from zoneinfo import ZoneInfo

NORMAL_TIME="07:45 PM"#str(input("enter:")) #"07:45 PM"
time_12hr=datetime.strptime(NORMAL_TIME, "%I:%M %p")
time_24hr=time_12hr.strftime("%H:%M")

print("24-hour:",time_24hr)


utc_time=datetime.now(timezone.utc)
ist=datetime.now(ZoneInfo("Asia/Kolkata"))
indian_time=utc_time.astimezone(ZoneInfo("Asia/Kolkata"))
chicago_time=utc_time.astimezone(ZoneInfo("America/Chicago"))
london_time=utc_time.astimezone(ZoneInfo("Europe/London"))

print("UTC:",utc_time)
print("IST:",ist)
print("india:",indian_time)
print("Chicago:",chicago_time)
print("london:",london_time)




# enter=datetime.now
# time24 = datetime.strptime(enter,"%I:%M %p").strftime("%H:%M")
# print("output:", time24)
