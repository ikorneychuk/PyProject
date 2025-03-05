"""не использованы библиотеки, модули
формат .ipynb
цельный сюжет
концовки: 0/3
пользователь влияет на исход
условные конструкции: 1/4
цикл while: 0/1
цикл for: 1/1
методы списков и множеств: 2/2
готовый словарь: 0/1
словарь по ходу: 1/1
запись рута в файл
"""

def check_answer(answer):
    if answer == "Да" or answer == "Yes" or answer == 'y' or answer == 'Y':
        return 1
    if answer == "Нет" or answer == "No" or answer == 'n' or answer == 'N':
        return 0

story_paths = {}
text = {}
answers = []



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
