
#создай приложение для запоминания информации
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('MEXAMER')
main_win.resize(500, 500)
question_l = QLabel('Какой национальности не существует?')
layout_quest = QVBoxLayout()




RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_quest.addWidget(question_l, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
layout_quest.addWidget(RadioGroupBox)





RadioGroupBox_answer = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft))
layout_res.addWidget(lb_Correct, alignment=(Qt.AlignCenter))
RadioGroupBox_answer.setLayout(layout_res)
layout_quest.addWidget(RadioGroupBox_answer)
RadioGroupBox_answer.hide()

btn_ok = QPushButton('Ответить')
layout_btn = QHBoxLayout()
layout_btn.addStretch(2)
layout_btn.addWidget(btn_ok)
layout_btn.addStretch(2)


layout_quest.addLayout(layout_btn)

main_win.setLayout(layout_quest)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


def show_result():
    RadioGroupBox.hide()
    RadioGroupBox_answer.show()
    btn_ok.setText('Следующий вопрос')


def show_question():
    RadioGroupBox_answer.hide()
    RadioGroupBox.show()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)






answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer =right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question_l.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

question_list = []
q1 = Question('Какая компания изобрела технологию RTX?', 'NVIDIA', 'MSI', 'ASUS', 'AMD')
q2 = Question('В каком году вышла игра "HALF-LIFE 2"?,', '2004', '2007', '2002', '2003')
q3 = Question('Сколько гигабайт видеопамяти у видеокарты 4090ti?', '24', '18', '16', '26')
q4 = Question('Сколько легенд  в Apex Legends 16 сезон?', '23', '25', '22', '26')
q5 = Question('Когда выйдет Counter Strike 2?', 'Июнь', 'Июль', 'Август', 'Уже вышла')

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)

cur_question = -1

def next_question():
    global cur_question, question_list
    cur_question = cur_question + 1
    if cur_question >= len(question_list):
        cur_question = 0
    q = question_list[cur_question]
    ask(q)    

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Неверно!')
 
 

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def btn_check():
    if btn_ok.text()=='Ответить':
        check_answer()
    else:
        next_question()


next_question()
btn_ok.clicked.connect(btn_check)




















main_win.show()
app.exec_()
