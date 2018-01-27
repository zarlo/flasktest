class mem(object):

    log = []

    def __init__():
        mem.log = ['test:log']

    def AddChatLog(sender, text):
        mem.log.append(sender + ":" + text)

    def Getlast20():
        output = ""
        for item in mem.log:
            output += '<li>' + item + '</li>'

        return output
