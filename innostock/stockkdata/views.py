from django.shortcuts import render

# Create your views here.


from django.http import  HttpResponse
from django.shortcuts import redirect,render
from   registeration.models import User
from .models import CompanyUpdate,CorpAction,BoardMeeting,AGM_EGM,Result,SAST,NewListing,ListOfCompanies,NewFilter


def home(request):
    # print("home")
    if(request.user.is_authenticated):
        list_of_companies=ListOfCompanies.objects.all()
        extra_filters=NewFilter.objects.all()

        return render(request,'stockdata/home.html',{"companies":list_of_companies,"filters":extra_filters})
    else:
        return redirect("/login/")


def owner(request):
    if(request.user.is_authenticated):
        return render(request,"stockdata/admin_site.html",{})
    else:
        return  redirect("/login/")


def search(request):
    if(request.user.is_authenticated):
        # print(request.POST['filter1'])
        list_of_companies=ListOfCompanies.objects.all()
        extra_filters=NewFilter.objects.all()
        result=[]
        if(request.method=="GET"):

            company=request.GET['filter1']
            category_name=request.GET['filter2']
            print(category_name)
            extra_filter=request.GET['filter3']
            print((extra_filter) in extra_filter)
            if (category_name == "Company Update"):
                result=CompanyUpdate.objects.filter(company__security_name=company)


            elif (category_name == "AGM/EGM"):
                result = AGM_EGM.objects.filter(company__security_name=company)

            elif (category_name == "Result"):
                result = Result.objects.filter(company__security_name=company)

            elif (category_name == "Corp. Action"):
                result = CorpAction.objects.filter(company__security_name=company)

            elif (category_name == "Board Meeting"):
                result = BoardMeeting.objects.filter(company__security_name=company)

            elif (category_name == "Insider Trading / SAST"):
                result = SAST.objects.filter(company__security_name=company)

            elif (category_name == "New Listing"):
                result = NewListing.objects.filter(company__security_name=company)
            if (extra_filter != ""):

                result_with_filter = []

                for data in result:
                    if (extra_filter in data.title):
                        result_with_filter.append(data)

                result = result_with_filter

        return render(request,"stockdata/home.html",{"result":result,"companies":list_of_companies,"filters":extra_filters})
    else:
        return  redirect("/login/")


def admin_site(request):
    if(request.user.is_authenticated):
        message=""
        if(request.method=="POST"):
            filter=request.POST['filter']
            new_filter=NewFilter(name=filter)
            new_filter.save()
            message="New filter added"
        return render(request,"stockdata/admin_site.html",{"message":message})