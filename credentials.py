import base64

class Credentials(object):

    def __init__(self):
        self.fromAd = 'moremail@mail.stuff'
        self.username = 'email@email.com'
        self.password = 'enunga,enganga'
        self.server = 'server:556'

    def getpassword(self):
        return base64.b64decode(self.password)
