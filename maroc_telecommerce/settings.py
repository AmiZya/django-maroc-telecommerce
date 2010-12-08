from django.conf import settings

GATEWAY_URL = ""
#GATEWAY_TEST_URL = u"http://shopping.maroctelecommerce.com/test/gateway/paiement.asp"

GATEWAY_TEST_URL = settings.MT_URL

STORE_ID = settings.MT_STORE_ID
SECRET = settings.MT_SECRET
LANG = getattr(settings, "MT_LANG", "EN")
