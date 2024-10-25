import time
import winsound
import music21

did_user_get_correct = None
user_input = False
answer_Streak = 0


# TODO: Add sound system for note identification
# TODO: anadir sistema para ver resultados
def quiz_timer():
    global user_input
    while user_input is False:
        try:
            index = int(input('input the amount of time you want for this quiz: \n30: 0\n60: 1\n90: 2\n180: 3\n'))
            quiz_times = [30, 60, 90, 180]
            quiz_time = quiz_times[index]
            print(f'you have chosen {quiz_time} as the amount of time for this quiz')
            user_input = True
            return quiz_time
        except ValueError:
            print('invalid input, please choose an index: ')
            continue
        except IndexError:
            print('invalid index, please choose valid index: ')
            continue
