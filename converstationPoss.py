# Importing Neccessary Packages
import os, operator, turtle, tkinter
from time import sleep
from conversationFlow import *
from Save import *
import Alex

# The Function
def execute(userInput):
    ui = userInput.lower()
    # Changing I'm/im to I am
    if (ui == "i'm"):
        ui = "i am"
    elif (ui == "im"):
        ui = "i am"
    # WHO WHAT WHEN WHERE WHY HOW
    if (ui[0] == "who"):
        who.execute(ui)
        return reply
    elif (ui[0] == "what"):
        what.execute(ui)
        return reply
    elif (ui[0] == "when"):
        when.execute(ui)
        return reply
    elif (ui[0] == "where"):
        where.execute(ui)
        return reply
    elif (ui[0] == "why"):
        why.execute(ui)
        return reply
    elif (ui[0] == "how"):
        how.execute(ui)
        return reply
    # Action (DO, WILL)
    elif (ui[0] == "do"):
        do.execute(ui)
        return reply
    elif (ui[0] == "will"):
        will.execute(ui)
        return reply
    # GREETINGS (HELLO, HI, HEY, SU[
    elif (ui[0] == "hello"):
        greeting.execute(ui)
        return reply
    elif (ui[0] == "hi"):
        greeting.execute(ui)
        return reply
    elif (ui[0] == "hey"):
        greeting.execute(ui)
        return reply
    elif (ui[0] == "sup"):
        greeting.execute(ui)
        return reply
    # I'm
    elif (ui == "i am"):
        im.execute(ui)
        return reply
    
    
    
    
    
    