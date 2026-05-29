from django.shortcuts import render

def employee_list(request):

    employees = [
        {'name':'Rahul','job_title':'Developer','salary':50000,'full_time':True},
        {'name':'Aisha','job_title':'Designer','salary':30000,'full_time':False},
    ]

    return render(request,'index.html',{'employees':employees})