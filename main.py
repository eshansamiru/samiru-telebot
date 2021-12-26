import telebot 
import time

from PIL import Image
import requests
from io import BytesIO


TOKEN = "5006305449:AAG4G6hv4QbJOEIWCTJt6TyvYREgmkwYrUw"
#This is my image link
IMAGE_LINK = "https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fhello&psig=AOvVaw17eS1mFtOIMsRP-IziFl1F&ust=1640587879107000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNifmp6lgvUCFQAAAAAdAAAAABAJ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    print(message.text)
    
    
@bot.message_handler(commands=["hello", "hi"])
def hello(message):
    bot.send_message(message.chat.id, "Hello World")
    
    
@bot.message_handler(commands=["image", "img"])
def image(message):
    img = open("hello.jpg", "rb")
    bot.send_photo(message.chat.id, img)
    
@bot.message_handler(commands=["imagenet", "imgnet"])
def imagnet(message):
    response = requests.get("IMAGE_LINK")
    imgnet = Image.open(BytesIO(response.content))
    #Send the photo
    bot.send_photo(message.chat.id, imgnet)
    
@bot.message_handler(commands=["video", "vid"])
def video(message):
    vid = open("video.mp4", "rb")
    bot.send_video(message.chat.id, vid)
    
@bot.message_handler(commands=["videonet", "vidnet"])
def videonet(message):
    download_file(VIDEO_LINK, "myvideo.mp4")
    vidnet = open("myvideo.mp4", "rb")
    bot.send_video(message.chat.id, vidnet)