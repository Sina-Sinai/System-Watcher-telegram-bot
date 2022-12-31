import telebot
from telebot import types
from random import randint
import re
from icecream import ic
import backend
from os import system,walk
from typing import Text
import requests
import json
import time
#from playsound import playsound
#==============================================================================================================================#
TOKEN = '1953265131:AAFv77e1VgPUMwI4blyEjj254PYOHz95Dyk'
# TOKEN = '1248089764:AAFAueuihRk7hMVkWgMAyL8o5tEOBPHqU04'
bot = telebot.TeleBot(TOKEN)
#==============================================================================================================================#
channel_id = '-1001414421073'
group_id = '-1001474810236'
#==============================================================================================================================#
ready_message = '''✅ربات اماده امتحان است
❗️ترتیب ارسال پاسخ باید به گونه مشخص شده باشد تا ربات توانایی شناسایی داشته باشد
شماره سوال=>شماره جواب  (بدون فاصله)
‼️از به کار بردن جملاتی مثل 8 میشه 2 خودداری کنید
مثال : 102=>4
🔅اگر در جواب شک داشتید بعد از نوشتن شماره جواب با یک فاصله کلمه شک رو بنویسید
مثال : 55=>4 شک
❗️زبان کیبورد شما مهم نیست و چه فارسی و چه انگلیسی به صورت استاندارد ارسال میشود.
اعداد فارسی نیز قابل دریافت میباشند
❗️در لیستی که بعد از زدن دستور /resort به گروه ارسال میشود یا لیست مرتب شده ای که در کانال قرار میگیرد ⁉️ علامت به معنای شک است.
'''
#==============================================================================================================================#
answer_list = {}
Is_in_second_page = False
answer_l = []
Admins_inside_db = []
send = {}
taking_answ = ''
Message_to_Creator = False
admin_id_list = [1263524768, 394075806]
getting_answer = False
robot = ''
dfgsdf = ''
Creator_ID = 394075806
quiz_mode = ''
Delete_Person = False
new_person_name = False
#==============================================================================================================================#
Delete_Admin = False
taking_query = False
user_id_list = []
is_in_quiz_part = False
take_clock = False
clll = False
m_I = False
s_m_text = '''❗️ هر چیزی که دوست داری هم گروهیات بدونن اینجا برام ارسال کن تا براشون بفرستم
❗️ اگه فایل یا صدا یا عکس بفرستی براشون فوروارد میکنم
❗️ اگه متن بدی براشون مینویسم
❗️ اگر هم لینک یه فایل اپلود شده داری بفرست تا براشون اون فایلو دانلود و ارسال کنم
❗️ حتی اگه یه لینک عادی هم بفرستی براشون میفرستم
❗️ اگه دستت خورده رو این گزینه و نمیخوای چیزی ارسال کنی فقط کلمه انصراف رو ارسال کن
❗️ توجه کن که همه هم گروهیات این پیامو میبینن پس اگه میخوای به شخص خاصی بفرستی نمیشه
❗️ توجه کن که این فرایند هم مثل تمامی بخش ها ناشناسه'''
trnslt = False
s_m = False
api_key = "JC31ZN02Fs7yPF6lEItn6STzN0lb4LMBVaNCKHWCAHk"
url = "https://api.unsplash.com"
todo = {'aaaa':1, 'bbbb':0, 'cccc':1, 'dddd':0}
#==============================================================================================================================#
m_i = None
User_PassWord_inuse = []
text = ''
ttttt = ''
sending_back = False
answering = None
searching = False
Make_New_PassWord = False
live = False
New_Admin_Person = False
nickname_list_db = []
first_message = '📃📄 |Answer List| 📃📄'
system('cls')
print('System Watcher is Ready !')
#==============================================================================================================================#
def Check_List():
    global nickname_list_db
    nickname_list_db = []
    for i in backend.view():
    # نیک نیم یه استرینگه ولی چیزی که ممایزش میکنه اون عدد بعد از code هست که خب یکم سخته
    # میونیم خیلی راحت از 001 به 1 تغیرش بدم و خودمو راحت کنم. کم هم تمیزتره
        nickname_list_db.append(int(i[2]))
        nickname_list_db.sort()
    # print(nickname_list_db)
#==============================================================================================================================#
def Check_user_id():
    global user_id_list
    user_id_list = []
    for i in backend.view():
        user_id_list.append(int(i[0]))
        user_id_list.sort()
#==============================================================================================================================#
def Check_Admin_numbers():
    global Admins_inside_db, admin_id_list
    Admins_inside_db = []
    for i in backend.view():
        Admins_inside_db.append(int(i[6]))
        if i[5] == 1 and i[0] not in admin_id_list:
            admin_id_list.append(int(i[0]))
    b = []
    for i in Admins_inside_db:
        if i not in b:
            b.append(i)
    Admins_inside_db = b
    Admins_inside_db.sort()
#==============================================================================================================================#
def Check_PassWord():
    global User_PassWord_inuse
    User_PassWord_inuse = []
    for i in backend.view():
        User_PassWord_inuse.append(int(i[4]))
#==============================================================================================================================#
def getfile(filename):
    myfile = open(filename, '+r')
    return myfile.read()
    myfile.close()
#==============================================================================================================================#
def putfile(filename, filedata):
    myfile = open(filename, 'w+')
    myfile.write(filedata)
    myfile.close()
#==============================================================================================================================#
def rand_photo(userchatid):
    global api_key, url
    mes = '📤 در حال ارسال درخواست...'
    mi = bot.send_message(userchatid,mes).message_id
    mes += '\n📥 دریافت اطلاعات موفق...'
    try:
        res = requests.get(url +'/photos/random'+ '?client_id=' + api_key)
        bot.edit_message_text(mes ,userchatid,mi)
    except:
        res = requests.get(url +'/photos/random'+ '?client_id=' + api_key)
        bot.edit_message_text(mes ,userchatid,mi)
    js = res.text
    record = json.loads(js)
    # return(record["urls"]['full'])
    mes += '\n📲 در حال ارسال عکس. لطفا صبور باشید'
    bot.edit_message_text(mes ,userchatid,mi)
    try:
        bot.send_photo(userchatid, record["urls"]['full'], record['description'])
        quiez(userchatid)
    except Exception as err:
        print(err)
        if err == 'A request to the Telegram API was unsuccessful. Error code: 400. Description: Bad Request: failed to get HTTP URL content':
            bot.delete_message(userchatid,mi)
            rand_photo(userchatid)  
    # bot.send_photo(userchatid, record["urls"]['full'], record['description'])
#==============================================================================================================================#
def by_type_photo(query, userchatid):
    global api_key, url
    mes = '📤 در حال ارسال درخواست...'
    mi = bot.send_message(userchatid,mes).message_id
    try:
        res = requests.get(url +'/search/photos'+ '?client_id=' + api_key , {'query' : query})
    except:
        res = requests.get(url +'/search/photos'+ '?client_id=' + api_key , {'query' : query})
    mes += '\n📥 دریافت اطلاعات موفق...'
    bot.edit_message_text(mes,userchatid,mi)
    js = res.text
    record = json.loads(js)
    # for i in len(record['results']):
    print(type(record))
    # bot.send_message(userchatid, record['results'][0]['urls']['full'])
    length = len(record['results'])
    print(record['total'])
    bot.send_message(userchatid,f'نتیجه جستجو برای کلمه " {query} " :\nتعداد نتیجه : {length}\nدر حال ارسال صفحه اول...')
    for i in range(len(record['results'])):
        try:
            bot.send_photo(userchatid,record['results'][i]['urls']['full'],caption=record['description'])
        except:
            continue
    quiez(userchatid)
#==============================================================================================================================#
@bot.edited_message_handler(content_types=['text'])
def edited_message_botmain(user):
    botmain(user)
#==============================================================================================================================#
def quiez(userchatid):
    global Is_in_second_page
    Is_in_second_page = True
    secret_btn = types.ReplyKeyboardMarkup(resize_keyboard=(1,2),row_width=3)
    secret_1 = types.KeyboardButton('بخش امتحان 〽️')
    secret_3 = types.KeyboardButton('پنل مدیریت 💻')
    secret_4 = types.KeyboardButton('TO DO List ✔')
    secret_5 = types.KeyboardButton('🎞 دریافت اطلاعات یک فیلم')
    secret_6 = types.KeyboardButton('ترجمه 📖')
    secret_7 = types.KeyboardButton('🗞 ارسال پیام به دیگران')
    secret_8 = types.KeyboardButton('بازگشت 🔙')
    secret_btn.add(secret_1,secret_3,secret_4,secret_5,secret_6,secret_7,secret_8)
    bot.send_message(userchatid,'🖥 به صفحه دوم خوش امدید',reply_markup=secret_btn)
    #playsound('music.mp3')
#==============================================================================================================================#
def quiz_part(userchatid):
    global is_in_quiz_part
    is_in_quiz_part = True
    q_btn = types.ReplyKeyboardMarkup((1,2))
    q_1 = types.KeyboardButton('جواب ها 📁')
    q_2 = types.KeyboardButton('ارسال جواب 📤')
    q_3 = types.KeyboardButton('پاکسازی لیست جواب ها 〽️')
    q_4 = types.KeyboardButton('جست و جو میان جواب ها 🔍')
    q_5 = types.KeyboardButton('ایجاد تایمر امتحان ⏰')
    q_6 = types.KeyboardButton('5 جواب اخر 📨')
    q_7 = types.KeyboardButton('دریافت زنده جواب ⏱📊')
    q_8 = types.KeyboardButton('سوال ❓')
    q_9 = types.KeyboardButton('بازگشت 🔙')
    q_10 = types.KeyboardButton('🔙')
    q_btn.add(q_1,q_2,q_3,q_4,q_5,q_6,q_7,q_8,q_9,q_10)
    bot.send_message(userchatid,'🤏 به بخش امتحان خوش امدید',reply_markup=q_btn)
#==============================================================================================================================#
def adminpanel(userchatid):
    admin_btn = types.ReplyKeyboardMarkup(row_width=2)
    admin1 = types.KeyboardButton('🚸 اضافه کردن فرد جدید')
    admin2 = types.KeyboardButton('حذف کردن فرد 💢')
    admin3 = types.KeyboardButton('⬅️ تغیر رمز عبور')
    admin4 = types.KeyboardButton('⏱ تمدید اعتبار')
    admin5 = types.KeyboardButton('🔰 افراد زیرمجموعه')
    admin6 = types.KeyboardButton('🖌 ارتباط با سازنده')
    admin7 = types.KeyboardButton('بازگشت 🔙')
    admin8 = types.KeyboardButton('🔙')
    admin_btn.add(admin1,admin2,admin3,admin4,admin5,admin6,admin7,admin8)
    if userchatid == 1263524768 or userchatid == 394075806:
        admin8 = types.KeyboardButton('🔚 بازگشت به منوی ادمین اصلی')
        admin_btn.add(admin8)
    # حواست باشه بعدا به این قسمت وقتی پیام ارسال میشه روزای باقی مونده از اعتبارشو نشون بده
    bot.send_message(userchatid,'به پنل مدیریت خوش امدید',reply_markup=admin_btn)
#==============================================================================================================================#
def sending_photo(userchatid):
    ph_btn = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=(1,2))
    ph1 = types.KeyboardButton('عکس تصادفی')
    ph2 = types.KeyboardButton('جستجوی موضوع عکس')
    ph_btn.add(ph1,ph2)
    bot.send_message(userchatid,'لطفا مشخص کنید :', reply_markup=ph_btn)
#==============================================================================================================================#
def Send_to_others(userchatid, usertext, caption=''):
    global s_m
    if usertext.startswith('http') or usertext.startswith('https'):
        for i in backend.view():
            if backend.search(userchatid)[0][6] == i[6]:
                try:
                    # print(i)
                    bot.send_document(i[0],usertext,caption=caption)
                except Exception as err:
                    print(i)
                    ic(err)
                    ic()
                    try:
                        bot.send_message(i[0],userchatid)
                    except:
                        print(i)
                        continue
        s_m = False
        bot.send_message(userchatid,'ارسال شد')
    else:
        for i in backend.view():
            if i[6] == backend.search(userchatid)[0][6]:
                # print(i)
                try:
                    bot.send_message(i[0],usertext)
                except:
                    print(i)
                    continue
        s_m = False
        bot.send_message(userchatid,'ارسال شد')
#==============================================================================================================================#
def main_admin(userchatid):
    Main_ad = types.ReplyKeyboardMarkup(row_width=4)
    Main_1 = types.KeyboardButton('اضافه کردن ادمین ❇️')
    Main_2 = types.KeyboardButton('حذف ادمین 💢')
    Main_3 = types.KeyboardButton('حذف کردن فرد 💢')
    Main_4 = types.KeyboardButton('منوی ادمین عادی 📃')
    Main_5 = types.KeyboardButton('تمدید اعتبار ادمین 🕒')
    Main_6 = types.KeyboardButton('افراد موجود 🙍‍♂️')
    Main_7 = types.KeyboardButton('ادمین های موجود 🙍')
    Main_8 = types.KeyboardButton('پیام به ادمین ها ⬅️')
    Main_9 = types.KeyboardButton('اخطار مدت اعتبار ⚠️')
    Main_10 = types.KeyboardButton('ارسال پیام 📡')
    Main_0 = types.KeyboardButton('بازگشت 🔙')
    Main_00 = types.KeyboardButton('🔙')
    Main_ad.add(Main_1,Main_2,Main_3,Main_4,Main_5,Main_6,Main_7,Main_8,Main_9,Main_0,Main_00)
    bot.send_message(userchatid,'به منوی مدیریت اصلی خوش امدید',reply_markup=Main_ad)
#==============================================================================================================================#
def internal_answer_person(userchatid):
    q_btn = types.ReplyKeyboardMarkup(resize_keyboard=1,row_width=2)
    for i in backend.view():
        q = types.KeyboardButton('کد '+str(i[2]))
        q_btn.add(q)
    bot.send_message(userchatid,'از چه کسی سوال دارید؟',reply_markup=q_btn)
#==============================================================================================================================#
def internal_answer(userchatid,to_id):
    global send, getting_answer
    getting_answer = True
    a_btn = types.ReplyKeyboardMarkup(resize_keyboard=(1,2))
    a1 = types.KeyboardButton('پایان')
    a_btn.add(a1)
    send['q'] = userchatid
    send['a'] = to_id
    bot.send_message(userchatid,'لطفا سوال خود را بپرسید و بعد روی پایان کلیک کنید',reply_markup=a_btn)
#==============================================================================================================================#
def hi(userchatid):
    #print(userchatid)
    global Is_in_second_page
    Is_in_second_page = False
    dokmeha = types.ReplyKeyboardMarkup(row_width=2)
    dokme1 = types.KeyboardButton('Take a screenshot')
    dokme2 = types.KeyboardButton('file manager')
    dokme3 = types.KeyboardButton('play sound')
    dokme4 = types.KeyboardButton('power options')
    dokmeha.add(dokme1,dokme2,dokme3,dokme4)
    # erere = types.InlineKeyboardMarkup(row_width=1)
    # rrrr = types.InlineKeyboardButton('text','https://google.com')
    # erere.add(rrrr) #it works bu you can't user both of them (inline and normal) in same time
    bot.send_message(userchatid,'Hi 😊 what can i do for you?',reply_markup=dokmeha)
#==============================================================================================================================#
def Delete_Person_func(userchatid,id="",nickname="", code="", live_answ="", entering_code="", is_admin="", subset_of=""):
    # has bug
    global Delete_Person, nickname_list_db, Delete_Admin
    dl_p_ch = backend.search(id,nickname, code, live_answ, entering_code, is_admin, subset_of)
    try:
        nickname_list_db.remove(int(dl_p_ch[0][2]))
        backend.delete(dl_p_ch[0][0])
        print(backend.view())
        bot.send_message(userchatid,f'فرد با ایدی عددی : {dl_p_ch[0][0]}\nاسم مستعار : {dl_p_ch[0][1]}\nشماره کد : {dl_p_ch[0][2]}\nبا موفقیت پاک شد')
        Delete_Person = False
        Check_List()
        Check_user_id()
        Check_Admin_numbers()
        Delete_Admin = False
        quiez(userchatid)
    except:
        bot.send_message(userchatid,'فرایند با مشکل مواجه شد ❌')
        Delete_Person = False
        Check_List()
        Check_user_id()
        Check_Admin_numbers()
        quiez(userchatid)
#==============================================================================================================================#
def answersfunc(userchatid,usermessageid):
    global answer_l
    t = ''
    if answer_l != []:
        for i in answer_l:
            t += i + '\n'
        bot.send_message(userchatid,t,reply_to_message_id=usermessageid)
    else:
        bot.send_message(userchatid,'هنوز هیچ جوابی دریافت نشده است ❌')
#==============================================================================================================================#
def Check_if_int(usertext):
    try:
        if int(usertext):
            return True
        else:
            raise Exception
    except:
        return False
#==============================================================================================================================#
def f1(user):
    usertext = user.text
    usermessageid = user.message_id
    userchatid = user.chat.id
    global first_message, m_i
    try:
        if 'شک' in usertext and '=>' in usertext:
            ic()
            match = re.search(r'(\d+)\=>(\d) (\w+)',usertext)
            ic()
            question_number = match.group(1)
            answer_number = match.group(2)
            ic()
        elif '=>' in usertext and not 'شک' in usertext:
            ic()
            match = re.search(r'(\d+)\=>(\d)',usertext)
            ic()
            question_number = str(match.group(1))
            answer_number = str(match.group(2))
            ic()
        elif 'میشه' in usertext and 'توضیح' not in usertext:
            a = []
            for i in usertext:
                if i.isdigit():
                    a.append(True)
                else:
                    pass
            if len(a) == 2:
                raise Exception
            else:
                pass
        elif '=' in usertext and '>' not in usertext:
            raise Exception
        elif '=' not in usertext and '>' in usertext:
            raise Exception
        if 'شک' in usertext and '=>' in usertext:
            ic()
            if int(answer_number) < 5:
                answer_list[question_number] = answer_number
                ic()
                # first_message += '\nQ : | '+str(question_number)+' |'+' A : | '+answer_number+' | |?|'
                first_message += f'\n🔱 {question_number} :  ✅ {answer_number} ⁉️'
                ic()
                bot.edit_message_text(first_message,channel_id,m_i)
            else:
                bot.send_message(userchatid,'شماره گزینه باید از 1 تا 4 باشد 😐',reply_to_message_id=usermessageid)
        elif '=>' in usertext and 'شک' not in usertext:
            ic()
            if int(answer_number) < 5:
                answer_list[question_number] = answer_number
                ic()
                first_message += f'\n🔱 {question_number} :  ✅ {answer_number}'
                ic()
                bot.edit_message_text(first_message,channel_id,m_i)
            else:
                bot.send_message(userchatid,'شماره گزینه باید از 1 تا 4 باشد 😐',reply_to_message_id=usermessageid)
    except Exception as Error:
        ic(Error)
        ic()
        if str(Error) == 'A request to the Telegram API was unsuccessful. Error code: 400 Description: Bad Request: message to edit not found':
            m_i = bot.send_message(channel_id,'📃📄 |Answer List| 📃📄').message_id
            botmain(user)
        else:
            bot.send_message(userchatid,
            'لطفا با فرمت درست دوباره ارسال فرمایید**شماره گزینه<=شماره سوال**\nاول گزینه سوالو بنویس بعد یه = بزار بعد یه < بزار که شبیه فلش بشه، خب؟\nبعد هم شماره گزینه رو بنویس\nاگه شک داشتی بعد از شماره گزینه یه فاصله بزن بعد بنویس "شک" تمام :)',
            reply_to_message_id=usermessageid)
#==============================================================================================================================#
def count_time(userchatid, hour, minute, second):
    global take_clock
    take_clock = False
    hour, minute, second = int(hour), int(minute), int(second)
    sec = int((hour * 60 * 60) + (minute * 60) + second)
    alert = f"{hour} ساعت و {minute} دقیقه و {second} ثانیه تا پایان امتحان!"
    mi = bot.send_message(userchatid,alert).message_id
    bot.pin_chat_message(userchatid, mi, True)
    # bot.pin_chat_message(userchatid, mi)
    for i in range(sec+1):
        if hour == 0 and minute == 0 and second == 0:
            bot.send_message(userchatid, 'زمان امتحان به پایان رسید!')
        else:
            if second == 0 and minute != 0:
                minute -= 1
                second = 60
            elif minute == 0 and hour != 0:
                hour -= 1
                minute = 60
                second = 00
            else:
                time.sleep(1)
                second -= 1
                # bot.delete_message(userchatid, mi)
                alert = f"{hour} ساعت و {minute} دقیقه و {second} ثانیه تا پایان امتحان!"
                mi = bot.edit_message_text(alert, userchatid, mi).message_id
#==============================================================================================================================#
def save(userchatid,usertext):
    num = randint(10000,999999)
    if num in User_PassWord_inuse:
        num = randint(10000,999999)
    text = usertext.replace('/save ','')
    putfile(f'database/data_{num}.txt',str(text))
    bot.send_message(userchatid,f'💾 Your message has been saved\nwith {num} data number')
#==============================================================================================================================#
def read_saves(userchatid):
    list_file = ''
    for root, dirs, files in walk('database'):
        for filename in files:
            list_file += '\n📦'+str(filename)
    bot.send_message(userchatid,f'📥 Your saved files are :\n{list_file}')
#==============================================================================================================================#
def translate(userreplytext,userchatid,usermessageid):
    fa = ['ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی']
    en = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    listt = []
    index = 0
    for i in userreplytext:
        if i in en:
            a = open('dictionary.txt','r+',encoding='UTF8')
            b = a.readline()
            listt.append(i)
            if i == " ":
                listt.pop(index)
                listt.append("-")
            elif i == "\n":
                listt.pop(index)
                listt.append("\n")
            else:
                try:
                    while i != b[0]:
                        b = a.readline()
                except:
                    continue
                listt.pop(index)
                listt.append(b[2])
            index += 1
        if i in fa:
            a = open('dictionary.txt','r+',encoding='UTF8')
            b = a.readline()
            listt.append(i)
            if i == " ":
                listt.pop(index)
                listt.append("-")
            elif i == "\n":
                listt.pop(index)
                listt.append("\n")
            else:
                try:
                    while i != b[2]:
                        b = a.readline()
                except:
                    continue
                listt.pop(index)
                listt.append(b[0])
            index += 1
    a.close()
    c = ''.join(listt)
    bot.send_message(userchatid,c,reply_to_message_id=usermessageid)
#==============================================================================================================================#
def MAKE_NEW_PASS(userchatid,id="",nickname="", code="", live_answ="", entering_code="", is_admin="", subset_of=""):
    global Make_New_PassWord
    try:
        n_PW = randint(100000,999999)
        if n_PW in User_PassWord_inuse:
            n_Pw = randint(100000,999999)
        pw_p_ch = backend.search(id,nickname, code, live_answ, entering_code, is_admin, subset_of)
        print(f'searched id : {pw_p_ch}')
        backend.update(pw_p_ch[0][0],pw_p_ch[0][1],pw_p_ch[0][2],pw_p_ch[0][3],n_PW,pw_p_ch[0][5],pw_p_ch[0][6])
        print(f'updated : {pw_p_ch}')
        bot.send_message(userchatid,f'کد فرد : {pw_p_ch[0][1]}\nID عددی : {pw_p_ch[0][0]}\nرمز عبور جدید : {n_PW}')
        Check_List()
        Check_PassWord()
        Check_user_id()
        Make_New_PassWord = False
        quiez(userchatid)
    except:
        bot.send_message(userchatid,'فرایند با مشکل مواجه شد ❌')
        Make_New_PassWord = False
        Check_List()
        Check_user_id()
        quiez(userchatid)
#==============================================================================================================================#
def take_message(usertext, usermessageid, userchatid):
    global answer_list, first_message,m_i
    ic()
    if 'شک' in usertext and '=>' in usertext:
        ic()
        match = re.search(r'(\d+)=>',usertext)
        question_number = str(match.group(1))
        usertext = usertext.replace(match.group(1),'')
        usertext = usertext.replace('=>','')
        usertext += '   ⁉️'
    elif '=>' in usertext and 'شک' not in usertext:
        ic()
        match = re.search(r'(\d+)=>',usertext)
        question_number = str(match.group(1))
        usertext = usertext.replace(match.group(1),'')
        usertext = usertext.replace('=>','')
    answer_list[question_number] = usertext
    f''
    first_message += f'\n🔱 {question_number} :  ✅ {usertext}'
    bot.edit_message_text(first_message,channel_id,m_i)
#==============================================================================================================================#
def sendinganswerfunc(userchatid):
    global answering
    answering = True
    botton = types.ReplyKeyboardMarkup(resize_keyboard=(1))
    btn1 = types.KeyboardButton('📌 تمام')
    botton.add(btn1)
    bot.send_message(userchatid,'🔰 لطفا جواب های خود را ارسال کنید و سپس گزینه تمام را بزنید',reply_markup=botton)
#==============================================================================================================================#
def sorting(usermessageid,userchatid):
    global answer_list
    ic()
    text = '📃📄 |Answer List| 📃📄\n'
    if answer_list != {}:
        for i in answer_list:
            if '|?|' not in answer_list[i]:
                text += f'Q : |{i}| A : |{answer_list[i]}|\n'
                ic()
            if '|?|' in answer_list[i]:
                text += f'Q : |{i}| A : |{answer_list[i]}| |?|\n'
                ic()
        bot.send_message(userchatid,text,reply_to_message_id=usermessageid)
        ic()
    else:
        bot.send_message(userchatid,'هنوز سوالی نفرستادی که از من لیست سوالارو میخای داداش 😐😐',reply_to_message_id=usermessageid)
#==============================================================================================================================#
def take_clock_func(usertext,userchatid):
    global take_clock
    if usertext != 'انصراف':
        try:
            match = re.search(r"(\d{2}):(\d{2}):(\d{2})",str(usertext))
            # ic()
            hour = int(match.group(1))
            minute = int(match.group(2))
            second = int(match.group(3))
            # print(match)
            # ic()
            count_time(userchatid, hour, minute, second)
        except Exception as err:
            ic(err)
            bot.send_message(userchatid,'لطفا با فرمت درست ارسال کنید و  اگر قصد انصراف دارید کلمه انصراف را ارسال کنید')
    else:
        bot.send_message(userchatid,'عملیات متوقف شد')
        take_clock = False
#==============================================================================================================================#
def receiveliveanswer(userchatid):
    ccc = backend.search(userchatid)
    if ccc[0][3]:
        backend.update(userchatid,ccc[0][1],ccc[0][2],False,ccc[0][4],ccc[0][5],ccc[0][6])
        bot.send_message(userchatid,'دریافت زنده جواب خاموش شد ❌')
    else:
        backend.update(userchatid,ccc[0][1],ccc[0][2],True,ccc[0][4],ccc[0][5],ccc[0][6])
        bot.send_message(userchatid,'دریافت زنده جواب روشن شد ✅')
#==============================================================================================================================#
def last5answers(userchatid, usermessageid):
    global answer_l
    if answer_l != []:
        t = answer_l[-5:]
        te = ''
        for i in t:
            te += i + '\n'
        bot.send_message(userchatid,te,reply_to_message_id=usermessageid)
    else:
        bot.send_message(userchatid,'هنوز هیچ جوابی دریافت نشده است ❌')
#==============================================================================================================================#
def m_Ifunc(usertext, userchatid):
    global m_I
    i = None
    t = None
    typem = None
    y = None
    p = [i, t, y, typem]
    if Check_if_int(usertext):
        length = 0
        for i in usertext:
            length += 1
        if length == 4:
            y = int(usertext)
        else:
            bot.send_message(userchatid, 'سال وارد شده اشکال دارد لطفا دوباره تلاش کنید')
    elif usertext.startswith('tt'):
        i = usertext
    elif usertext in ['movie', 'series', 'episode']:
        typem = usertext
    else:
        t = usertext
    index = 0
    for i in p:
        if i != None:
            index += 1
        else:
            continue
    if index == 2:
        bot.send_message(userchatid, 'اطلاعات ارسالی کافی است. درخواست ارسال شد. لطفا منتظر بمانید.')
        res = requests.get(url='http://www.omdbapi.com/?i=tt3896198&apikey=9e512dd2', params={'i' : i, 't' : t, 'type' : typem, 'y' : y})
        bot.send_photo(userchatid,
        "https://m.media-amazon.com/images/M/MV5BNjM0NTc0NzItM2FlYS00YzEwLWE0YmUtNTA2ZWIzODc2OTgxXkEyXkFqcGdeQXVyNTgwNzIyNzg@._V1_SX300.jpg",
        caption= f'Title : {res["Title"]}\nGenre : {res["Genre"]}\nActors : {res["Actors"]}\nStory : {res["Plot"]}\nImdb : {res["imdbRating"]}\nRotten Tomatoes : {res["Ratings"][1]["Value"]}\nMetacritic : {res["Ratings"][2]["Value"]}\nBoxoffice : {res["BoxOffice"]}')
    m_I = False
#==============================================================================================================================#
def poweroptions(userchatid):
    dokmeha = types.ReplyKeyboardMarkup()
    dokme1 = types.KeyboardButton('Shut down')
    dokme2 = types.KeyboardButton('Restart')
    dokme3 = types.KeyboardButton('Home')
    dokmeha.add(dokme1,dokme2,dokme3)
    bot.send_message(userchatid,'Welcome to poweroption menu',reply_markup=dokmeha)
#==============================================================================================================================#
def send_answer_to_member_func(userchatid):
    global sending_back
    eee = types.ReplyKeyboardMarkup(resize_keyboard=(1,2))
    eee1 = types.KeyboardButton('⭕️ اتمام پاسخ دهی')
    eee.add(eee1)
    bot.send_message(userchatid,'🔰 لطفا پاسخ خود به کاربر را وارد نمایید و سپس اتمام را بزنید',reply_markup=eee)
    sending_back = True
#==============================================================================================================================#
def Message_to_Creator_func(userusername,userchatid,usertext):
    global Message_to_Creator, send
    try:
        ryry = types.ReplyKeyboardMarkup((1,2))
        ry1 = types.KeyboardButton('〽️ ارسال پیام پشتیبانی به کاربر')
        ry2 = types.KeyboardButton('⭕️ نادیده گرفتن')
        ryry.add(ry1,ry2)
        bot.send_message(send['a'],f'🧑‍💻 پیام از طرف کاربر \n{userchatid} | {userusername} : \n' + usertext,reply_markup=ryry)
        bot.send_message(userchatid,'پیام با موفقیت ارسال شد ✅\nدر عرض چند دقیقه یا چند ساعت به پیام شما پاسخ خواهیم داد')
        Message_to_Creator = False
        quiez(userchatid)
    except:
        bot.send_message(userchatid,'فرایند با مشکل مواجه شد ❌')
        Message_to_Creator = False
        quiez(userchatid)
def s_m_func(usertext,userchatid,usercaption):
    global s_m
    if usertext != 'انصراف':
        Send_to_others(userchatid,usertext,usercaption)
    else:
        bot.send_message(userchatid,'عملیات متوقف شد')
        s_m = False
#==============================================================================================================================#
def clearanswerlist(userchatid):
    global clll
    cll = types.ReplyKeyboardMarkup(resize_keyboard=(1,2))
    cl1 = types.KeyboardButton('بلی')
    cl2 = types.KeyboardButton('خیر')
    cll.add(cl1, cl2)
    bot.send_message(userchatid,'ایا مطمئنید میخواهید لیست جواب ها را پاک کنید؟\nتوجه کنید که این عمل قابل برگشت نمی باشد',reply_markup=cll)
    clll = True
def managerpanelfunc(userchatid):
    if userchatid == 1263524768 or userchatid == 394075806:
        main_admin(userchatid)
    else:
        if userchatid in admin_id_list:
            adminpanel(userchatid)
        else:
            bot.send_message(userchatid,'❌ شما دسترسی ادمین ندارید')
#==============================================================================================================================#
def clllfunc(userchatid,usertext):
    global answer_l, clll
    if usertext == 'بلی':
        answer_l = []
        clll = False
        quiez(userchatid)
        bot.send_message(userchatid,'لیست سوالات پاک شد')
    if usertext == 'خیر':
        clll = False
        bot.send_message(userchatid,'عملیات متوقف شد')
        quiez(userchatid)
#==============================================================================================================================#
def readfunc(usertext,userchatid):
    usertext.replace('/read ','')
    usertext = str(usertext)
    try:
        file_text = getfile(f'database/data_{usertext}')
        file_text = str(file_text)
        bot.send_message(userchatid, f"Here's your file's text:\n--------------------------\n{file_text}")
    except:
        bot.send_message(userchatid, "Sorry, We didn't find your file!\nPlease try again")
#==============================================================================================================================#
def codeintextfunc(usertext,userchatid):
    usertext = usertext.replace('کد ','')
    for i in backend.view():
        if usertext == i[2]:
            internal_answer(userchatid,i[0])
#==============================================================================================================================#
def sending_back_func(usertext,userchatid):
    global send, sending_back, ttttt
    if usertext == '⭕️ اتمام پاسخ دهی':
        aaaaa = send['a']
        bot.send_message(send['q'],f'✅: {backend.search(aaaaa)[0][1]} در پاسخ به سوال شما : \n' + ttttt)
        sending_back = False
        send = {}
        quiez(userchatid)
    else:
        ttttt += usertext + '\n'
#==============================================================================================================================#
def makenewpasswordfunc(usertext,userchatid):
    global nickname_list_db
    if Check_if_int(usertext):
        if len(usertext) == 6:
            MAKE_NEW_PASS(userchatid,entering_code=int(usertext))
        if 6 < len(usertext):
            MAKE_NEW_PASS(userchatid,id=int(usertext))
        if int(usertext) in nickname_list_db:
            MAKE_NEW_PASS(userchatid,code=usertext)
    else:  
        if 'code ' in usertext:
            MAKE_NEW_PASS(userchatid,nickname=usertext)
#==============================================================================================================================#
def quizmode_func(userchatid,usermessageid):
    global q_m
    q_m = ''
    if robot == 'ربات اماده' and quiz_mode == 'on':
        q_m += 'حالت امتحان عادی و تشریحی فعاله 📝'
    elif robot == 'ربات اماده' and quiz_mode != 'on':
        q_m += 'حالت امتحان عادی فعاله ☑️'
    else:
        q_m += 'حالت امتحان فعال نیس'
    bot.send_message(userchatid,q_m,reply_to_message_id=usermessageid)
def searchinanswersfunc(userchatid):
    global answer_l, searching
    if answer_l != []:
        searching = True
        bot.send_message(userchatid,'🔰 لطفا کلمه ای که میخاهید در میان جواب ها جست و جو شود را ارسال کنید')
    else:
        bot.send_message(userchatid,'هنوز هیچ جوابی دریافت نشده است ❌')
#==============================================================================================================================#
def searchingfunc(userchatid,usermessageid,usertext):
    global searching
    ttt = ''
    for i in answer_l:
        if usertext in i:
            ttt += i + '\n#----------------#\n'
    if ttt != '':
        bot.send_message(userchatid,ttt,reply_to_message_id=usermessageid)
        searching = False
        bot.send_message(userchatid,'اتمام جست و جو 🚫')
    else:
        bot.send_message(userchatid,'هیچ جوابی این کلمه را شامل نمیشود ❌\nاتمام جست و جو 🚫')
        searching = False
#==============================================================================================================================#
def answeringfunc(usertext, userchatid):
    global answering, dfgsdf
    if usertext == '📌 تمام':
        answering = False
        quiez(userchatid)
    else:
        dfgsdf = str(f'〽️ {backend.search(userchatid)[0][1]} 〽️ :: ⬇️')
        dfgsdf += str(f'\n✅ {usertext}')
        answer_l.append(dfgsdf)
        for i in backend.view():
            if i[3]:
                bot.send_message(i[0],dfgsdf)
def endtest(userchatid):
    global robot, quiz_mode,answer_list
    robot = ''
    quiz_mode = ''
    answer_list = {}
    bot.delete_message(channel_id,m_i)
    bot.send_message(userchatid,"ازمون پایان یافت")
#==============================================================================================================================#
def todofunc(usermessageid, userchatid):
    change_btn = types.InlineKeyboardMarkup(row_width=3)
    text_line = ''
    index = 1
    if todo != {}:
        for i in todo:
            text_line += f'\n〽 {str(index)}.  {i}'
            if todo[i] == 1:
                text_line += '   ✅'
                chbtn = types.InlineKeyboardButton(f"تغییر حالت شماره {str(index)} به انجام نشده", callback_data=f"todo_x_{str(index)}")
            else:
                text_line += '   ❌'
                chbtn = types.InlineKeyboardButton(f"تغییر حالت شماره {str(index)} به انجام شده",callback_data=f"todo_o_{str(index)}")
            index += 1
            change_btn.add(chbtn,row_width=3)
        # خط بالا رو داشتم برای گزاشتن تنظیمات مربوط به لیست تودو مینوشتم که چون فعلا تلگرام ندارم نمیشه
        # بعدا باید این ماژولو کامل کنم الان فعلا هیجی نداره
        #  یادت باشه قسمت اینلاین ماژول تایپس رو قشنگ زیر و رو کنی
    else:
        text_line = '⚠هنوز هیچ چیزی اضافه نکردی!'
    bot.send_message(userchatid, text_line, True, usermessageid,reply_markup=change_btn)
#==============================================================================================================================#
def getting_answer_func(usertext, userchatid):
    global taking_answ
    if usertext == 'پایان':
        qqq = types.ReplyKeyboardMarkup(resize_keyboard=(1,2))
        qqq1 = types.KeyboardButton('⬅️ ارسال پاسخ به کاربر')
        qqq2 = types.KeyboardButton('⭕️ نادیده گرفتن ⭕️')
        qqq.add(qqq1,qqq2)
        quiez(userchatid)
        bot.send_message(send['a'],f'❇️ پیام از طرف کابر : \n |⨈|{backend.search(userchatid)[0][1]}|⨈| : \n' + taking_answ,reply_markup=qqq)
        getting_answer = False
        taking_answ = ''
    else:
        taking_answ += usertext + '\n'
#==============================================================================================================================#
def ignore_func(userchatid):
    global send, sending_back, Message_to_Creator
    send = {}
    sending_back = False
    Message_to_Creator = False
    quiez(userchatid)
#==============================================================================================================================#
def clsort(usermessageid,userchatid):
    global answer_list
    answer_list = {}
    bot.send_message(userchatid,'لیست سوالات پاک شد', reply_to_message_id=usermessageid)
#==============================================================================================================================#
@bot.callback_query_handler(func=lambda call: True)
def callbackq(user):
    global todo
    job = user.data
    usermessageid = user.message.message_id
    userchatid = user.from_user.id
    usertxt = user.message.text
    if job.startswith('todo_'):
        job = job.replace('todo_','')
        if job.startswith('x_'):
            job = int(job.replace('x_','')) - 1
            inx = 0
            for i in todo:
                if job == inx:
                    todo[i] = 0
        elif job.startswith('o_'):
            job = int(job.replace('o_','')) - 1
            inx = 0
            for i in todo:
                if job == inx:
                    todo[i] = 1
        bot.edit_message_text("ربات در دست تعمیر است")
        # i have to split the main function into multiple functions so i stoped changing this until i finish that
    a = 'aaa'
#==============================================================================================================================#
@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact', 'sticker'])
def SSend_to_others(user):
    usermessageid = user.message_id
    userchatid = user.chat.id
    global s_m
    if s_m:
        for i in backend.view():
            if backend.search(userchatid)[0][6] == i[6]:
                try:
                    bot.forward_message(i[0],userchatid,usermessageid)
                except:
                    print(i)
                    continue
        s_m = False
        bot.send_message(userchatid,'ارسال شد')
#==============================================================================================================================#
@bot.message_handler(content_types=['text'])
def botmain(user):
    # print(user.forward_from.id)
    Check_PassWord()
    Check_List()
    Check_user_id()
    Check_Admin_numbers()
    global m_i, first_message, answer_list, robot, quiz_mode, answering, searching, live, taking_answ, send, getting_answer, take_clock
    global sending_back, ttttt, dfgsdf, admin_id_list, new_person_name, nickname_list_db, Make_New_PassWord, Delete_Person, s_m, todo
    global Creator_ID, Message_to_Creator, Is_in_second_page, New_Admin_Person, Delete_Admin, taking_query, clll, answer_l,is_in_quiz_part,trnslt
    global m_I, s_m_text
    # bot.send_message(246118493,"This a Test")
    usertext = user.text
    usermessageid = user.message_id
    userchatid = user.chat.id
    userusername = user.from_user.username
    usercaption = user.caption
    # bot.send_message(userchatid, user)
    if usertext == 'ربات اماده':
        m_i = bot.send_message(channel_id,'📃📄 |Answer List| 📃📄').message_id
        bot.send_message(userchatid,ready_message)
        robot = 'ربات اماده'
    if robot == 'ربات اماده':
        if quiz_mode == 'on' and '=>' in usertext:
            take_message(usertext, usermessageid, userchatid)
        if robot == 'ربات اماده' and quiz_mode != 'on':
            f1(user)
#==============================================================================================================================#
    if usertext == '/resort':
        sorting(usermessageid,userchatid)
    elif usertext == '/clsort':
        clsort(usermessageid,userchatid)
    elif usertext == '/start' or usertext == 'Home' or usertext == 'بازگشت 🔙':
        Is_in_second_page = False
        hi(userchatid)
    elif usertext =="file manager":
        read_saves(userchatid)
        txt = "for saving a new text -> /save {your text}\nfor sending a file's text -> 'read {file's code}'\nHome Page -> Home"
        bot.send_message(userchatid, txt)
    elif usertext.startswith('/read '):
        readfunc(usertext,userchatid)
    elif usertext.startswith('/save '):
        save(userchatid,usertext)
    elif usertext == '/save':
        bot.send_message(userchatid,'You should do this:\n/save [message]\nDo not use persian.')
    elif usertext == '/savelist':
        read_saves(userchatid)
    elif usertext == 'power options':
        poweroptions(userchatid)
    elif usertext == 'اتمام ازمون':
        endtest(userchatid)
    elif usertext == 'امتحان تشریحی':
        quiz_mode = 'on'
        bot.send_message(userchatid,'حالت امتحان تشریحی روشنه 📝',reply_to_message_id=usermessageid)
    elif usertext == 'ترجمه' or usertext == 'هن' or usertext == 'هن؟' or usertext == 'هن ؟':
        translate(user.reply_to_message.text,userchatid,usermessageid)
#==============================================================================================================================#
    elif usertext == "/sendphoto":
        sending_photo(userchatid)
    elif usertext == 'عکس تصادفی':
        rand_photo(userchatid)
    elif usertext == 'جستجوی موضوع عکس':
        taking_query = True
        bot.send_message(userchatid,'لطفا موضوع عکس رو به انگلیسی ارسال کنید')
    elif taking_query:
        query = usertext
        by_type_photo(query, userchatid)
    elif usertext == 'ترجمه 📖':
        bot.send_message(userchatid,'متن خود را تنها به زبان فارسی یا انگلیسی ارسال کنید تا به یکدیگر ترجمه شوند')
        trnslt = True
    elif trnslt:
        trnslt = False
        translate(usertext, userchatid, usermessageid)
    elif usertext == 'TO DO List ✔':
        todofunc(usermessageid, userchatid)
#==============================================================================================================================#
# Api Mode
    elif usertext == '🎞 دریافت اطلاعات یک فیلم':
        bot.send_message(userchatid, 'لطفا در حداقل دو پیام جداگانه اسم، ایدی معتبر imdb، سال انتشار و یا یکی از سه حالت movie, series, episode را ارسال کنید.\nیکی از دو پارامتر اسم یا ایدی فیلم لازم میباشد.')
        m_I = True
    elif m_I:
        m_Ifunc(usertext, userchatid)
#==============================================================================================================================#
    elif usertext == '/quizmode':
        quizmode_func(userchatid,usermessageid,usertext)
    for i in backend.view():
        if userchatid == i[0] and usertext == str(i[4]):
            quiez(userchatid)
#==============================================================================================================================#
    if Is_in_second_page and userchatid in user_id_list and user.chat.type == 'private':
        if usertext == 'بخش امتحان 〽️':
            # is_in_quiz_part = True
            quiz_part(userchatid)
        elif usertext == 'پنل مدیریت 💻':
            managerpanelfunc(userchatid)
        elif usertext == '🔙':
            is_in_quiz_part = False
            quiez(userchatid)
        elif usertext == '🗞 ارسال پیام به دیگران':
            s_m = True
            bot.send_message(userchatid,s_m_text)
        elif s_m:
            s_m_func(usertext,userchatid,usercaption)
#==============================================================================================================================#
        elif is_in_quiz_part:
            if searching:
                searchingfunc(userchatid,usermessageid,usertext)
            elif usertext == '🔙':
                is_in_quiz_part = False
                quiez(userchatid)
            elif getting_answer:
                getting_answer_func(usertext, userchatid)
#==============================================================================================================================#
            elif answering:
                answeringfunc(usertext, userchatid)
            elif usertext == 'پاکسازی لیست جواب ها 〽️':
                clearanswerlist(userchatid)
            elif clll:
                clllfunc(userchatid,usertext)
#==============================================================================================================================#
            elif usertext == 'ارسال جواب 📤':
                sendinganswerfunc(userchatid)
            elif usertext == 'جواب ها 📁':
                answersfunc(userchatid,usermessageid)
#==============================================================================================================================#
            elif usertext == '5 جواب اخر 📨':
                last5answers(userchatid, usermessageid)
            elif usertext == 'ایجاد تایمر امتحان ⏰':
                bot.send_message(userchatid, 'لطفا زمان امتحان را در حالت\nhh:mm:ss\nارسال کنید. منظور از دو  حرف اینت که باید عدد دو رقمی باشد\nیعنی حتی اگر ساعت تک رقتمی بود باید یک صفر قبل ان بگذارید')
                take_clock = True
            elif take_clock:
                take_clock_func(usertext,userchatid)
#==============================================================================================================================#
            elif usertext == 'جست و جو میان جواب ها 🔍':
                searchinanswersfunc(userchatid)
#==============================================================================================================================#
            elif usertext == 'دریافت زنده جواب ⏱📊':
                receiveliveanswer(userchatid)
#==============================================================================================================================#
            elif usertext == 'سوال ❓':
                internal_answer_person(userchatid)
            elif 'کد ' in usertext:
                codeintextfunc(usertext,userchatid)
#==============================================================================================================================#
            elif sending_back:
                sending_back_func(usertext,userchatid)
#==============================================================================================================================#
            elif usertext == '⬅️ ارسال پاسخ به کاربر':
                send_answer_to_member_func(userchatid)
            elif usertext == '⭕️ نادیده گرفتن ⭕️':
                ignore_func(userchatid)
#================================================================================== ============================================#
            elif usertext == '〽️ ارسال پیام پشتیبانی به کاربر':
                bot.send_message(send['q'],'☎️ پیام از طرف پشتیبانی : \n' + usertext)
#==============================================================================================================================#
            elif Message_to_Creator:
                Message_to_Creator_func(userusername,userchatid,usertext)
#==============================================================================================================================#
        if userchatid in admin_id_list:
            if Make_New_PassWord:
                makenewpasswordfunc(usertext,userchatid)
#==============================================================================================================================#
            elif new_person_name:
                # makenewpersonnamefunc()
                try:
                    new_person_nick_code = str(nickname_list_db[-1] + 1 )
                    new_person_Id = user.forward_from.id
                    nEW_p_pass = randint(100000,999999)
                    if nEW_p_pass in User_PassWord_inuse:
                        nEW_p_pass = randint(100000,999999)
                    subset_number = backend.search(id=userchatid)
                    backend.insert(int(new_person_Id), 'code ' + new_person_nick_code, new_person_nick_code, False, nEW_p_pass, False,subset_number[0][6])
                    bot.send_message(userchatid,'فرد جدید اضافه شد ✅')
                    Check_PassWord()
                    bot.send_message(userchatid,f'رمز ورور فرد جدید: |⨈| {nEW_p_pass} |⨈|')
                    nickname_list_db.append(new_person_nick_code)
                    new_person_name = False
                except:
                    bot.send_message(userchatid,'فرایند با مشکل مواجه شد ❌')
                    Check_PassWord()
                new_person_name = False
#==============================================================================================================================#
            elif Delete_Person:
                if Check_if_int(usertext):
                    if len(usertext) == 6:
                        Delete_Person_func(userchatid,entering_code=int(usertext))
                    if 6 < len(usertext):
                        Delete_Person_func(userchatid,id=int(usertext))
                    if int(usertext) in nickname_list_db and len(usertext) == 1:
                        Delete_Person_func(userchatid,code=usertext)
                else:  
                    if 'code ' in usertext:
                        Delete_Person_func(userchatid,nickname=usertext)
                    else:
                        bot.send_message(userchatid,'کاربری با این مشخصات پیدا نشد ❌')
                        Delete_Person = False
                        quiez(userchatid)
#==============================================================================================================================#
            elif usertext == '🚸 اضافه کردن فرد جدید':
                new_person_name = True
                bot.send_message(userchatid,'لطفا پیامی را از فرد جدیدی که میخاهید اضافه کنید را به ربات فروارد کنید')
                # اگه کسی فورواردش بسته باشه نمیتونه کار کنه اکسپشنش رو بنویس
            elif usertext == '⬅️ تغیر رمز عبور':
                pass_chang_btn = types.ReplyKeyboardMarkup(resize_keyboard=(1,2))
                pass_ch1 = types.KeyboardButton('👤 تغییر رمز افراد')
                pass_ch2 = types.KeyboardButton('🗣 تغییر رمز خود')
                pass_chang_btn.add(pass_ch1,pass_ch2)
                bot.send_message(userchatid,'🔅 لطفا نوع تغییر را مشخص کنید',reply_markup=pass_chang_btn)
            elif usertext == '🔰 افراد زیرمجموعه':
                admin_num = backend.search(id=userchatid)
                subsets = backend.search(subset_of=admin_num[0][6])
                TeXt_of_susets = '🔰 افراد زیر مجموعه شما : \n'
                for i in subsets:
                    if i[5] == 0:
                        TeXt_of_susets += f'|⨈| {i[1]} |⨈|\n'
                bot.send_message(userchatid,TeXt_of_susets)
#==============================================================================================================================#
            elif usertext == '👤 تغییر رمز افراد':
                bot.send_message(#طولانی شد اینتر زدم بره پایین
                    userchatid,
                    '☣️ لطفا یکی از پارامتر های مربوط به فرد را ارسال کرده تا رمز جدید و تصادفی را دریافت کنید:\nکد عددی\nکد به همراه کلمه کلیدی code (به همراه فاصله)\nرمز قدیمی\nایدی عددی'
                    )
                Check_PassWord()
                Make_New_PassWord = True
            elif usertext == '🗣 تغییر رمز خود':
                bot.send_message(userchatid,'☣️ لطفا متوجه باشید که رمزی تصادفی برای شما صورت میگیرد و امکان تایین رمز توسط خودتان وجود ندارد')
                try:
                    i_in_view = backend.search(id=userchatid)
                    User_New_Pass = randint(100000,999999)
                    if User_New_Pass in User_PassWord_inuse:
                        User_New_Pass = randint(100000,999999)
                    backend.update(i_in_view[0][0],i_in_view[0][1],i_in_view[0][2],
                    i_in_view[0][3],User_New_Pass,i_in_view[0][5],i_in_view[0][6])
                    Check_PassWord()
                    bot.send_message(userchatid,f'عملیات با موفقیت انجام شد ✅\nرمز عبور جدید شما : |⨈| {User_New_Pass} |⨈|')
                except:
                    bot.send_message(userchatid,'قرایند با مشکل مواجه شد ❌')
                    Check_PassWord()
#==============================================================================================================================#
            elif usertext == 'حذف کردن فرد 💢':
                bot.send_message(#طولانی شد اینتر زدم بره پایین
                    userchatid,
                    '☣️ لطفا یکی از پارامتر های مربوط به فرد را ارسال کرده تا فرد مورد نظر حذف شود (توجه کنید که این عمل برگشت پذیر نمی باشد):\nکد عددی\nکد به همراه کلمه کلیدی code (به همراه فاصله)\nرمز قدیمی\nایدی عددی'
                    )
                Check_PassWord()
                Delete_Person = True
#==============================================================================================================================#
            elif usertext == 'ارسال پیام 📡':
                c_to_s = types.ReplyKeyboardMarkup((1,2))
#==============================================================================================================================#
            elif usertext == '🖌 ارتباط با سازنده':
                bot.send_message(userchatid,'🔅 پیام خود را برای دریافت پشتیبانی یا سوال و جواب ارسال کنید\nتوجه کنید برای دریافت طرز کار ربات میتوانید از دستور \howbotworks استفاده کنید')
                send['q'] = userchatid
                send['a'] = Creator_ID
                Message_to_Creator = True
#==============================================================================================================================#
            elif usertext == '⏱ تمدید اعتبار':
                purchase_btn = types.InlineKeyboardMarkup()
                Prch_1 = types.InlineKeyboardButton('صفحه پرداخت','https://b2n.ir/669954')
                purchase_btn.add(Prch_1)
                bot.send_message(userchatid,'''لطفا با استفاده از دکمه زیر به صفحه واریز وارد شده\nمبلغ مورد نظر را واریز کرده
و سپس عکسی از رسید واریز گرفته و همراه با کد خود به بات ارسال کنید
توجه کنید که فرایند تایید ممکن است کمی طول بکشد
مبالغ : 
💵یک ماه : 12 تومن
💵دو ماه : 23 تومن
💵سه ماه : 30 تومن
💵شش ماه : 50 تومن
💵یک سال : 115 تومن''',reply_markup=purchase_btn)
#==============================================================================================================================#
        if userchatid == 1263524768 or userchatid == 394075806:
            if Delete_Admin:
                # hasn't tested yet
                if Check_if_int(usertext):
                    if len(usertext) == 6:
                        if backend.search(entering_code=int(usertext))[0][5]:
                            Delete_Person_func(userchatid,entering_code=int(usertext))
                        else:
                            bot.send_message(userchatid,'❌ فرد با این رمز ادمین نمی باشد\nلطفا حالت دیگری را امتحان کنید\n(جست و جو هنوز روشن است ‼️)')
                    if 6 < len(usertext):
                        if backend.search(id=int(usertext))[0][5]:
                            Delete_Person_func(userchatid,id=int(usertext))
                        else:
                            bot.send_message(userchatid,'❌ فرد با این ایدی ادمین نمی باشد\nلطفا حالت دیگری را امتحان کنید\n(جست و جو هنوز روشن است ‼️)')
                    if int(usertext) in nickname_list_db and len(usertext) <= 2 and backend.search(code=usertext)[0][5]:
                        Delete_Person_func(userchatid,code=usertext)
                else:
                    if 'code ' in usertext:
                        Delete_Person_func(userchatid,nickname=usertext)
                    else:
                        bot.send_message(userchatid,'کاربری با این مشخصات پیدا نشد ❌')
                        Delete_Admin = False
                        quiez(userchatid)
            if New_Admin_Person:
                try:
                    #مشکل نداره, فعلا تست نشده
                    # تست شد اوکیه. منتها اگه کد ادمینو وارد کنی انجام نمیده
                    Check_List()
                    Check_Admin_numbers()
                    new_person_nick_code = str(nickname_list_db[-1] + 1 )
                    new_person_Id = user.forward_from.id
                    nEW_p_pass = randint(100000,999999)
                    if nEW_p_pass in User_PassWord_inuse:
                        nEW_p_pass = randint(100000,999999)
                    subset_number = int(Admins_inside_db[-1] + 1)
                    backend.insert(int(new_person_Id), 'code ' + new_person_nick_code, new_person_nick_code, False, nEW_p_pass, True,subset_number)
                    bot.send_message(userchatid,'فرد جدید اضافه شد ✅')
                    Check_PassWord()
                    Check_Admin_numbers()
                    bot.send_message(userchatid,f'رمز ورور ادمین جدید: |⨈| {nEW_p_pass} |⨈|')
                    nickname_list_db.append(new_person_nick_code)
                    New_Admin_Person = False
                except:
                    bot.send_message(userchatid,'فرایند با مشکل مواجه شد ❌')
                    Check_PassWord()
                    New_Admin_Person = False
            # new_person_name = False
            if usertext == '🔚 بازگشت به منوی ادمین اصلی':
                main_admin(userchatid)
            elif usertext == 'افراد موجود 🙍‍♂️':
                TeXt_of_susets = '🔰 افراد موجود : \n'
                for i in backend.view():
                    if i[5]:
                        TeXt_of_susets += f'🤖Admin No.{i[6]} : \n'
                        subsets = backend.search(subset_of=i[6])
                        if subsets == []:
                            TeXt_of_susets += '       No Subsets yet!'
                        for j in subsets:
                            if j[5]:
                                continue
                            TeXt_of_susets += f'      👾{j[1]}\n'
                bot.send_message(userchatid,TeXt_of_susets)
            elif usertext == 'ادمین های موجود 🙍':
                TeXt_Of_Admins = 'ادمین های موجود : \n'
                for i in backend.view():
                    if i[5]:
                        TeXt_Of_Admins += f'  User : {i[1]}, Admin Code : {i[6]}'
                bot.send_message(userchatid,TeXt_Of_Admins)
            elif usertext == 'منوی ادمین عادی 📃':
                adminpanel(userchatid)
            elif usertext == 'اضافه کردن ادمین ❇️':
                New_Admin_Person = True
                bot.send_message(userchatid,'لطفا پیامی را از فرد جدیدی که میخاهید اضافه کنید را به ربات فروارد کنید')
            elif usertext == 'حذف ادمین 💢':
                bot.send_message(#طولانی شد اینتر زدم بره پایین
                    userchatid,
                    '📄 لطفا یکی از پارامتر های مربوط به فرد را ارسال کرده تا فرد مورد نظر حذف شود (توجه کنید که این عمل برگشت پذیر نمی باشد):\n📍 کد عددی\n📍 کد به همراه کلمه کلیدی code (به همراه فاصله)\n📍 رمز قدیمی\n📍 ایدی عددی'
                    )
                Check_PassWord()
                Check_Admin_numbers()
                Delete_Admin = True
    else:
        pass
        # bot.send_message(userchatid, "❌ This message is NOT among options")
        # Is_in_second_page = False
        # hi(userchatid)
#==============================================================================================================================#            
bot.polling(True)