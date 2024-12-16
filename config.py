from aiogram import html

home_button = [
    [
        ('↩️ На главную', 'home'),
    ],
]

class welcome:
    text = html.bold('Добро пожаловать в HomeWork, бот для отслеживания выполнения домашних заданий, поддерживающий функцию создания классов или групп')
    buttons = [
        [
            ('➕ Создать класс', 'wc_create_class'),
            ('👥 Вступить в класс', 'wc_join_class')
        ],
    ]

class wc_create_class1:
    text = 'Дайте имя классу'

class wc_create_class2:
    text = 'Отлично, ваш класс успешно создан! Пожалуйста, назовите первую группу в классе'

class wc_create_class3:
    text = 'Отлично, группа создана, а вы - уже в классе! Приглашайте своих одноклассников при помощи кнопки "Добавить"'
    buttons = home_button

class wc_join_class:
    text = 'Чтобы вступить в класс, скиньте ваш айди любому участнику класса, а он добавит вас через кнопку "Добавить".\n\nВаш айди: '\
            + html.code('{user_id}')
    buttons = home_button

class home:
    text = html.bold('Привет, {user_name}!\n') + 'Выполнено {hw_completed}/{hw_all} домашних заданий.'
    buttons = [
        [
            ('📆 ДЗ на завтра', 'tommorrow'),
        ],
        [
            ('➕ Добавить', 'cl_add_member'),
        ]
    ]

class cl_add_member1:
    text = 'Напишите айди человека, которого вы хотите добавить в класс'

class cl_add_member2:
    text = 'Напишите (точное, вплоть до регистра!) название группы, в которую вы хотите добавить нового участника'

class cl_add_member3:
    text = 'Участник успешно добавлен в класс {current_class}'
    buttons = home_button

class tommorrow:
    text = 'Домашнее задание на завтра'
    buttons = home_button
    