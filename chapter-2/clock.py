current_time = input("what time is it now?")
wait_time = input("how many hours do you want to set the alarm for?")
current_time_int =int(current_time)
wait_time_int = int(wait_time)
alarm_time = (current_time_int + wait_time_int) % 12 
print(alarm_time)