from datetime import datetime, timedelta
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

def calc_duration_for_emp(queryset):
    print('Im in calc')
    delta=timedelta()
    isCheckIn = True
    checkin = None
    # checkin = datetime()
    for q in queryset:
        print(q.action, q.action_time)
        if q.action == 'CheckIn' and isCheckIn:
            checkin = q.action_time
            isCheckIn = False
        
        elif q.action == 'CheckOut' and not isCheckIn:
            delta += checkin - q.action_time
            isCheckIn = True

        print(delta.seconds)
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