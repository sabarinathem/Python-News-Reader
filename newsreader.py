import pytesseract as pyt
from PIL import Image
from gtts import gTTS
from playsound import playsound

img=Image.open('news.jpg')
text=pyt.image_to_string(img,lang='mal')
text=text.replace('\n',' ')
print(text)
text=gTTS(text,lang='ml')
text.save("voice.mp3")
playsound("voice.mp3")