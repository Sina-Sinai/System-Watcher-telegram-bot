import re
def take_message(user):
    usertext = user.text
    usermessageid = user.message_id
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    if 'گزینه' in usertext:
        if 'شک' in usertext:
            match = re.search(r'(\d+)\=>(\d) (\w+)',usertext)
            question_number = match.group(1) + ' | شک |'
            answer_number = match.group(2)
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
        res = str(question_number) + ' : ' + answer
    if 'گزینه' not in usertext:
        if 'شک' in usertext:
            match = re.search(r'(\d+)\=>(\w+) (\w+)',usertext)
            question_txt = match.group(1) + ' | شک |'
            answer_txt = match.group(2)
        if 'شک' not in usertext:
            match = re.search(r'(\d+)\=>(\w+)',usertext)
            question_txt = match.group(1)
            answer_txt = match.group(2)
        res = str(question_txt) + ' : ' + str(answer_txt)
    return res