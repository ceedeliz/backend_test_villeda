import urllib.request

from celery import shared_task
from time import sleep

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from backend_test.celery import app as celery_app

from celery.utils.log import get_task_logger
#CAMBIAR ESTE PEDO AQI from .models import Foo

logger = get_task_logger(__name__)

@celery_app.task
def sleepy(duration):
    logger.info("Send welcome email")
    sleep(duration)
    return None

@celery_app.task
def catch_data():
    foo_instance = Foo.objects.create(name='test')
    return None

@celery_app.task
def reminder(menu,date):
    #url = "https://slack.com/api/reminders.add?token=xoxp-1798524260176-1774887462787-1782591065316-84dcfd25d8f8a3a97c387b13dc12e622&text=el menu de hoy&time=in 2 minutes"
    url = "https://slack.com/api/reminders.add?token=xoxp-1798524260176-1774887462787-1782591065316-84dcfd25d8f8a3a97c387b13dc12e622&text={}&time={}".format(menu,date)
    url = url.replace(" ","%20")
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("hola")
        print(html)
    return None

@celery_app.task
def slack_task(data):
    print("adios")
    client = WebClient(token="xoxb-1798524260176-1767941888982-HIbfiJWGPhhvx70gxmdLSuMt")

    json = data

    try:
        response = client.chat_postMessage(channel='#test', blocks=[json])
        print("el mensaje se envio correctamente")
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
    return None
