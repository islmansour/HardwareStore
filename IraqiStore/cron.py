from django_cron import CronJobBase, Schedule
import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate(
    "./pdfs/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def sendPush(title, msg, registration_token, dataObject=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)


class news_notify(CronJobBase):
    RUN_EVERY_MINS = 2  # every 1 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'IraqiStore.my_scheduled_job'    # a unique code

    def do(self):
        print('cron running..')
        tokens = ["dwyJ-fW-Lkteo3nSn8mdSu:APA91bG2yzQJeEtXJU8tM4utv91Xse_2w4IQ86Gz3v68QQ0GXTCZFgruBxIEDS2BVSBfiZ_NNf__U9Rdk63SRV7OssFeSiDo_nFub9cuGHcjRKZmn8yZFvSrXQHqENaiZk8W2k5slVwi"]
        sendPush("Hi", "This is my next msg", tokens)


def my_scheduled_job():
    tokens = ["dwyJ-fW-Lkteo3nSn8mdSu:APA91bG2yzQJeEtXJU8tM4utv91Xse_2w4IQ86Gz3v68QQ0GXTCZFgruBxIEDS2BVSBfiZ_NNf__U9Rdk63SRV7OssFeSiDo_nFub9cuGHcjRKZmn8yZFvSrXQHqENaiZk8W2k5slVwi"]
    sendPush("Hi", "This is my next msg", tokens)
    raise Exception("testing cron error")
