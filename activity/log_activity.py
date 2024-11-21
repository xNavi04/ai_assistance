def append_wrong_answer(time, question, answer):
    with open('../actions/log/log.txt', 'a', encoding='utf-8') as file:
        line = f"{time}  :  pytanie : {question} , odpowiedź : {answer}\n"
        file.write(line)