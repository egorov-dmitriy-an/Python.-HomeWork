from datetime import datetime as dt

def request_contact_logger(data, sensor):
    time = dt.now().strftime('%H:%M')
    if sensor == 2:
        with open('log_seminar_7.csv', 'a') as file:
            file.write('{};Add contact;{}\n'
                        .format(time, data))
    elif sensor == 1:
        with open('log_seminar_7.csv', 'a') as file:
            file.write('{};Find contact;{}\n'
                        .format(time, data))
                        