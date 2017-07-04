from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class Chatmessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Neha', 'Ms', 20, 4.5)

friend_one = Spy('Neha', 'Ms.', 2.5, 37)
friend_two = Spy('Riya', 'Ms.', 4.2, 27)
friend_three = Spy('No', 'Dr.', 3.5, 17)


friends = [friend_one, friend_two, friend_three]


