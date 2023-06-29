import telebot, requests, shutil, time
from telebot import types
from model import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from token_1 import token_bot

num_photos = 0
mode = 0

bot = telebot.TeleBot(token_bot)

def get_random_photo():
    url = "https://rand.by/image"
    driver = webdriver.Chrome()
    try:
        driver.get(url=url)
        driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/main/section/div[1]/button").click()
        time.sleep(1)
        img = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/main/section/div[2]/div[2]/div[2]/img")
        src = img.get_attribute('src')
        response = requests.get(src, stream=True)
        with open('img.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
       
    except Exception as ex:
        print(ex)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Скинуть две своих фотографии")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Скинуть фотографию стиля, а контент выбрать случайно")
    markup.row(btn2)
    bot.send_message(message.chat.id, f"Здаров {message.from_user.first_name} бот создан для переноса стиля с одного изображения на другое", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    global num_photos, mode
    fileID = message.photo[-1].file_id   
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f"{num_photos}.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    num_photos += 1

    if mode == 1 and num_photos == 2: # пользователь присылает два своих фото
        style_img = image_loader("0.jpg")
        content_img = image_loader("1.jpg")
    elif mode == 2 and num_photos == 1: # пользователь присылает только стиль, контент берётся из интернета
        style_img = image_loader("0.jpg")
        content_img = image_loader("img.jpg")
        num_photos = 2 # чтобы закинуть в модель

    if num_photos == 2:
        bot.send_message(message.chat.id, "Ща пошаманим")
        input_img = content_img.clone()
        output, frame = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                            content_img, style_img, input_img)
        make_video(frame)
        res = unloader(output.squeeze(0))
        bot.send_photo(message.chat.id, res)
        with open ('my.gif', 'rb') as gif:
            bot.send_video(message.chat.id, gif, None)
        num_photos = 0

@bot.message_handler()    
def on_click(message):
    global mode
    if message.text == "Скинуть две своих фотографии":
        bot.send_message(message.chat.id, "Кидай два фото: сначала -  стиль, потом - контент") 
        mode = 1
    elif message.text == "Скинуть фотографию стиля, а контент выбрать случайно":
        bot.send_message(message.chat.id, "Случайное фото контента")
        get_random_photo()
        file = open('img.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, "Кидай стиль") 
        mode = 2
    else:
        bot.send_message(message.chat.id, "Э слушай на кнопку нажми, да")

bot.polling(non_stop=True)