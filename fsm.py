from transitions.extensions import GraphMachine

name = []

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '/newbot'

    def is_going_to_state2(self, update):
        text = update.message.text
        return 1

    def is_going_to_state3(self, update):
        text = update.message.text
        name.append(text)
        return 1

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '/start'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '/mybots'

    def on_enter_state1(self, update):
        update.message.reply_text("Alright, a new bot. How are we going to call it? Please choose a name for your bot.")
        # self.go_back(update)
    def on_exit_state1(self, update):
        print('Leaving state1')  

    def on_enter_state2(self, update):
        update.message.reply_text("Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.")
        # self.go_back(update)
    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("Done! Congratulations on your new bot. ")
        self.go_back(update)
    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual.\nYou can control me by sending these commands:\n/newbot - create a new bot\n/mybots - show your bots ")
        self.go_back(update)
    def on_exit_state4(self, update):
        print('Leaving state4')  

    def on_enter_state5(self, update):
        text = 'Your bots:\n'
        for e in name:
            text = text + e + '\n'
        update.message.reply_text(text)
        self.go_back(update)
    def on_exit_state5(self, update):
        print('Leaving state6') 
