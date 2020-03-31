from gtts import gTTS 
import os 

mytext = 'Trying text to speceh! and punctuations'

myobj = gTTS(text=mytext, lang='en', slow=False) 

myobj.save("Output audio/trying.mp3") 
 
