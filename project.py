#константы для проверки ввода
YES = "да yes"
NO = "нет no"

#проверка ответа
def check_answer(answer):
    if answer in YES:
        return 1
    elif answer in NO:
        return 0

#запрос ответа
def ask_answer(variables):
    while True:
        answer = input().lower()
        if answer in variables:
            break
    return answer

#рестарт игры в случае первой концовки
def restart(answer):
    answers = []
    text = {}
    if answer in YES:
        print(story_paths["title"], story_paths["intro"], story_paths["intermission_1"], story_paths["path_1"], sep = "")    #начало
        if check_answer(ask_answer("".join([YES, NO]))):    #первый выбор
            print(story_paths["answer_1"][0])
            answers.append(story_paths["answer_1"][0])
            restart(ask_answer("".join([YES, NO])))    #рестарт по желанию
        else:
            print(story_paths["answer_1"][1], story_paths["path_2"])
            answers.append(story_paths["answer_1"][1])
            if check_answer(ask_answer("".join([YES, NO]))):    #второй выбор
                print(story_paths["answer_2"][0])
                answers.append(story_paths["answer_2"][0])
            else:
                print(story_paths["answer_2"][1])
                answers.append(story_paths["answer_2"][1])
   
        for item in story_paths.items():    #добавление сюжета в переменную для записи в файл
            if type(item[1]) is not type([]): 
                text[item[0]] = item[1]
            else:
                if answers[0].endswith("Начать заново?"):
                    answers[0] = answers[0].replace("Начать заново?", "")
                    text[item[0]] = answers.pop(0)    #работа с пользовательскими ответами
                else:
                    text[item[0]] = answers.pop(0)
                if len(answers) == 0:
                    break
                    
        with open("story_new.txt", "w", encoding = "UTF-8") as final_story:    #запись в файл
            for line in text.items():
                print("".join(line[1]), file = final_story)
                
    elif answer in NO:
            print('Спасибо за игру!')

#весь сюжет
story_paths = {"title":"ТИХИЙ ДЕН: ИГРА НАЧИНАЕТСЯ\n\n",
                "intro":"Дэн стоял у котла и готовил стандартный суп из акульего плавника. Воздух пах рыбой и солью.\n«Да… Дельфин» подумал он, не подозревая, что это акула. Он был стандартный моряк криминального толка, не сведущий в морской биологии, жаждущий богатств и роскошной жизни, вечно странствующий, но никогда не достигающий своих целей. Многие скажут, что он неудачник – но ему всё равно. Море, нажива, и  верный экипаж шхуны капитана Брэпси – вся его жизнь.\nНо в этот раз всё может быть по-другому. Приведете ли вы его к богатству и славе, или его ждет другая судьба?\n«Земля!» крикнул матрос с вороньего гнезда, и жизнь на корабле внезапно оживилась. Они были близко к своей цели – тот самый остров сокровищ. Игра начинается…\n",
                "intermission_1":"Песчаные, нетронутые пляжи, перетекающие в густые, темные джунгли… Островок, на котором они высадились, был абсолютно безлюдным, но за одним исключением. Вдали, на лужайке стояло крохотное здание, походящее на запылившийся комод. Приблизившись, можно было разглядеть манящую надпись над дверью: «BAR».\nГоловорезы, чей запас грога уже давным-давно иссяк, без лишних раздумий и вопросов побежали к загадочному строению в надеждах найти там спиртное. Похоже, людей там не было, но запасов предостаточно: старый товарищ Дэна, Бобc, уже вынес целый ящик с бутылками, празднуя распивал пойло. «Айда с нами, Дэн!» прокричал Бобc. По лицу Дэна потихоньку растягивалась улыбка. «Да… я бы сейчас выпил четыре или пять пинт грога…» подумал он, и его ноги уже будто сами плелись в сторону «бара».\nНо некоторые пираты устремили свой взор в совсем другое место. Поодаль, у корабля, капитан Брэпси собрал вокруг себя кучку людей, всех устремивших свой взор вниз, будто все они что-то разглядывали. Точно, карта сокровищ! Они что-то задумали, но не оставят же они всех остальных? Дэна смяло сомнение, что-то во всём это было зловещее.\n",
                "path_1":"Решайте, пойдет ли Дэн в бар?\n",
                "answer_1":["Не пойти с другом выпить – что за вздор! К чёрту этих заговорщиков, подумал Дэн, и поддался своему нутру, жаждущему рома.\nПосиделки были весёлые: последнее что Дэн помнит, это как ему разбили бутылку об голову после его однозначно честной победы в армрестлинге против этого проклятого штурмана. Пляски, песни, истории… Всё это перемешалось в одну темную массу, как ром, которым был полон его живот.\nНовый день встретил Дэна рассветом. Он проснулся один, на пляже, где-то около «бара». Море приятно шумело, чайки подпевали.\nНо когда он поднял голову, в его взор врезалась деталь. Корабль! Его нигде нет! Внезапный прилив крови ударил по ослабшему от алкоголя сердцу матроса, и его голова закружилась, увалив его обратно в мир снов. Из которого он никогда не выйдет…\nАлкоголь – это яд!\nКонец! Начать заново?", "Как бы не манили Дэна радостные возгласы и запах спиртного – капитан просто так собирать команду не будет. Подходя ближе к кучке, он начал слышать как Капитан рассуждал о каком-то плане. Когда он был уже совсем близко, капитан внезапно поднял голову и его глаза широко открылись, смотря прямо на Дэна. За ним повторили и остальные тринадцать матросов.\n«О! Ты, матрос, и будешь нести мешок с лопатами. Я никогда не обсчитываюсь, нас пятнадцать!» – сказал капитан. Что-то в его лице было подозрительным.\n«Вот зараза! Без бухла, еще и тащить что-то?» подумал Дэн. Но его глаза сразу упали на то, что было в руках капитана – это же действительно карта! Те самые сокровища, можно и поработать недолго!\n«Ну что-ж, я думаю все всё поняли. Выдвигаемся, сейчас же, не теряя ни минуты! Нам надо успеть до заката», —свернув карту сказал капитан Брэпси, и тотчас выдвинулся в сторону джунглей. Предстояла долгая дорога. \nПрошел один… Нет, два… Может, три… Кто его знает, сколько часов, солнца не было видно за густой листвой деревьев в джунглях, но дорога легче не становилась. Мешок давил на плечи и спина начинала скрипеть, инструменты неудобно выпирали в разные стороны, вызывая дискомфорт и мешая двигаться. Но Дэн не отставал – если уж идти за сокровищем, то не падать духом и дойти до него, тихо и стандартно. \n«Стоп! Мы на месте» – воодушевленно гавкнул капитан. «Три пенька, два камня… да! Копайте здесь.»\n«Наконец-то можно скинуть этот тяжелющий мешок…» подумал Ден. Другие матросы так же облегчённо вздохнули, некоторые уже предвкушали вид богатств. Уставший Дэн уселся неподалёку под деревом. Джунгли были такими густыми, что его со всех сторон окутывал папоротник. Все разобрали лопаты и принялись за работу. Как вдруг…\nЗвук выстрела. Затем еще один, и еще один. Дым мушкетов поднялся ввысь. Рядом с Дэном упал один из его товарищей, выронив свой пистолет. Засада! Но похоже, самого Дэна не заметили. Раздался коварный смех, напоминавший карканье вороны. Дэн в страхе выглянул из-за дерева, чтобы посмотреть, что происходит.\nЦелый отряд облаченных в черное головорезов, вооруженных до зубов. Откуда они взялись? И капитана нигде не видать. Странная таверна из ниоткуда, непонятные условия, глубина джунглей… Неужели это всё была ловушка?\n«Муа-ха-ха! Глупцы! Капитан Брэпси и его команда дураков! Мы вас обыграли, словно скрипку! Ха-ха-ха! Копайте дальше, и может мы оставим вас в живых, в отличие от вашего капитана... Этому предателю давно была уготована черная метка»\n«Банубас… Пошел ты, Банубас!» со злостью подумал Дэн. Лицо насмехающегося головореза: наконец он понял, что он увидел с утра в лице капитана. Всё это время это был мерзкий капитан Банубас, заклятый враг Брэпси, лишь притворявшийся им! Пришел судьбоносный час: рискнуть шкурой ради товарищей, или выждать лучшего момента для себя самого…"],
                "path_2":"Помочь товарищам?\n",
                "answer_2":["Нельзя оставлять друзей в беде! Взор Дэна упал на пистолет его раненого товарища рядом – он еще заряжен.\nПора рискнуть и отдать свою судьбу в руки шанса! Дэн схватил пистолет, взвёл замок и сделал выстрел в Банубаса, который тут же упал. Растерявшиеся головорезы разом переключили свое внимание на Дэна, и с перепугу один из них сразу шмальнул в его сторону. Жгучая боль пронзила руку Дэна, заставив его скорчиться и упасть, как Папа Карло. Сознание его было одолено болью, и начало покидать его…\nНо смышленные пираты Брэпси тотчас пустились в рукопашную! Лопатами, камнями и ножами они ударили по растерявшимся разбойникам, сбитых с толку внезапным и точным ударом Дэна. \nДэн очнулся уже на корабле от резкого запаха какого-то снадобья, напоминавшего ему о майских жуках. Его рана была перебинтована, а вокруг него стояли его товарищи-матросы. \n«Живой!» вскрикнул штурман, «Ты спас шкуру всех нас Дэн! До дна за этого морского волка, и за пиастры что мы отыскали!»\n«Я делал всё… стандартно. Так сделал бы любой. Игра начинается...» вспоминал Дэн о тех днях спустя несколько месяцев, став капитаном этого судна. Фортуна в тот день была на его стороне, и он использовал ее на благо остальных! Так началась новая история капитана Дэна и слава о его приключениях разлетелась на весь мир, оставшись в истории на век.  \nКонец! Спасибо за игру!", "Когда ты в двух шагах от груды сказочных богатств, нельзя рисковать понапрасну! Пока удрученные матросы принялись копать дальше под мушкой свиты Банубаса, Дэн тихо сидел в кустах, выжидая лучшего момента. Минуты тянулись, словно часы, но вскоре клад был найден. \n«Вы такие же доверчивые, как ваш капитан! Пли!»\nРаздалось еще несколько выстрелов. Похоже, коварный Банубас обманул матросов! \n«Так. С этими покончено… Возвращайтесь к кораблю, матросы!»\n«А как же клад?» - спросил Банубаса один из его подопечных\n«Клад… Ты только о кладе думаешь? Я же говорил, что сейчас буйные воды! Нужно следить за кораблём, а то он уплывет. А за кладом вернемся позже, он никуда не денется. Бегом, не то клада не достанется никому!»\n«Вот же жук… Он думает забрать весь клад себе… Но его заберу себе я!» подумал Дэн. В его голове появился план. С нехотью подопечные головорезы Банубаса начали уходить. Банубас остался наедине с кладом, как он думал, и вновь противно засмеялся. Но тут Дэн схватил пистолет упавшего рядом с ним товарища, взвёл замок и наставил дуло на голову Банубаса. Его лицо перекосил ужас. \n«А мог бы не быть жадным… Но получишь… ровно одну пулю в голову.»\nБа-бах. Банубас упал, подняв вокруг себя облако пыли. Из его рук выпал гигантских размеров и поразительной чистоты рубин. Подойдя ближе к яме, где был заложен клад, Дэн увидел целый сундук, полный пиастров и рубинов. Его охватила непреодолимая амбиция заполучить богатства себе: вот тот шанс, который он ждал!\nВозвращался к шхуне Дэн, как и шел в джунгли: с мешком. И он был также тяжел, но та тяжесть чувствовалась так легко, словно он был полон пуха, эйфории от богатств, доставшихся ему одному.\nПока оставшиеся в живых из экипажа бузили и распивали алкоголь в баре, дэн тщательно спрятал свой клад в своей подсопке. На следующий день он разочаровал свой экипаж, показав им лишь пиастры из клада, коих было не так много. Но когда они в следующий раз остались в одном из портов, Дэн исчез, вместе с кладом.\n«Я делал всё тихо. Так поступил бы каждый» думал Дэниэл о тех днях, будучи видным Лондонским графом. Один кроваво-красный рубин лежал на его столе в напоминание о его удаче. Так пират, распорядившись своей фортуной, выбрал купить путь в высшее общество, став образованным купцом и мореходом, и, сидя в своем поместье, увековечивал себя в истории, расписывая повесть о своих пиратских днях, которую он назовет…\n«Тихий Дэн».\nКонец! Спасибо за игру!"]}
text = {}    #финальный текст для записи в файл
answers = []    #список ответов игрока


print(story_paths["title"], story_paths["intro"], story_paths["intermission_1"], story_paths["path_1"], sep = "")    #начало
if check_answer(ask_answer("".join([YES, NO]))):    #первый выбор
    print(story_paths["answer_1"][0])
    answers.append(story_paths["answer_1"][0])
    restart(ask_answer("".join([YES, NO])))    #рестарт по желанию
else:
    print(story_paths["answer_1"][1], story_paths["path_2"])
    answers.append(story_paths["answer_1"][1])
    if check_answer(ask_answer("".join([YES, NO]))):    #второй выбор
        print(story_paths["answer_2"][0])
        answers.append(story_paths["answer_2"][0])
    else:
        print(story_paths["answer_2"][1])
        answers.append(story_paths["answer_2"][1])

for item in story_paths.items():    #добавление сюжета в переменную для записи в файл
    if type(item[1]) is not type([]): 
    text[item[0]] = item[1]
    else:
        if answers[0].endswith("Начать заново?"):
            answers[0] = answers[0].replace("Начать заново?", "")
            text[item[0]] = answers.pop(0)    #работа с пользовательскими ответами
        else:
            text[item[0]] = answers.pop(0)
        if len(answers) == 0:
            break

with open("story.txt", "w", encoding = "UTF-8") as final_story:    #запись в файл
    for line in text.items():
        print("".join(line[1]), file = final_story)
with open("story.txt", "w", encoding = "UTF-8") as final_story:    #запись в файл
    for line in text.items():
        print("".join(line[1]), file = final_story)
