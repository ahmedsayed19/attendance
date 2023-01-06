from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Attendance, AttendanceAction, serialize_actions_per_employee_UTC, get_hours_minutes, calc_duration_for_emp



@api_view(['GET'])
def employee_day_attendance(request, employee, date):
    attended_employee = Attendance.objects.filter(employee_code=employee, date=date).first()
    

    if attended_employee is None:
        return Response({'attended': False})

    actions = AttendanceAction.objects.filter(employee=attended_employee).order_by('-action_time')

    delta = calc_duration_for_emp(actions)
    
    context = {
        'duration': get_hours_minutes(delta),
        'attended': True
    }

    return Response(context ,status=status.HTTP_200_OK)



@api_view(['GET'])
def employee_history(request, employee):
    # employee_id = Attendance.objects.get(employee_code=employee) 
    queryset = AttendanceAction.objects.select_related('employee').filter(employee__employee_code=employee)

    context = serialize_actions_per_employee_UTC(queryset)
    
    return Response(context, status=status.HTTP_200_OK)