from PyQt5.QtWidgets import QApplication

app = QApplication([])

from main_window import *

def show_result():
    '''показати панель питань'''
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання')

def show_question():
    ''' показати панель завдань'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_data():
    ''' показує потрібну інформацію на екрані'''

    lb_Question.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def check_result():
    ''' перевірка, чи правильна відповідь обрана
    якщо відповідь була обрана, то напис "правильно/
    значення і показується панель відповідей
    '''
    correct = answer.isChecked()
    if correct:

        lb_Result.setText(text_correct)
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:

            lb_Result.setText(text_wrong)
            show_result()

def click_OK(self):

    if btn_OK.text() != 'Наступне питання':
        check_result()

show_data()
show_question()
btn_OK.clicked.connect(click_OK)

app.exec_()