# Solitaire-by-penguin-rules
Це консольна реалізація пасьянсу за правилами пінгвін на python

<h2>Загальна постановка задачі</h2>
Написати платформенно незалежну програму з консольним інтерфейсом, що
забезпечує одному гравцю можливість розкладання зазначеного пасьянсу.

<h2>Правила Пінгвін</h2>
<i>Кількість колод: 1<br/>
Кількість карт у колоді: 52<br/>
Мета пасьянсу: необхідно зібрати всі карти на базових стопках у висхідних послідовностях у масть.</i><br/>
<i>Правила пасьянсу.</i> Колода ретельно тасується й 49 карт викладаються в 7 ігрових вертикальних
стопок по 7 карт у кожній стопці. Зверху викладених карт розташовуються місця для семи резервних
стопок. Із правої сторони розташовуються місця для чотирьох базових стопок, де стартовими картами є
карти того ж значення, що й перша поміщена карта в будь-яку базову стопку. 3 карти, що залишилися
кладуть у запасну стопку. Необхідно зібрати всі карти на базових стопках у висхідних послідовностях у
масть. Дозволяється переміщати верхні карти ігрових стопок з однієї ігрової стопки на іншу ігрову стопку
в спадних послідовностях у масть. Дозволяється переміщати будь-які карти з ігрових стопок у резервні
стопки, а з резервних можна переміщати й на базові стопки. У кожній резервній стопці повинне бути не
більше однієї карти. Якщо яка-небудь із ігрових стопок звільняється від карт, то на порожнє місце можна
покласти будь-яку карту із запасної колоди.<br/>
Пасьянс зійшовся, якщо всі карти зібрані на базових стопках у висхідних послідовностях у масть.

<h2>Уточнення загальної постановки задачі</h2>
Напишіть програму, яка дозволяє гравцю розкладати зазначений у варіанті пасьянс.<br/>
На початку роботи програма виводить інформацію про виконавця та правила пасьянсу.<br/>
Далі, поки або пасьянс не зійдеться, або поки користувач не припинить розкладання
пасьянсу, програма виводить поточний стан гри (пасьянсу) та запитує в користувача його
черговий хід.<br/>
Якщо пасьянс зійшовся, то про це наприкінці має бути явне повідомлення. Якщо
користувач припинив розкладання пасьянсу, то програма має чемно сказати йому "до
побачення".
<h2>Вимоги</h2>
Якщо не зазначено інше, під наявністю функції/методу/класу/... мається на увазі
наявність належно реалізованої функції/..., що відповідає умові лабораторної та вимогам до
неї.
<h3>Відображення поточного стану гри</h3>
Поточний стан гри має відображатися в текстовому вигляді. Не варто виконувати
очищення екрану перед виведенням стану! Ця операція під різними ОС потребує різних
команд, а тоді програма не буде платформенно незалежною.<br/>
Що саме та як виводити суттєво залежить від умов варіанту. Зображення має бути таким,
щоб з нього можна було побачити поточний стан грального стола та прийняти рішення щодо
чергового ходу.
Оскільки виведення текстове і виводиться не тільки стан, а ще відбувається спілкування
з користувачем, то на початку та в кінці стану слід виводити рядок-роздільник, щоб стан
візуально відокремлювався від іншої інформації. В якості рядка-роздільника пропоновано
<b>використовувати, наприклад, рядок такого вигляду (деяка кількість знаків рівності поспіль)</b><br/>
=========<br/>
або рядок такого вигляду:<br/>
*********<br/>
Або якийсь інший рядок, що досягає мети візуального розділення інформації.<br/>

<h3>Структура програми та контроль помилок</h3>
Програма розташовується в кількох файлах. Точкою входу є файл <b>main.py</b>. Використання
сторонніх бібліотек та власних глобальних змінних заборонено. У програмі відсутні
синтаксичні помилки та вона може бути виконана інтерпретатором Python версії 3.11.<br/>
Має бути наявна <b>система класів</b>, що моделюють сутності, що виникають у грі. Серед
класів має бути клас верхнього рівня — клас <b>Game</b>, об'єкт якого зберігає стан гри (де які карти)
та його методи забезпечують виконання дій гравцем.<br/>
Схема виконання ходу має бути такою:<br/>
програма запитує в користувача його хід, виконує відповідні дії викликом відкритого
методу класу <b>Game</b>, за відмови у виконанні виводить повідомлення про це.<br/>
Перевірка коректності ходів гравця цілком на сумлінні класу <b>Game</b>, при цьому його
методи жодних винятків не генерують.<br/>
Жоден метод жодного класу не повинен спілкуватись з користувачем! Усі засоби
реалізації спілкування (запит на дію, повідомлення про неможливість її виконання, про
некоректний вибір тощо) мають знаходитись за межами класів, що моделюють логіку гри чи
ігрові сутності. При цьому методи класів можуть (чи, навіть, мають, якщо доречно) повертати
ознаку успішності свого виконання.<br/>
Аварійне завершення програми є неприпустимим.
<h3>Невелика порада щодо розташування та іменування файлів</h3>
Під час імпорту власних бібліотек та пакетів треба вказувати ім'я файлу чи папки, де
розташовується відповідний код. Прийнято записувати назви малими літерами (це дає
можливість відрізняти бібліотеку від однойменного з точністю до регістру символів класу, що
в ній записаний). Якщо назви дискових файлів чи папок будуть не в тому в регістрі, що
записаний в інструкції імпортування, то така програма зможе працювати тільки під Windows
(бо в ній шляхи є регістро-незалежними). Тоді вона не буде платформенно незалежною і не
отримає позитивних балів, тому що банально не зможе працювати під тією ОС, де буде
перевірятись.<br/>
Слідкуйте за регістром символів у назвах файлів та пакетів вашої програми!
<h3>Інше</h3>
M1. Усі надіслані версії лабораторної не порушують принципи академічної
доброчесності.<br/>
M2. Усі ідентифікатори записані символами US-ASCII.<br/>
M3. Код не повинен містити дублювання та невикористовувані фрагменти (навіть
закоментовані).<br/>
M4. Коментарі не повинні бути надлишковими.<br/>
M5. Коментарі та документація відповідає тому, що пояснює.<br/>
M6. Код має відповідати рекомендаціям підрозділів 7.1.6 та 7.4 (див. файл 7 Керування
порядком обчислень.pdf).<br/>
M7. Використовувані в програмі імена є змістовними, їх призначення зрозуміле з їх назви.
Довгих імен слід уникати.<br/>
M8. Назви суто допоміжних функцій мають починатися з підкреслення. Усі функції
належно задокументовані.<br/>
M9. Під час проєктування слід дотримуватись принципів функціонального проєктування,
уникати довгих функцій.<br/>
M10. Код не має бути заплутаним. Код не має бути захаращений перевірками.
Використання механізму винятків має бути доречним та адекватним.<br/>
M11. Змінні, що використовуються в тілі функції виключно як локальні змінні функції для
збереження проміжних результатів, не повинні бути її параметрами.<br/>
M12. Кожен фізичний рядок файлу з текстом програми цілком вміщується в одну ширину
екрана ноутбука. (Текст програми можна прочитати в текстовому редакторі без
горизонтальної прокрутки.)<br/>
M13. Форматування рядків виконується виключно за допомогою f-рядків.<br/>
M14. Інструкції global, nonlocal заборонені до використання.<br/>
M15. Використання у власному коді exit або інших засобів дострокового завершення
програми заборонено.<br/>
M16. Завершення функції за інструкцією return з середини циклу заборонено.<br/>
M17. Усі функції означені на рівні модуля або як методи класу.<br/>
M18. Інструкції try не повинні бути вкладеними (за текстом) в інші інструкції try.<br/>
M19. При проєктуванні класів слід дотримуватись принципів ООП.<br/>
<h3>Принципи академічної доброчесності (дуже важливо!)</h3>

Студент вільно орієнтується в коді лабораторної роботи, яку він здає, розуміє усі вико-
ристані синтаксичні елементи мови та бібліотечні засоби, зміст та призначення частин коду,
вміє самостійно запустити програму на виконання, здатен самостійно внести локальні виправ-
лення в код. У коді відсутні коментарі, що перекладають зміст інструкцій на природні мови.<br/>
Порушення M13 прирівнюється до порушення академічної доброчесності, причому таким, що
спростоване бути не може.<br/>
<b>Принципи академічної доброчесності передбачають, що ані брати чужий код, ані
давати комусь свій не можна. Сумісна розробка також заборонена.</b><br/>
Якщо листи з кодом та відеопрезентацією відправлено не з власної поштової адреси, або
якщо з однієї адреси відправлено роботи різних студентів, або якщо студент виконав не свій
варіант, або неправильно зазначив виконавця, або виконавцем зазначений хтось інший, то все
це, навіть у проміжних версіях, також вважається порушенням академічної доброчесності,
причому таким, що спростованим бути не може.

<h2>Перевірка програмних проєктів</h2>
Отримана сукупність програм ПРОГРАМНО перевірятиметься на дотримання принципів
академічної доброчесності (запозичення коду). Чим більше буде збіг, тим більш ретельною
буде співбесіда. Якщо збіг буде зашкалювати, то всі такі лабораторні будуть оцінені в 0 балів,
незалежно від того, хто був клієнтом, а хто сервером.<br/>
Програмний проєкт передбачає захист у формі відеопрезентації і, можливо, співбесіди.<br/>
Відеопрезентація є невід’ємною частиною захисту програмного проєкту. За її відсутності
позитивна кількість балів виставлена бути не може.<br/>
Остаточне рішення проводити чи ні співбесіду залишається на розсуд викладача.<br/>
Захист лабораторної роботи вважається неуспішним, якщо під час захисту виявляється,
що студент не до кінця розуміє код або погано в ньому орієнтується чи не розуміє використані
синтаксичні елементи мови, зміст та призначення частин коду, а також якщо захист не
відбувся з ініціативи студента.<br/>
У випадку проведення захисту лабораторна робота може бути позитивно оцінена тільки у
випадку, коли студент/студентка дав/дала правильні відповіді на всі запитання щодо
структури зданого коду, змісту та призначення його елементів, використаних алгоритмів, а
також вільно орієнтується у зданому коді та здатен/здатна правильно внести невеликі
модифікації.<br/>
Оцінка за програмні проєкти, що були здані на перевірку невчасно, але не пізніше ніж за
повний робочий тиждень до кінця теоретичного навчання в семестрі, знижується на 20%.
Програмні проєкти, що надійшли на перевірку пізніше ніж за повний робочий тиждень до
кінця теоретичного навчання в семестрі, перевіряються на офіційному перескладанні
дисципліни (якщо воно буде призначене студенту), при цьому оцінка не може складати більше
60% від максимально можливої.<br/>
Згідно правил Університету, оцінки, що менше 9 балів, до загальної суми семестрових
балів не додаються.<br/>
Якщо:<br/>
тестер не отримав або відхилив лабораторну,<br/>
або відсутня частина файлів проєкту чи вони не імпортуються,<br/>
або відсутня відеопрезентація,<br/>
або хоча б одна версія порушує принципи академічної доброчесності,<br/>
або лабораторна має критичну кількість запозичень,<br/>
або захист був неуспішним,<br/>
або порушено вимоги підрозділу Структура програми та контроль помилок*<br/>
то лабораторна отримує 0 балів.<br/>
* Якщо єдиною проблемою з вимогами зазначеного підрозділу є відсутність консольного
інтерфейсу (тобто реалізовано тільки логіку гри у вигляді відповідної системи класів), то
лабораторна має шанси на 9-12 балів залежно від якості коду.<br/>
Все працює, все згідно вимог, все гарно і ззовні, і з середини, то це 15 балів.<br/>
Все працює, все гарно, але тільки ззовні, то це 11-13 балів залежно від ступеня проблем.<br/>
Якщо наявний тільки консольний інтерфейс або є проблеми з реалізацією логіки пасьянсу,
то позитивних балів очікувати не варто.<br/>
Перевірка розпочнеться після 10 травня. Попередня перевірка не планується.<br/>
Перескладання програмних проєктів, за які вже були виставлені остаточні бали, з метою
збільшення кількості балів не передбачаються.<br/>

<h2>Порядок роботи над програмою</h2>
... з висоти пташиного польоту виглядає так.<br/>
<u>Частина, що не стосується інтерфейсу</u><br/>
1. Розібратися з умовою.<br/>
2. Побудувати клас, що реалізує логіку пасьянсу та стан гри.<br/>
Треба визначити:<br/>
– що є поточним станом гри (розподіл карт по купках, тощо) та в яких структурах даних
буде зберігатися;<br/>
– методи, які виконують окремі ігрові дії (як користувача, так і комп’ютера)
Взяти до уваги, що<br/>
– гравець може перекладати карти тільки згідно правил<br/>
– комп’ютер задає початковий стан, визначає чи завершено розкладання і чи пасьянс
зійшовся.<br/>
Жодного спілкування з користувачем клас робити не повинен.<br/>
<u>Частина, що стосується інтерфейсу</u><br/>
1. Поміркувати над зображенням стану гри.<br/>
2. Реалізувати виведення стану гри.<br/>
3. Продумати спілкування з користувачем (як реалізувати запити ходів користувача) та
реалізувати його.<br/>
4. Зібрати все до купи.<br/>
