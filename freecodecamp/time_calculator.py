
# !!! SUCCESS !!!
# !!! BUG ISSUES NEEDS FIXING !!!
# YET TO BE PERFECTED
# LINK https://replit.com/@satanicwizard66/boilerplate-time-calculator#time_calculator.py

def add_time(start, duration, day=None):


    ampm_list = ["AM", "PM"]
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    daysLater = ""
    newWeekday = ""


    #SPLITS UP PARAMETERS
    poop = start.split(' ')
    start_section = poop[0].split(':')
    duration_section = duration.split(':')
    ampm = poop[1]
    
    
    #ORGANIZES AND STORES HOURS AND MINUTES
    start_hours = int(start_section[0])
    start_minutes = int(start_section[1])
    d_hours = int(duration_section[0])
    d_minutes = int(duration_section[1])

    #ADDS HOURS AND MINUTES
    sum_hours = start_hours + d_hours
    sum_minutes = start_minutes + d_minutes


    #LOGIC AND CALCULATIONS
    new_minutes = (sum_minutes) % 60 #converts minutes
    if new_minutes < 10:
        new_minutes = "0" + str(new_minutes)
    new_hours = (sum_hours % 12) + (sum_minutes > 59) #adds hour if necessary
    if new_hours == 0:
        new_hours = 12


    #LOGIC OF DAYS AND HALF DAYS AM PM
    half_of_day = (sum_hours + (sum_minutes > 59)) // 12

    ampm = ampm_list.index(ampm)
    new_ampm = ampm_list[(ampm + (half_of_day % 2)) % 2]

    if half_of_day > (3 - ampm): # 1.5 days passed for pm OR 2 days for am == more than one day later
      daysLater = f" ({(half_of_day + ampm) // 2} days later)"
    elif half_of_day > (1 - ampm): # half a day passed for pm OR 1 day for am == next day
      daysLater = " (next day)"

    if (day):
      oldDayIndex = days_of_week.index(day.lower().capitalize())
      # (halfDays + ampm) // 2 == the number of full days passed
      newDayIndex = (oldDayIndex + (half_of_day + ampm) // 2) % 7
      newWeekday = f", {days_of_week[newDayIndex]}"
 

    new_time = f"{new_hours}:{new_minutes} {new_ampm}{newWeekday}{daysLater}"
    return new_time


print(add_time('11:06 PM', '2:02', 'Monday'))