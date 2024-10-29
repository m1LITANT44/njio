import random
import time
import keyboard
from datetime import datetime


print("Добро пожаловать в игру 'Время на размылшения'!")
start_game_time = datetime.now()
print(f"Время начала игры: {start_game_time.strftime('%H:%M:%S')}")

print("Нажмите клавишу ...")
possible_keys = ['enter', 'space', 'tab', 'backspace', 'ecs', 'delete', 'end',
                'page up', 'page down', 'up', 'down', 'left', 'right', 'shift',
                'ctrl', 'alt']


#цикл игры
num_rounds = random.randint(0,4)
reaction_times = []
for round in range(num_rounds):
    print(f'Раунд {round + 1}')
    wait_time = random.randint(1,3)
    #time.sleep(wait_time)
    starting_reaction = time.time()
# ожидание нажатия клавиши
    print(f'Нажмите {random.choice(possible_keys)} для начала ...')
    knopka = random.choice(possible_keys)
    print(knopka)

    while True:
        if keyboard.is_pressed(random.choice(knopka)):
            break
    end_reaction = time.time()
    difference = end_reaction - starting_reaction
    reaction_times.append(difference)
    sum_reaction = sum(reaction_times)
    end_game_time = datetime.now()
print(f"Время окончания игры:{end_game_time.strftime('%H:%M:%S')}")

total_duration = end_game_time - start_game_time
print(f"Общее время игры:{total_duration.total_seconds():.2f} секунд")
