"""не использованы библиотеки, модули
формат .ipynb
цельный сюжет
концовки: 0/3
пользователь влияет на исход
условные конструкции: 1/4
цикл while: 1/1
цикл for: 1/1
методы списков и множеств: 2/2
готовый словарь: 0/1
словарь по ходу: 1/1
запись рута в файл
"""

YES = "да yes"
NO = "нет no"

def check_answer(answer):
    if answer in YES:
        return 1
    elif answer in NO:
        return 0

def ask_answer(variables):
    while True:
        answer = input()
        if answer in variables:
            break
    return answer

story_paths = {}    #готовый словарь с развилками
text = {}    #собирается по ходу
answers = []    #ответы пользователя


print('Дэн стоял у котла и готовил стандартный суп из акульего плавника. Воздух пах рыбой и солью. 
«Да… Дельфин» подумал он, не подозревая, что это акула. Он был стандартный моряк криминального толка, не сведущий в морской биологии, жаждущий богатств и роскошной жизни, вечно странствующий, но никогда не достигающий своих целей. Многие скажут, что он неудачник – но ему всё равно. Море, нажива, и  верный экипаж шхуны капитана Брэпси – вся его жизнь. 
Но в этот раз всё может быть по-другому. Приведете ли вы его к богатству и славе, или его ждет другая судьба? 

«Земля!» крикнул матрос с вороньего гнезда, и жизнь на корабле внезапно оживилась. Они были близко к своей цели – тот самый остров сокровищ. Игра начинается…
')

print("ПРибыли направо или налево")
if check_answert(ask_answer("".join([YES, NO]))):
    print("лютая смерть")
else:
    print("дошли до сокровища, брэпси - банубас")
    if check_answert(ask_answer("".join([YES, NO]))):
        print("тихо и стандартно")
    else:
        print("мир, да счастье. игра начинается")

"""
print("Блять, ладно, пора отправляться искать это сокровиша. Но сука, не зайти ли мне в кабака промочить глотку?")
print("ДА или НЕТ?")
secret_counter = 0
secret_answers = ["Не", "не"]
while secret_counter != 3:
    if check_answer(input()):
        if not secret_counter == 2: print(secret_answers[secret_counter])
        secret_counter+= 1
    else:
        break
else:
    print("секретная концовка")
"""

if check_answer(input()):
    answers.append(story_paths[][0])
else:
    answers.append(story_paths[][1])

text["title"] = "ТИХИЙ ДЕН: ИГРА НАЧИНАЕТСЯ\n\n"
for key in story_paths.keys():
    text[key] = answers.pop(0)

with open("story.txt", "w", encoding = "UTF-8") as final_story:
    for line in text.items():
        print(" ".join(line[1]), file = final_story)
