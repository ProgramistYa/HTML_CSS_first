# Преоброзование текста в аудизапись.
from gtts import gTTS

text = "Привет , меня зовут Саша , я начинающий програмист."
language = 'ru'

tts = gTTS(text=text, lang=language)
tts.save("hello.mp3")
