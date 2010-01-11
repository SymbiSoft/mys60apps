import appuifw, e32, audio, time

filename = "e:\\"+str(time.time())+".wav"

def recording():
    global S
    S=audio.Sound.open(filename)
    S.record()
    print "Recording on! To end it, select stop from menu!"

def closing():
    global S
    S.stop()
    S.close()
    print "Stopped"

def quit():
    script_lock.signal()
    appuifw.app.set_exit()

appuifw.app.menu = [(u"stop", closing)]

appuifw.app.title = u"Sound recorder"
appuifw.app.exit_key_handler = quit

recording()

script_lock = e32.Ao_lock()
script_lock.wait()


 

