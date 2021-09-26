import pytesseract as pyt
from PIL import Image
from gtts import gTTS
from playsound import playsound
from translate import Translator
from googletrans import Translator

# Read the English text from Image
img=Image.open('malayalam.png')
text=pyt.image_to_string(img,lang='mal')
text=text.replace('\n',' ')

# Translate the extrated english text to malayalam
transl=Translator()
out=transl.translate(text,dest='en')
mal_text=out.text
print(mal_text)

# read the computer by its own voice
text=gTTS(mal_text,lang='en',slow=False)
text.save("voice.mp3")
playsound("voice.mp3")
