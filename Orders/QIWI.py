from django.conf import settings
from extra_settings.models import Setting
from pyqiwip2p import QiwiP2P

def get_QIWI_p2p():
    # QIWI payments
    try:
        p2p = QiwiP2P(auth_key=Setting.get("QIWI_PRIVATE_KEY"))
    except:
        try:
            print("\n[!] SET QIWI_PRIVATE_KEY SETTING IN Settings or .env.prod FILE!!!\n")
            p2p = QiwiP2P(auth_key=settings.QIWI_PRIVATE_KEY)
        except:
            p2p = False
    
    return p2p
