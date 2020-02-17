from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler

class Test(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.intent')
    def handle_test(self, message):
        
        #request api code
        
        sensor_unit = message.data.get('sensor')
        self.speak_dialog('test', {'sensor':sensor_unit})


def create_skill():
    return Test()

