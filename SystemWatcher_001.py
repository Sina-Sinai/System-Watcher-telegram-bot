import telebot
from telebot import types
from random import randint
import re
from os import system,walk
#from playsound import playsound
#==============================================================================================================================#
TOKEN = '1248089764:AAFAueuihRk7hMVkWgMAyL8o5tEOBPHqU04'
bot = telebot.TeleBot(TOKEN)
#==============================================================================================================================#
channel_id = '-1001204622260'
group_id = '-1001395959886'
#==============================================================================================================================#
ready_message = '''ربات اماده امتحان است
لطفا پاسخ هر سوال را با این فرمت ارسال نمایید 
تا ربات توانایی تشخیص سوال و گزینه مربوطه را داشته باشد

(شماره گزینه<=شماره سوال)
102=>2
**اگر به صورت عادی چه فارسی و چه انگلیسی تایپ کنید پیام شما به این صورت ارسال میشود**

لطفا فاصله نگذارید مگر برای گذاشتن "شک" که با یک فاصله بعد از شماره گزینه

(Q=>A) or (Q=>A شک)"اگر شک داشتید"

|?|  در لیست به معنای شک است
**نیازی به قراردادن پرانتز نیست**
'''
#==============================================================================================================================#
answer_list = {}
answer_l = []
code_list = {'سینا':'کد 001','B':'کد 002','Isyan Tetick':'کد 003','Deleted':'کد 004','ali':'کد 005','Salar':'کد 006','ᎰᎪᏞᏞᎬN':'کد 007'}
id_list = {'001':'1263524768','002':'1250041126','003':'1499841944','004':'1414632095','005':'1287889248','006':'1498008651','کد 007':'1149573041'}
live_id_list = {'1263524768':False,'1250041126':False,'1499841944':False,'1414632095':False,'1287889248':False,'1498008651:':False,'1149573041':False}
Allowed_chat_id = []
send = {}
taking_answ = ''
admin_id_list = []
getting_answer = False
robot = ''
dfgsdf = ''
quiz_mode = ''
#==============================================================================================================================#
m_i = None
text = ''
ttttt = ''
sending_back = False
answering = None
searching = False
live = False
first_message = '***answer list***'
system('cls')
print('Bot is Ready !')
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
@bot.edited_message_handler(content_types=['text'])
def edited_message_botmain(user):
    botmain(user)
#==============================================================================================================================#
def quiez(userchatid):
    secret_btn = types.ReplyKeyboardMarkup(resize_keyboard=(1,2),row_width=2)
    secret_1 = types.KeyboardButton('جواب ها 📁')
    secret_2 = types.KeyboardButton('ارسال جواب 📤')
    secret_3 = types.KeyboardButton('جست و جو میان جواب ها 🔍')
    secret_4 = types.KeyboardButton('5 جواب اخر 📨')
    secret_5 = types.KeyboardButton('دریافت زنده جواب ⏱📊')
    secret_6 = types.KeyboardButton('سوال ❓')
    secret_7 = types.KeyboardButton('پنل مدیریت 💻')
    secret_8 = types.KeyboardButton('بازگشت 🔙')
    secret_btn.add(secret_1,secret_2,secret_3,secret_4,secret_5,secret_6,secret_7,secret_8)
    bot.send_message(userchatid,'به صفحه دوم 😈 خوش امدید',reply_markup=secret_btn)
    #playsound('music.mp3')
#==============================================================================================================================#
def adminpanel(userchatid):
    admin_btn = types.ReplyKeyboardMarkup(resize_keyboard=(1,2),row_width=2)
    admin1 = types.KeyboardButton('اضافه کردن فرد جدید')
    admin2 = types.KeyboardButton('تغیر رمز عبور')
    admin4 = types.KeyboardButton('ارتباط با سازنده')
    admin5 = types.KeyboardButton('بازگشت 🔙')
    admin_btn.add(admin1,admin2,admin4,admin5)
#==============================================================================================================================#
def internal_answer_person(userchatid):
    q_btn = types.ReplyKeyboardMarkup(resize_keyboard=(1,2),row_width=2)
    q1 = types.KeyboardButton('کد 001')
    q2 = types.KeyboardButton('کد 002')
    q3 = types.KeyboardButton('کد 003')
    q4 = types.KeyboardButton('کد 004')
    q5 = types.KeyboardButton('کد 005')
    q6 = types.KeyboardButton('کد 006')
    q_btn.add(q1,q2,q3,q4,q5,q6)
    bot.send_message(userchatid,'از چه کسی سوال دارید؟',reply_markup=q_btn)
#==============================================================================================================================#
def internal_answer(userchatid,to_id):
    #print(userchatid)
    #print(to_id)
    global send, getting_answer
    getting_answer = True
    a_btn = types.ReplyKeyboardMarkup(resize_keyboard=(1,2))
    a1 = types.KeyboardButton('پایان')
    a_btn.add(a1)
    send['q'] = userchatid
    send['a'] = to_id
    #print(send)
    bot.send_message(userchatid,'لطفا سوال خود را بپرسید و بعد روی پایان کلیک کنید',reply_markup=a_btn)
#==============================================================================================================================#
def hi(userchatid):
    #print(userchatid)
    dokmeha = types.ReplyKeyboardMarkup(row_width=2)
    dokme1 = types.KeyboardButton('Take a screenshot')
    dokme2 = types.KeyboardButton('file manager')
    dokme3 = types.KeyboardButton('play sound')
    dokme4 = types.KeyboardButton('power options')
    dokmeha.add(dokme1,dokme2,dokme3,dokme4)
    bot.send_message(userchatid,'Hi 😊 what can i do for you?',reply_markup=dokmeha)
#==============================================================================================================================#
def save(userchatid,usertext):
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
    listt = []
    index = 0
    a = open('dictionary.txt','r+',encoding='UTF8')
    b = a.readline()
    for i in userreplytext:
        listt.append(i)
        while i != b[0]:
            b = a.readline()
        listt.pop(index)
        listt.append(b[2])
        index += 1
    a.close()
    c = ''.join(listt)
    bot.send_message(userchatid,c,reply_to_message_id=usermessageid)

#==============================================================================================================================#
def take_message(user):
    global answer_list, first_message,m_i
    usertext = user.text
    usermessageid = user.message_id
    userchatid = user.chat.id
    if 'گزینه' not in usertext:
        if 'شک' in usertext and '=>' in usertext:
            match = re.search(r'(\d+)=>',usertext)
            question_number = match.group(1)
            usertext = usertext.replace(match.group(1),'')
            usertext = usertext.replace('=>',' ')
            for i in usertext:
                if i.isdigit() and i is not ' ':
                    bot.send_message(userchatid,'اگر در امتحان تشریحی سوالی تستی بود از کلمه کلیدی "گزینه" بعد از نوشتن جواب  استفاده کنید')
                else:
                    answer_text = usertext + 'شک داریم     '
        elif '=>' in usertext and 'شک' not in usertext:
            match = re.search(r'(\d+)=>',usertext)
            question_number = match.group(1)
            usertext = usertext.replace(match.group(1),'')
            usertext = usertext.replace('=>','')
            answer_text = usertext
        answer_list[question_number] = answer_text
        first_message += f'\nQ : | {question_number} | A : {answer_list[question_number]}'
        bot.edit_message_text(first_message,channel_id,m_i)
        
    elif 'گزینه' in usertext:
        if 'شک' in usertext:
            match = re.search(r'(\d+)\=>(\d)',usertext)
            question_number = match.group(1)
            answer_number = match.group(2) + ' | شک |'
        if 'شک' not in usertext:
            match = re.search(r'(\d+)\=>(\d)',usertext)
            question_number = match.group(1)
            answer_number = match.group(2)
        if answer_number == '1':
            answer = '1️⃣⬛⬛⬛'
        elif answer_number == '2':
            answer = '⬛2️⃣⬛⬛'
        elif answer_number == '3':
            answer = '⬛⬛3️⃣⬛'
        elif answer_number == 4:
            answer = '⬛⬛⬛4️⃣'
        elif answer_number == '0':
            answer = '⬛⬛⬛⬛'
        res = first_message+'\n'+str(question_number) + ' : ' + answer
        bot.edit_message_text(res,channel_id,m_i)
#==============================================================================================================================#
def sorting(usermessageid,userchatid):
    global answer_list
    text = '*** |Answer List| ***\n'
    if answer_list != {}:
        for i in answer_list:
            if '|?|' not in answer_list[i]:
                text += f'Q : |{i}| A : |{answer_list[i]}|\n'
            if '|?|' in answer_list[i]:
                text += f'Q : |{i}| A : |{answer_list[i]}| |?|\n'
        bot.send_message(userchatid,text,reply_to_message_id=usermessageid)
    else:
        bot.send_message(userchatid,'هنوز سوالی نفرستادی که از من لیست سوالارو میخای داداش 😐😐',reply_to_message_id=usermessageid)
#==============================================================================================================================#
def poweroptions(userchatid):
    dokmeha = types.ReplyKeyboardMarkup()
    dokme1 = types.KeyboardButton('Shut down')
    dokme2 = types.KeyboardButton('Restart')
    dokme3 = types.KeyboardButton('Home')
    dokmeha.add(dokme1,dokme2,dokme3)
    bot.send_message(userchatid,'Welcome to poweroption menu',reply_markup=dokmeha)
#==============================================================================================================================#
def showhelp(usermessageid,userchatid):
    tttxt = '''.......................................⨌⨌لیست دستورات⨌⨌.............................................
=========================================================
                                             /help   ———--------------     اسمش روشه بیسواد :/
========================================================= 
 """ربات اماده""" -—————--————— ربات رو اماده امتحان میکنه
=========================================================
                                          /resort    ———————سوالا میگره برات میفرسته
=========================================================
                                            /clsort   -———----—--  لیست سوالارو خالی میکنه
=========================================================
"""اتمام ازمون""" ——-———————— دیگه سوالارو نمیگیره (خاموش)'''
    bot.send_message(userchatid,tttxt,reply_to_message_id=usermessageid)
#==============================================================================================================================#
def clsort(usermessageid,userchatid):
    global answer_list
    answer_list = {}
    bot.send_message(userchatid,'لیست سوالات پاک شد', reply_to_message_id=usermessageid)
#==============================================================================================================================#
@bot.message_handler(content_types=['photo'])
def photo_hadler(user):
    pass
#==============================================================================================================================#
@bot.message_handler(content_types=['text'])
def botmain(user):
    global m_i, first_message, answer_list, robot, quiz_mode, answering, searching, live, code_list, taking_answ, send, getting_answer
    global sending_back, ttttt, live_id_list, dfgsdf, admin_id_list
    admin = 'ALSPOUR'
    usertext = user.text
    usermessageid = user.message_id
    userchatid = user.chat.id
    userfirstname = user.chat.first_name
    #print(userfirstname, userchatid)
    if usertext == 'ربات اماده':
        m_i = bot.send_message(channel_id,'***answer list***').message_id
        bot.send_message(userchatid,ready_message)
        robot = 'ربات اماده'
    if robot == 'ربات اماده':
        if quiz_mode == 'on' and '=>' in usertext:
            take_message(user)
        if robot == 'ربات اماده' and quiz_mode != 'on':
            try:
                if 'شک' in usertext and '=>' in usertext:
                    match = re.search(r'(\d+)\=>(\d) (\w+)',usertext)
                    #bot.send_message(userchatid,match.group(0))#the hole message
                    ##bot.send_message(userchatid,match.group(1))#question number
                    ##bot.send_message(userchatid,match.group(2))#answer number
                    ##bot.send_message(userchatid,"شک")
                    question_number = match.group(1)
                    answer_number = match.group(2)
                elif '=>' in usertext and not 'شک' in usertext:
                    match = re.search(r'(\d+)\=>(\d)',usertext)
                    #bot.send_message(userchatid,match.group(0))#the hole message
                    ##bot.send_message(userchatid,match.group(1))#question number
                    ##bot.send_message(userchatid,match.group(2))#answer number
                    question_number = match.group(1)
                    answer_number = match.group(2)
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
                    if int(answer_number) < 5:
                        answer_list[question_number] = str(answer_number)
                        first_message += '\nQ : | '+str(question_number)+' |'+' A : | '+answer_number+' | |?|'
                        bot.edit_message_text(first_message,channel_id,m_i)
                    else:
                        bot.send_message(userchatid,'شماره گزینه باید از 1 تا 4 باشد 😐',reply_to_message_id=usermessageid)
                elif '=>' in usertext and 'شک' not in usertext:
                    if int(answer_number) < 5:
                        answer_list[question_number] = str(answer_number)
                        first_message += '\nQ : | '+str(question_number)+' |'+' A : | '+answer_number+' |'
                        bot.edit_message_text(first_message,channel_id,m_i)
                    else:
                        bot.send_message(userchatid,'شماره گزینه باید از 1 تا 4 باشد 😐',reply_to_message_id=usermessageid)
            except Exception as Error:
                print(Error)
                if str(Error) == 'A request to the Telegram API was unsuccessful. Error code: 400 Description: Bad Request: message to edit not found':
                    m_i = bot.send_message(channel_id,'***answer list***').message_id
                    botmain(user)
                else:
                    bot.send_message(userchatid,
                    'لطفا با فرمت درست دوباره ارسال فرمایید**شماره گزینه<=شماره سوال**\nاول گزینه سوالو بنویس بعد یه = بزار بعد یه < بزار که شبیه فلش بشه، خب؟\nبعد هم شماره گزینه رو بنویس\nاگه شک داشتی بعد از شماره گزینه یه فاصله بزن بعد بنویس "شک" تمام :)',
                    reply_to_message_id=user.message_id)
#==============================================================================================================================#
    if usertext == '/resort':
        sorting(usermessageid,userchatid)
    if usertext == '/clsort':
        clsort(usermessageid,userchatid)
    if usertext == '/help':
        showhelp(usermessageid,userchatid)
    if usertext == '/start' or usertext == 'Home' or usertext == 'بازگشت 🔙':
        hi(userchatid)
    if usertext.startswith('/save '):
        save(userchatid,usertext)
    if usertext == '/save':
        bot.send_message(userchatid,'You should do this:\n/save [message]\nDo not use persian.')
    if usertext == '/savelist':
        read_saves(userchatid)
    if usertext == 'power options':
        poweroptions(userchatid)
    if usertext == 'اتمام ازمون':
        robot = ''
        quiz_mode = ''
    if usertext == 'امتحان تشریحی':
        quiz_mode = 'on'
        bot.send_message(userchatid,'حالت امتحان تشریحی روشنه',reply_to_message_id=usermessageid)
#==============================================================================================================================#
    if usertext == 'ربات':
        bot.send_message(userchatid,'هستم داداش، جونم؟',reply_to_message_id=usermessageid)
    if usertext == '/quizmode':
        q_m = ''
        if robot == 'ربات اماده' and quiz_mode == 'on':
            q_m += 'حالت امتحان عادی و تشریحی فعاله'
        elif robot == 'ربات اماده' and quiz_mode != 'on':
            q_m += 'حالت امتحان عادی فعاله'
        else:
            q_m += 'حالت امتحان فعال نیس'
        bot.send_message(userchatid,q_m,reply_to_message_id=usermessageid)
    if searching:
        ttt = ''
        for i in answer_l:
            if usertext in i:
                ttt += i + '\n'
        bot.send_message(userchatid,ttt,reply_to_message_id=usermessageid)
    if getting_answer:
        if usertext == 'پایان':
            #print(taking_answ)
            qqq = types.ReplyKeyboardMarkup(resize_keyboard=(1,2))
            qqq1 = types.KeyboardButton('ارسال پاسخ به کاربر')
            qqq2 = types.KeyboardButton('نادیده گرفتن')
            qqq.add(qqq1,qqq2)
            bot.send_message(send['a'],f'پیام از طرف کابر |⨈|{code_list[userfirstname]}|⨈| : \n' + taking_answ,reply_markup=qqq)
            #print(taking_answ)
            getting_answer = False
            taking_answ = ''
            quiez(userchatid)
        else:
            taking_answ += usertext + '\n'
            #print(taking_answ)
        #print(getting_answer)
    if answering:
        if usertext == 'تمام':
            answering = False
            quiez(userchatid)
        else:
            dfgsdf = str(f'|⨈{code_list[userfirstname]}⨈| : \n {usertext}')
            answer_l.append(dfgsdf)
            for i in live_id_list:
                if live_id_list[i]:
                    bot.send_message(i,dfgsdf)
    if usertext == 'ترجمه':
        translate(user.reply_to_message.text,userchatid,usermessageid)
#==============================================================================================================================#
    if usertext == '818504' and userchatid == 1263524768:#sina
        quiez(userchatid)
    if usertext == '818504' and userchatid == 394075806:#sina1
        quiez(userchatid)
    if usertext == '456428' and userchatid == 1250041126:#yadol
        quiez(userchatid)
    if usertext == '971494' and userchatid == 1499841944:#rasol
        quiez(userchatid)
    if usertext == '471302' and userchatid == 1414632095:#fallah
        quiez(userchatid)
    if usertext == '651851' and userchatid == 1287889248:#mntzry
        quiez(userchatid)
    if usertext == '151660' and userchatid == 1498008651:#sasan
        quiez(userchatid)
    if usertext == '781177' and userchatid == 1149573041:#mammad
        quiez(userchatid)
#==============================================================================================================================#
    if usertext == 'ارسال جواب 📤':
        answering = True
        botton = types.ReplyKeyboardMarkup(resize_keyboard=(1))
        btn1 = types.KeyboardButton('تمام')
        botton.add(btn1)
        bot.send_message(userchatid,'لطفا جواب های خود را ارسال کنید و سپس گزینه تمام را بزنید',reply_markup=botton)
    if usertext == 'جواب ها 📁':
        t = ''
        if answer_l != []:
            for i in answer_l:
                t += i + '\n'
            bot.send_message(userchatid,t,reply_to_message_id=usermessageid)
        else:
            bot.send_message(userchatid,'هنوز هیچ جوابی دریافت نشده است')
    if usertext == '5 جواب اخر 📨':
        if answer_l != []:
            t = answer_l[-5:]
            te = ''
            for i in t:
                te += i + '\n'
            bot.send_message(userchatid,te,reply_to_message_id=usermessageid)
        else:
            bot.send_message(userchatid,'هنوز هیچ جوابی دریافت نشده است')
    if usertext == 'جست و جو میان جواب ها 🔍':
        if answer_l != []:
            searching = True
            bot.send_message(userchatid,'لطفا کلمه ای که میخاهید در میان جواب ها جست و جو شود را ارسال کنید')
        else:
            bot.send_message(userchatid,'هنوز هیچ جوابی دریافت نشده است')
    if usertext == 'دریافت زنده جواب ⏱📊':
        #bot.send_message(userchatid,'این بخش هنوز فعال نیست')
        if live_id_list[str(userchatid)]:
            live_id_list[str(userchatid)] = False
            bot.send_message(userchatid,'دریافت زنده جواب خاموش شد')
        else:
            live_id_list[str(userchatid)] = True
            bot.send_message(userchatid,'دریافت زنده جواب روشن شد')
#==============================================================================================================================#
    if usertext == 'سوال ❓':
        internal_answer_person(userchatid)
    if usertext == 'کد 001':
        internal_answer(userchatid,id_list['001'])
    if usertext == 'کد 002':
        internal_answer(userchatid,id_list['002'])
    if usertext == 'کد 003':
        internal_answer(userchatid,id_list['003'])
    if usertext == 'کد 004':
        internal_answer(userchatid,id_list['004'])
    if usertext == 'کد 005':
        internal_answer(userchatid,id_list['005'])
    if usertext == 'کد 006':
        internal_answer(userchatid,id_list['006'])
    if usertext == 'کد 007':
        internal_answer(userchatid,id_list['007'])
    if sending_back:
        if usertext == 'اتمام پاسخ دهی':
            #print(ttttt)
            bot.send_message(send['q'],'در پاسخ به سوال شما : \n' + ttttt)
            sending_back = False
            send = {}
            quiez(userchatid)
        else:
            ttttt += usertext + '\n'
            #print(ttttt)
    if usertext == 'ارسال پاسخ به کاربر':
        eee = types.ReplyKeyboardMarkup(resize_keyboard=(1,2))
        eee1 = types.KeyboardButton('اتمام پاسخ دهی')
        eee.add(eee1)
        bot.send_message(userchatid,'لطفا پاسخ خود به کاربر را وارد نمایید و سپس اتمام را بزنید',reply_markup=eee)
        sending_back = True
    if usertext == 'نادیده گرفتن':
        send = {}
        sending_back = False
        quiez(userchatid)
#==============================================================================================================================#
    # if usertext == 'پنل مدیریت 💻':
    #     if userchatid == 1263524768 or userchatid == 394075806:
    #         main_admin()
    #     else:
    #         if userchatid in admin_id_list:
    #             adminpanel(userchatid)
    #         else:
    #             bot.send_message(userchatid,'شما دسترسی ادمین ندارید')
#==============================================================================================================================#
bot.polling(True)