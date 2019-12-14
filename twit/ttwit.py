from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
import json
from playsound import playsound
from random import choice
from tweepy.streaming import StreamListener
from tkinter import *
import tkinter.ttk as ttk

inst={
    'violin':['v1.wav','v2.wav','v3.wav','v4.wav','v5.wav'],
    'guitar':['g1.wav','g2.wav','g3.wav','g4.wav'],
    'drum':['b1.wav','b2.wav']
}

pannels = dict()
defaultbg = None

with open('keys.txt','r') as f:
    keys = json.load(f)

class StdOutListener( StreamListener ):

    def __init__( self ):
        self.tweetCount = 0

    def on_connect( self ):
        print("Connection established!!")

    def on_disconnect( self, notice ):
        print("Connection lost!! : ", notice)

    def on_data( self, status ):
        tw=json.loads(status)['text']
        print(tw, flush=True)
        for i,j in inst.items():
            pannels[i][1].configure(bg=defaultbg)
            if i in tw.lower():
                playsound('snd/'+choice(j),block=False)
                try: # this is needed to handle encoding not supported by Tcl
                    pannels[i][1].configure(text=tw)
                    pannels[i][1].configure(bg='green')
                except:
                    pass
        return True

    def on_error( self, status ):
        print(status)

def main():
    global defaultbg

    win = Tk()
    win.title("TwiSound")
    win.geometry("1000x300")

    for i,k in enumerate(inst.keys()):
        box = ttk.LabelFrame(win,text=k,height=300,width=300)
        box.grid(column=i,row=0,padx=10)
        box.pack_propagate(0)
        txt = Label(box,wraplength=290,font=('Segoe UI',14))
        txt.pack()
        pannels[k] = (box,txt)

    defaultbg = txt['bg']

    auth = OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.secure = True
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = API(auth)

    # If the authentication was successful, you should
    # see the name of the account print out
    print(api.me().name)
    stream = Stream(auth, StdOutListener())
    stream.filter(track=inst.keys(),is_async=True)
    win.mainloop()
    stream.disconnect()


if __name__ == '__main__':
    main()