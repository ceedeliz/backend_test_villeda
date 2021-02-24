import os
import getopt
import json
import slack

from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from datetime import date

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
)


from .tasks import sleepy, slack_task, catch_data, reminder
from applications.orders.models import Order
from applications.menu.models import Menu
from applications.meals.models import Meal


manage_msg = []
# Create your views here.
def index(request):
    return render(request,"example/home.html",{})

def msj(request):
    #data = json.loads("""{"type": "section", "text": {"type": "plain_text", "text": "desde views"}}""")
    data = """
            		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Section block with radio buttons"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": true
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": true
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": true
						},
						"value": "value-2"
					}
				],
				"action_id": "radio_buttons-action"
			}
		}
           """
    slack_task.delay(json.loads(data))
    print("------------")
    print("finish")

    return HttpResponse(status=200)

@csrf_exempt
def event_hook(request):
    def compare_input(req):
        req = req.split(' ')
        num = req[0]
        try:
            isinstance(int(num), int)
            print("eleccion de menu")
            return True
        except:
            print("detalles de menu")
            return False

    client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    json_dict = json.loads(request.body.decode('utf-8'))
    BOT_ID = client.api_call("auth.test")['user_id']

    if json_dict['token'] != settings.VERIFICATION_TOKEN:
        return HttpResponse(status=403)
    if 'type' in json_dict:
        if json_dict['type'] == 'url_verification':
            response_dict = {"challenge": json_dict['challenge']}
            return JsonResponse(response_dict, safe=False)
    if 'event' in json_dict:
        event_msg = json_dict['event']
        if ('subtype' in event_msg) and (event_msg['subtype'] == 'bot_message'):
            return HttpResponse(status=200)

    if event_msg['type'] == 'message':
        user = event_msg['user']
        message = event_msg['text']
        print(json_dict['event'])
        channel = event_msg['channel']
        response_msg = ":wave:, Hello <@%s>" % user
        
        if(BOT_ID != user):
            eleccion = compare_input(message)
            if(len(manage_msg) == 0):
                manage_msg.append(message)
                response_msg = "Hola!, selecciona el numero del platillo de tu preferencia"
            elif(len(manage_msg) == 1):
                try:
                    isinstance(int(message), int)
                    manage_msg.append(message)
                    response_msg = ("Si te gustaría especificar algunos detalles por favor escribelos a continuación."
                                    " De lo contrario escribe 'sin' para terminar el pedido")
                except:
                    response_msg = "La elección es incorrecta, intenta de nuevo, unicamente con el número del platillo"
            elif(len(manage_msg) == 2):
                    Order.objects.create(user=user, details='detalles de menu', meal_id='1877d6b5-a2bc-41b2-b604-a15f2cd9080c')
                    response_msg = "Gracias por elección, orden recibida"                
                    del manage_msg[:]


            client.chat_postMessage(channel=channel, text=response_msg)
            print(manage_msg)
            return HttpResponse(status=200)
    return HttpResponse(status=200)

def send_reminder(request):
    menuData = Menu.objects.filter(day__gte=date.today()).order_by('-created')[:1]
    menu_id = menuData[0].id
    menu_desc = menuData[0].description + " "
    print(menu_id)
    orderData = Meal.objects.filter(menu_id__id=menu_id)
    meals = ""
    for order in orderData:
        meals += order.description + " "

    msg = menu_desc + " " + meals
    print(msg)
    response = reminder.delay(msg,"in 2 minutes")
    return HttpResponse(response)
    