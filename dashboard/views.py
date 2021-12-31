from django.shortcuts import render
from .models import Vehicle_Data, sjs_dailyprofit
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth

# Create your views here.

res = 0


def index(request):
    return render(request, 'index.html')


def data_page(request):
    today = datetime.today().date()
    if(request.method == "POST"):
        vno = request.POST['vno']
        #date = request.POST['date']
        date = today
        vehicle_wash = request.POST["vehicle"]
        vehicle_amount = request.POST["amount"]
        payment_type = request.POST["payment"]
        data_obj = Vehicle_Data(vehicle_no=vno, vehicle_arrived_date=date, vehicle_wash=vehicle_wash,
                                vehicle_amount=vehicle_amount, payment_type=payment_type)
        data_obj.save()
        global res
        res = 1

        profit_today_innersql = "SELECT id,vehicle_amount  FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' ".format(
            date)
        profit_today_outersql = Vehicle_Data.objects.raw(profit_today_innersql)
        profit_today = 0
        for i in profit_today_outersql:
            profit_today += i.vehicle_amount

        sjs_dailyprofit_obj = sjs_dailyprofit.objects.all()
        sql_len = sjs_dailyprofit_obj.__len__()
        if(sql_len == 0):
            sjs_dailyprofit_obj = sjs_dailyprofit(
                dialy_date=date, dialy_profit=profit_today)
            sjs_dailyprofit_obj.save()
        if(sql_len > 0):
            if(sjs_dailyprofit.objects.filter(dialy_date=date).exists()):
                obj = sjs_dailyprofit.objects.get(dialy_date=date)
                print("Profit is:", obj.dialy_profit)
                obj.dialy_profit = profit_today
                print("Profit is:", obj.dialy_profit)
                obj.save()
            else:
                sjs_dailyprofit_obj = sjs_dailyprofit(
                    dialy_date=date, dialy_profit=profit_today)
                sjs_dailyprofit_obj.save()

        return HttpResponseRedirect('data_page')
#        return render(request, 'bill_page.html', {'vno': vno, 'date': date, 'vehicle_wash': vehicle_wash, 'vehicle_amount': vehicle_amount, 'payment_type': payment_type})

#        return render(request, 'final_page.html', {'bodywash_count_today': bodywash_count_today, 'fullwash_count_today': fullwash_count_today, 'jcb_count_today': jcb_count_today, 'crane_count_today': crane_count_today, 'handcash_count_today': handcash_count_today, 'digitalcash_count_today': digitalcash_count_today, 'profit_today': profit_today})

    else:
        return render(request, 'data_page.html')


def bill_page(request):
    all_vehicle_data = Vehicle_Data.objects.all()
    return render(request, 'bill_page.html', {'all_vehicle_data': all_vehicle_data})


def login_page(request):
    if(request.method == "POST"):
        uname = request.POST["username"]
        passw = request.POST["password"]

        user = auth.authenticate(username=uname, password=passw)
        if user is not None:
            auth.login(request, user)
            print(user)
            today = datetime.today().date()
            bodywash_count_today_innersql = "SELECT * FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and vehicle_wash = 'Body Wash' ".format(
                today)
            bodywash_count_today_outersql = Vehicle_Data.objects.raw(
                bodywash_count_today_innersql)
            bodywash_count_today = bodywash_count_today_outersql.__len__()

            fullwash_count_today_innersql = "SELECT * FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and vehicle_wash = 'Full Wash' ".format(
                today)
            fullwash_count_today_outersql = Vehicle_Data.objects.raw(
                fullwash_count_today_innersql)
            fullwash_count_today = fullwash_count_today_outersql.__len__()

            jcb_count_today_innersql = "SELECT * FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and vehicle_wash = 'jcb' ".format(
                today)
            jcb_count_today_outersql = Vehicle_Data.objects.raw(
                jcb_count_today_innersql)
            jcb_count_today = jcb_count_today_outersql.__len__()

            crane_count_today_innersql = "SELECT * FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and vehicle_wash = 'crane' ".format(
                today)
            crane_count_today_outersql = Vehicle_Data.objects.raw(
                crane_count_today_innersql)
            crane_count_today = crane_count_today_outersql.__len__()

            handcash_count_today_innersql = "SELECT * FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and payment_type = 'Hand Cash' ".format(
                today)
            handcash_count_today_outersql = Vehicle_Data.objects.raw(
                handcash_count_today_innersql)
            handcash_count_today = handcash_count_today_outersql.__len__()

            digitalcash_count_today_innersql = "SELECT * FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and payment_type = 'Digital Cash' ".format(
                today)
            digitalcash_count_today_outersql = Vehicle_Data.objects.raw(
                digitalcash_count_today_innersql)
            digitalcash_count_today = digitalcash_count_today_outersql.__len__()

            pending_count_today_innersql = "SELECT * FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and payment_type = 'Pending' ".format(
                today)
            pending_count_today_outersql = Vehicle_Data.objects.raw(
                pending_count_today_innersql)
            pending_count_today = pending_count_today_outersql.__len__()

            profit_today_innersql = "SELECT id,vehicle_amount  FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' ".format(
                today)
            profit_today_outersql = Vehicle_Data.objects.raw(
                profit_today_innersql)
            profit_today = 0
            for i in profit_today_outersql:
                profit_today += i.vehicle_amount
            print("Today profit is:", profit_today)

            bodywashincome_today_innersql = "SELECT id,vehicle_amount  FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and vehicle_wash='Body Wash' ".format(
                today)
            bodywashincome_today_outersql = Vehicle_Data.objects.raw(
                bodywashincome_today_innersql)
            bodywash_profit_today = 0
            for i in bodywashincome_today_outersql:
                bodywash_profit_today += i.vehicle_amount

            fullwashincome_today_innersql = "SELECT id,vehicle_amount  FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and vehicle_wash='Full Wash' ".format(
                today)
            fullwashincome_today_outersql = Vehicle_Data.objects.raw(
                fullwashincome_today_innersql)
            fullwash_profit_today = 0
            for i in fullwashincome_today_outersql:
                fullwash_profit_today += i.vehicle_amount

            jcbincome_today_innersql = "SELECT id,vehicle_amount  FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and vehicle_wash='jcb' ".format(
                today)
            jcbincome_today_outersql = Vehicle_Data.objects.raw(
                jcbincome_today_innersql)
            jcb_profit_today = 0
            for i in jcbincome_today_outersql:
                jcb_profit_today += i.vehicle_amount

            craneincome_today_innersql = "SELECT id,vehicle_amount  FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and vehicle_wash='crane' ".format(
                today)
            craneincome_today_outersql = Vehicle_Data.objects.raw(
                craneincome_today_innersql)
            crane_profit_today = 0
            for i in craneincome_today_outersql:
                crane_profit_today += i.vehicle_amount

            handcashincome_today_innersql = "SELECT id,vehicle_amount  FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and payment_type='Hand Cash' ".format(
                today)
            handcashincome_today_outersql = Vehicle_Data.objects.raw(
                handcashincome_today_innersql)
            handcash_profit_today = 0
            for i in handcashincome_today_outersql:
                handcash_profit_today += i.vehicle_amount

            digitalcashincome_today_innersql = "SELECT id,vehicle_amount  FROM dashboard_Vehicle_Data where vehicle_arrived_date = '{0}' and payment_type='Digital Cash' ".format(
                today)
            digitalcashincome_today_outersql = Vehicle_Data.objects.raw(
                digitalcashincome_today_innersql)
            digitalcash_profit_today = 0
            for i in digitalcashincome_today_outersql:
                digitalcash_profit_today += i.vehicle_amount

            everyday_profit_obj = sjs_dailyprofit.objects.all()
            everyday_vehicle_obj = Vehicle_Data.objects.all()

            return render(request, 'user_page.html', {'bodywash_count_today': bodywash_count_today,
                                                      'fullwash_count_today': fullwash_count_today,
                                                      'jcb_count_today': jcb_count_today,
                                                      'crane_count_today': crane_count_today,
                                                      'handcash_count_today': handcash_count_today,
                                                      'digitalcash_count_today': digitalcash_count_today,
                                                      'bodywash_profit_today': bodywash_profit_today,
                                                      'fullwash_profit_today': fullwash_profit_today,
                                                      'jcb_profit_today': jcb_profit_today,
                                                      'crane_profit_today': crane_profit_today,
                                                      'handcash_profit_today': handcash_profit_today,
                                                      'digitalcash_profit_today': digitalcash_profit_today,
                                                      'profit_today': profit_today,
                                                      'everyday_profit_obj': everyday_profit_obj,
                                                      'everyday_vehicle_obj': everyday_vehicle_obj,
                                                      'pending_count_today': pending_count_today
                                                      })

        else:
            return HttpResponse("Invalid Credentials")
    else:
        return render(request, 'login.html')


def logout_page(request):
    auth.logout(request)
    return HttpResponseRedirect('data_page')
