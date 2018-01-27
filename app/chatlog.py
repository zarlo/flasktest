class chatlog(object):

    AddlogMethod = None
    GatlogMethod = None

    def Init(Addlog, GetLog):
        chatlog.AddlogMethod = Addlog
        chatlog.GatlogMethod = GetLog

    def AddChatLog(sender, text):
        chatlog.AddlogMethod(sender, text)

    def Getlast20():
        return chatlog.GatlogMethod()
