# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'फिर भीयदि कोई बीमारी की चपेट में आता है तोवह समुचित उपचार का हकदार है, सरकार इस दिशा में सभी कदम उठा रहीहै।'
  
# Language in which you want to convert
language = 'hi'

output_file = "testing/sample_hi_3.mp3"
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save(output_file)
  
