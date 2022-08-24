from django.shortcuts import render
from django.http import HttpResponse

from .models import stock_deal

import twstock
from datetime import datetime

# Create your views here.


def home(request):
    """

    type->str

    float(
        twstock.realtime.get("2330")["realtime"]["latest_trade_price"]
        )
    --> current trade price

    """

    deals = stock_deal.objects.all()


    for deal in deals:

        try:
            current_price = \
            round(
                float(twstock.realtime.get(deal.company_code)["realtime"]["latest_trade_price"]),
                2)

        except:
            print("log: error while convert {} to float".format(twstock.realtime.get(deal.company_code)["realtime"]["latest_trade_price"]))
            current_price = 0


        deal.current_price = current_price
        deal.profit_and_loss = round(
            (current_price - deal.bought_price) * deal.share,
            2)
        
        duration = datetime.now().date() - deal.bought_date
        deal.duration = duration.days

        deal.save()


    return render(request, "home.html", {
        "deals": deals
        })

def history(request):



    return render(request, "history.html")
