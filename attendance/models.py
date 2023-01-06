from datetime import datetime, time, timedelta
from django.db import models




# Create your models here.
class Attendance(models.Model):
    employee_code = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self) -> str:
        return self.employee_code + '\t' + str(self.date)


class AttendanceAction(models.Model):

    CHECKIN = 'CheckIn'
    CHECKOUT = 'CheckOut'
    ACTION_CHOICES = [
        (CHECKIN, 'Check In'),
        (CHECKOUT, 'Check Out'),
    ]

    action_time = models.DateTimeField()
    action = models.CharField(choices=ACTION_CHOICES, max_length=8)
    employee = models.ForeignKey(Attendance, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.employee) 


# Utilities 

def calc_duration_for_emp(actions):
    delta=timedelta()
    isCheckIn = False
    checkin = None
    for q in actions:
        if q.action == 'CheckIn' and not isCheckIn:
            checkin = q.action_time
            isCheckIn = True
        
        elif q.action == 'CheckOut' and isCheckIn:
            delta += checkin - q.action_time
            isCheckIn = False
        
        elif q.action == 'CheckOut' and not isCheckIn:
            delta += datetime.combine(datetime.combine(q.action_time.date(), q.action_time.time() - q.action_time.date(), time(00,00))) 

    if isCheckIn:
        action_date, action_time = actions.first().action_time.date(), actions.first().action_time.time()
        delta += datetime.combine(action_date, time(23,59,59)) - datetime.combine(action_date, action_time) 
        delta += timedelta(seconds=1)

    return delta


def get_hours_minutes(t):
    s = t.seconds
    h = s // 3600
    m = (s - (h*3600)) // 60
    return "{:d}:{:02d}".format(h, m)


def serialize_actions_per_employee_UTC(queryset):
    data = {}
    for q in queryset:
        if q.employee.date in data:
            data[q.employee.date].append({
                'action': q.action,
                'time': (q.action_time - timedelta(hours=2)).isoformat()
            })
        else:
            data[q.employee.date] = [{
                'action': q.action,
                'time': (q.action_time - timedelta(hours=2)).isoformat()
            }]


    context = {
        'days': [
            {'date':k, 'action': v} for k, v in data.items()
        ]
    }

    return context