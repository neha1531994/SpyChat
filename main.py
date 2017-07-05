from detail import spy, Spy, Chatmessage, friends
from steganography.steganography import Steganography
from termcolor import colored
from datetime import datetime


status_messages=["Available","busy","At Work"]
direct=['sos','help','save']
print"Hello! Let\'s get started"

x = "Do you want to continue as " + colored(spy.salutation, 'red') + " " + colored(spy.name, 'red') + " (Y/N)? "
y = raw_input(x)

def status(current_status_message):

    update_status_message=None
    if current_status_message!=None:
        print "your current_status_message is %s\n"%(current_status_message)
    else:
        print "status message is null"
    default=raw_input("Do you want to select from older ones(yes/no)")
    if default=="no":
        new_status_message=raw_input("what is your message")
        if len(new_status_message)>0:
            status_messages.append(new_status_message)
            update_status_message=new_status_message
            status_messages.append(update_status_message)
    elif default=="yes":
        item_position=1
        for message in status_messages:
            print "%d  %s"%(item_position,message)
            item_position=item_position+1
        message_selection=int(raw_input("\nchoose from above message"))
        if len(status_messages)>=message_selection:
            update_status_message=status_messages[message_selection-1]
    else:
        print "invalid option"
    if update_status_message:
        print "your update status message is:%s" %(update_status_message)
        return update_status_message
    else:
        print "you didn't update your status message"
        print update_status_message



# FRIEND_LIST FUNCTION #
def friend_list():
    friend=Spy('','',0,0)
    friend.name= raw_input("friend_name")
    friend.rating = float(raw_input("rating"))
    friend.age= int(raw_input("age"))
    friend.salutation=raw_input("Mr or Miss")
    if len(friend.name)>0 and friend.age>=12:
        print "%s %s is now your friend"%(friend.salutation,friend.name)
        friends.append(friend)

    else:
        print "Not Valid"
    return len(friends)



# selection function #
def select_friend():
    #print "for select rahul enter 1","for select neha enter 2"
    item_no=0
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_no + 1, friend.salutation, friend.name,
                                                                friend.age,
                                                                friend.rating)
        item_no = item_no + 1
    friend_choice=raw_input("choose friend from list?")
    friend_choice_position=int(friend_choice)-1
    return friend_choice_position


#read chat history
def read_chat_history():
   read_for = select_friend()
   for chat in friends[read_for].chats:
       b=colored(chat.time.strftime('%A,%d %B %Y %H:%M:%S'),'blue')
       if chat.sent_by_me:
         print'[%s] %s: %s' % (b,'you said:',chat.message)
       else:
         print '[%s] %s read:%s'%(b,friends[read_for].name,chat.message)


#send a message
def send_message():
    friend_choice=select_friend()
    origional_image= raw_input("what is the name of the image")
    output_path="output.jpg"
    text=raw_input("what do you want to say")
    Steganography.encode(origional_image,output_path,text)
    new_chat=Chatmessage(text,True)
    friends[friend_choice].chats.append(new_chat)
    print "Your secret message image is ready!"



#Read a message
def read_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    if len(secret_text) == 0:
        print "No secret mesage"
    else:
        temp = secret_text.split()
        for i in direct:
            if i in temp:
                temp[temp.index(i)] = "help me"
        secret_text = str.join(" ", temp)
        if len(temp) > 100:
            del friends[sender]
            print 'Message length exceeded. Message was not saved.'
            print 'Your friend is deleted'
        else:
            new_chat = Chatmessage(secret_text, False)
            friends[sender].chats.append(new_chat)
            print "Your secret message has been saved"


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome " + colored(spy.name,'red') + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = status(spy.current_status_message)
                elif menu_choice == 2:
                    number_of_friends = friend_list()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if y.upper() == "Y":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'











