import pytesseract as pyt
from PIL import Image
from gtts import gTTS
from playsound import playsound
from translate import Translator
from googletrans import Translator

# Read the English text from Image
img=Image.open('story_eng.png')
text=pyt.image_to_string(img)
text=text.replace('\n',' ')
# Translate the extrated english text to malayalam
transl=Translator()
out=transl.translate(text,dest='ml')
mal_text=out.text

# read the computer by its own voice
text=gTTS(mal_text,lang='ml')
text.save("voice.mp3")
playsound("voice.mp3")
