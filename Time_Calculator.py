def add_time(start, duration,day=None):
    L=start.split(":")
    hours=int(L[0])
    M=L[1].split(" ")
    minutes=int(M[0])
    zone=M[1]
    if zone=="PM" and hours!=12:
        hours+=12
    if zone=="AM" and hours==12:
        hours=0
    D=duration.split(":")
    hours+=int(D[0])
    minutes+=int(D[1])
    if minutes>=60:
        minutes-=60
        hours+=1
    total_hours=hours
    if total_hours % 24 < 12:
        zone = "AM"
    else:
        zone = "PM"
    hours=total_hours%12
    if hours==0:
        hours=12
    total_days=total_hours//24
    d=''
    if total_days==1:
        d+="(next day)"
    elif total_days>1:
        d+=f'({total_days} days later)'
    next_day=''
    if day:
        days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        start_day_index = days.index(day.capitalize())
        next_day_index = (start_day_index + total_days) % 7
        next_day = days[next_day_index]
    hours_str=str(hours)
    minutes_str=str(minutes).zfill(2)#adds trailing zeros till the needed amount of length is not reached
    new_time=''
    new_time+=hours_str+":"
    new_time+=minutes_str+" "
    new_time+=zone
    if day:
        new_time+=", "+next_day
        if d:
            new_time+=' '+d
    elif d:
        new_time+=' '+d
    return new_time
print(add_time('11:59 PM', '24:05','Monday'))
