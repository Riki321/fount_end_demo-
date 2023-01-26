from django.shortcuts import render
from hackthon.models import Organization,Participants,Venue
from hackthon.forms import OrganizationForms,ParticipantsForms
from django.contrib import messages
from django.http import HttpResponse
from django.db import connection

def HomePage(request):
    return render(request,'HomePage.html')

##Organization
def show_org(request):
    showall = Organization.objects.all()
    return render(request,'show_org.html',{"show_org":showall})

def sort_org(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=Organization.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sort_org.html',context)
    else:
        return render(request,'sort_org.html')



def insert_org(request):
    if request.method=="POST":
        if (request.POST.get('org_id') and request.POST.get('name') 
            and request.POST.get('address') and request.POST.get('org_rating')):
            saverecord=Organization()
            saverecord.org_id=request.POST.get('org_id') 
            saverecord.name=request.POST.get('name')
            saverecord.address=request.POST.get('address')
            saverecord.org_rating=request.POST.get('org_rating')

            allval=Organization.objects.all()
            
            for i in allval:
                if str(i.org_id)==str(request.POST.get('org_id')):
                    messages.warning(request,'Organization already exists....!');
                    return render(request,'insert_org.html')

            saverecord.save()
            messages.success(request,'Organization '+saverecord.org_id+' '+saverecord.name+' is saved succesfully!!')
            return render(request,'insert_org.html')
            # saverecord.save()
            # messages.success(request,'Game '+saverecord.game_name+' is saved succesfully!!')
            # return render(request,'insertGame.html')
    else:
            return render(request,'insert_org.html')


def edit_org(request,id):
    edit_org_obj=Organization.objects.get(org_id=id)
    context={
        "org":edit_org_obj
    }
    return render(request,'edit_org.html',context)


def update_org(request,id):
    update_org=Organization.objects.get(org_id=id)
    form=OrganizationForms(request.POST,instance=update_org)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'edit_org.html',{"org":update_org})


def del_org(request,id):
    delGameObj=Organization.objects.get(org_id=id)
    context={
        "org":delGameObj
    }
    return render(request,'del_org.html',context)

def deleted_org(request,id):
    delGameObj=Organization.objects.get(org_id=id)
    delGameObj.delete()
    show_all=Organization.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    return render(request,'del_org.html',{"org": show_all})
def runQueryorg(request):
    raw_query = "select * from \"Organization\" where org_rating<(select avg(org_rating) from \"Organization\");"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()

    return render(request,'runQueryorg.html',{'data':alldata})
def custom_query(request):
    custom_query=request.POST.get("custom_query")
    print(custom_query)
    #raw_query = "select * from \"Organization\" where org_rating=1;"

    cursor = connection.cursor()
    cursor.execute(custom_query)
    alldata=cursor.fetchall()

    return render(request,'runQueryorg.html',{'data':alldata})

def run_query(request):

    return render(request,'custom_query.html',{})





##Participants:
def show_part(request):
    showall=Participants.objects.all()
    context = {
        'data': showall
    }
    return render(request,'show_part.html',context)

def insert_part(request):
    if request.method=="POST":
        if (request.POST.get('part_id') and request.POST.get('first_name') and request.POST.get('middle_name') 
        and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('mobile_no') and 
        request.POST.get('address') and request.POST.get('role') and request.POST.get('gender') and 
        request.POST.get('country') and request.POST.get('disability')):
            saverecord=Participants()
            saverecord.part_id=request.POST.get('part_id') 
            saverecord.first_name=request.POST.get('first_name')
            saverecord.middle_name=request.POST.get('middle_name')
            saverecord.last_name=request.POST.get('last_name')
            saverecord.email=request.POST.get('email')
            saverecord.mobile_no=request.POST.get('mobile_no')
            saverecord.address=request.POST.get('address')
            saverecord.role=request.POST.get('role')
            saverecord.gender=request.POST.get('gender')
            saverecord.country=request.POST.get('country')
            saverecord.disability=request.POST.get('disability')

            allval=Participants.objects.all()
            
            for i in allval:
                if str(i.part_id)==str(request.POST.get('part_id')):
                    messages.warning(request,'Participants already exists....!');
                    return render(request,'insert_part.html')

            saverecord.save()
            messages.success(request,'Participants '+saverecord.part_id+' '+saverecord.first_name+' is saved succesfully!!')
            return render(request,'insert_part.html')
    else:
            return render(request,'insert_part.html')


def sort_part(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=Participants.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sort_part.html',context)
    else:
        return render(request,'sort_part.html')


def edit_part(request,id):
    edit_part_Obj=Participants.objects.get(part_id=id)
    context={
        "part":edit_part_Obj
    }
    return render(request,'edit_part.html',context)


def update_part(request,id):
    update_part=Participants.objects.get(part_id=id)
    form=ParticipantsForms(request.POST,instance=update_part)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'edit_part.html',{"part":update_part})

def del_part(request,id):
    del_part_Obj=Participants.objects.get(part_id=id)
    context={
        "part":del_part_Obj
    }
    return render(request,'del_part.html',context)

def deleted_part(request,id):
    delCusObj=Participants.objects.get(part_id=id)
    delCusObj.delete()
    showall=Participants.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    return render(request,'del_part.html',{"part": showall})


def runQuerypart(request):
    raw_query = "select * from \"Participants\" where gender=\'Male\';"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()

    return render(request,'runQuerypart.html',{'data':alldata})

def custom_query1(request):
    custom_query=request.POST.get("custom_query1")
    print(custom_query1)
    #raw_query = "select * from \"Organization\" where org_rating=1;"

    cursor = connection.cursor()
    cursor.execute(custom_query1)
    alldata=cursor.fetchall()

    return render(request,'runQuerypart.html',{'data':alldata})


def run_query1(request):

    return render(request,'custom_query1.html',{})