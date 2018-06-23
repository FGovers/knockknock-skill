from mycroft import MycroftSkill, intent_file_handler


class Knockknock(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('knockknock.intent')
    def handle_knockknock(self, message):
        self.speak_dialog('knockknock')


def create_skill():
    return Knockknock()

