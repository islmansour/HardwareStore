# from django_cron import CronJobBase, Schedule
import firebase_admin
from firebase_admin import credentials, messaging

from IraqiStore.models import CronTest, Notification, User, LOV, NotificationRecipient

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


def getNotificationText(msgCode, locale):
    _msgText = ''
    try:
        _msg = LOV.objects.filter(type='CRON_NOTIFICATION').filter(
            language=locale).filter(name=msgCode)[0]

        _msgText = _msg.value
    except Exception as inst:
        _msgText = '*** Error retreiving notification text by code (cron.py:getNotificationText)'
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)
    return _msgText

# sending notifications:
#   Whenever there is a notification, we add a record to the Notification enity, e.g creating News will trigger a notification to all
#   Users.
#   The process will loop for all notificaiton that were NOT sent yet, then loop for all users and sends the notification to them. The process
#   takes into consideration the selected lannguage for the user, and uses the getNotificationText function to find the Text to be sent to the
#   user based on the language.
#   We then update the notification flag "Sent" to true;


def my_scheduled_job():

    qnotification_set = Notification.objects.filter(sent=False)
    for notification in qnotification_set.iterator():
        if notification.token is None or notification.token == "":
            try:
                user_set = User.objects.filter(active=True)
                tokensAr = []
                tokenEn = []
                tokenHe = []
                msgAr = getNotificationText(
                    notification.message, 'ar')
                msgHe = getNotificationText(
                    notification.message, 'he')
                msgEn = getNotificationText(
                    notification.message, 'en')
                for _user in user_set:
                    if _user.admin == True:
                        pass
                    elif _user.language == "ar":
                        NotificationRecipient.objects.create(
                            messageId=notification.id, recipientId=_user.id, content=msgAr)
                        tokensAr.append(_user.token)
                    elif _user.language == "he":
                        NotificationRecipient.objects.create(
                            messageId=notification.id, recipientId=_user.id, content=msgHe)
                        tokenHe.append(_user.token)
                    elif _user.language == "en":
                        NotificationRecipient.objects.create(
                            messageId=notification.id, recipientId=_user.id, content=msgEn)
                        tokenEn.append(_user.token)

            except Exception as inst:
                print(type(inst))    # the exception instance
                print(inst.args)     # arguments stored in .args
                print(inst)
            sendPush("بلوك عراقي",
                     msgAr, tokensAr)
            sendPush("בלוק עיראקי",
                     msgHe, tokenHe)
            sendPush("Block Iraqi",
                     msgEn, tokenEn)
            notification.sent = True
            notification.save()


def add_text():
    CronTest.objects.create(text='this is text')
