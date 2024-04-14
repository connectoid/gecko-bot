BUTTON = {'ru':{'MAIN_MENU_BUTTON':'🏠 Главное меню',
                'HELP_BUTTON': '🆘 Помощь',
                'TO_MAIN_MENU_BUTTON': '⬅️ В главное меню',
                'REPEAT_BUTTON': '🔁 Повторить',
                'PROFILE_BUTTON': 'ℹ️ Профиль',
                'REMAINS_BUTTON': '🔢 Остаток заросов',
                'TARIFF_BUTTON': '💰 Выбрать тариф',
                'HISTORY_BUTTON': '🕑 История запросов',
                'RUS_LANG_BUTTON': 'Русский (ru)',
                'ENG_LANG_BUTTON': 'Английский (en)',
            },

            'en':{'MAIN_MENU_BUTTON':'🏠 Main menu',
                'HELP_BUTTON': '🆘 Help',
                'TO_MAIN_MENU_BUTTON': '⬅️ To main menu',
                'REPEAT_BUTTON': '🔁 Repeat',
                'PROFILE_BUTTON': 'ℹ️ Profile',
                'REMAINS_BUTTON': '🔢 Rest of requests',
                'TARIFF_BUTTON': '💰 Choose a tariff',
                'HISTORY_BUTTON': '🕑 Requests history',
                'RUS_LANG_BUTTON': 'Русский (ru)',
                'ENG_LANG_BUTTON': 'English (en)',

            }
}

MESSAGE = {'ru': {
                'FIRST_START': 'Вам доступен тестовый тариф, который включает (описание бесплатного тарифа)',
                'LEXICON_HELP': 'Текст справочной информации',

                'START_MESSAGE': 'Вы запустили бот',

                'FEEDBACK_TEXT': 'Введите ваше сообщение, оно будет отправлено администратору',

                'FEEDBACK_SENT': 'Ваше сообщение отправлено!',

                'UNRECOGNIZED_COMMAND': 'Неизвестная команда.',
                'LANG': 'Выберите ваш язык. Choose your language.',
                'LANG_CHOSEN': 'Язык выбран (Применение перевода текста командного меню займет какое-то '\
                'время, чтобы ускорить вы можете перезагрузить приложение: ',
                'EXIT_DIALOGUE': 'Вы вышли из диалога.',
                'NOT_IN_DIALOGUE': 'В данный момент вы не ведёте диалог.',
                'CHOOSE_TARIFF': 'Выберите тариф (бесплатно в тестовом режиме):',
                'NOT_IN_DIALOGUE': 'В данный момент вы не ведёте диалог.',
                'DENIED_IN_DIALOGUE': 'Эта команда недоступна в режиме диалога.',
                'LIMIT_RICHED': 'У вас не осталось оплаченных запросов, выйдите из диалога командой /cancel и '\
                'выберите любой тариф в разделе Профиль /profile (это бесплатно)',
                'CHOOSE_SECTION': 'Выберите раздел',
                'UNDER_DEVELOPMENT': '👷‍♂️ Данный раздел пока в разработке',
                'TARIFF_SELECTED': 'Выбран тариф',
                'PROMPTS_REMAINS': 'У вас осталось запросов:',
                'YOUR_TARIFF': 'Ваш тариф: ',
                'COUNT_OF_RECENT': 'Выберите количество последних запросов: ',
                'TARIFF_WORD': 'Тариф',
                'PROMPTS_WORD': 'запросов',
                'CURRENCY_WORD': 'руб',
                
            },


            'en': {
                'FIRST_START': 'You have access to the trial plan, which includes 10 free requests '\
                'to ChatGPT and DALL-E2. After exhausting the trial requests, you need to choose '\
                'and pay for a plan in the "ℹ️ Profile" section or by using the command /profile.',
                'LEXICON_HELP': 'This bot can answer any question and generate any image based '\
                'on text description. The <b>ChatGPT</b> artificial intelligence neural network '\
                'is responsible for text dialogue. This AI works in dialogue mode and supports '\
                'natural language requests, including in Russian. It is capable of not only '\
                'answering easy questions in the style of Alice, but also summarizing hours-long '\
                'films in just a few seconds, creating program code on request, compiling financial '\
                'tables, writing scripts, poems, and providing detailed guides on any topics of '\
                'interest to you. Try asking him a question, such as "Write me an essay on the topic '\
                'of Arctic marine life" or "Create a regular expression for all phone numbers in '\
                'Russia".\n\n'\
                'The second AI presented in this bot is <b>DALL-E2</b>. This is a new neural network '\
                'algorithm that creates an image from a short phrase or sentence provided by you. '\
                'This AI, like ChatGPT, understands Russian, but better results can be achieved by '\
                'creating prompts in English. Try, for example, such prompts: <i>"An oil painting '\
                'of a mechanical clockwork flying machine from the renaissance, Gorgeous digital '\
                'painting, amazing art, artstation 3, realistic"</i> or <i>"a photo of cat flying '\
                'out to space as an astronaut, digital art"</i>, but you can also experiment with '\
                'Russian ones 🙂 \n\nBot is running in demo mode. You can choose any tariff for free '\
                'in the /profile section.',
                
                'START_MESSAGE': 'You have launched the ChatGPT/DALL-E2 bot. Choose an AI to dialogue '\
                'with in the bottom menu (ChatGPT or DALL-E2). Read more about the possibilities of this bot '\
                'in the "🆘 Help" section or by calling the /help command.',

                'FEEDBACK_TEXT': 'Enter your message, it will be sent to the administrator. '\
                'In the message, you can report an error, write a suggestion, or provide any other '\
                'information. Use the /cancel command to exit the dialog.',

                'FEEDBACK_SENT': 'Your message has been sent!',

                'UNRECOGNIZED_COMMAND': 'Unknown command or you are asking a question outside of the '\
                'AI dialog. Please select ChatGPT or DALL-E2 in the bottom menu. If these options are '\
                'not visible in the menu, please execute the command /start',
                'LANG': 'Выберите ваш язык. Choose your language',
                'LANG_CHOSEN': 'Language has been chosen (Applying the command-menu translation may '\
                'take some time, to speed it up you can restart the application): ',
                'EXIT_DIALOGUE': 'You are exit from dialogue',
                'NOT_IN_DIALOGUE': 'You are not in dealogue now. Choose in Main menu AI to dialogue',
                'CHOOSE_TARIFF': 'Choose your tariff (free in demo-mode):',
                'NOT_IN_DIALOGUE': 'Currently you are not in conversation. Select ChatGPT or DALL-E2 from '\
                'the main menu to start a conversation.',
                'DENIED_IN_DIALOGUE': 'This command is not available in AI dialog mode. '\
                'To use this command,  you need to exit the dialog by using the /cancel '\
                'command or you can continue the dialog.',
                'LIMIT_RICHED': 'You have no paid requests left, please exit the dialog by command /cancel '\
                'and select any tariff in the Profile section /profile (it is for free).',
                'CHOOSE_SECTION': 'Please select a section.',
                'UNDER_DEVELOPMENT': '👷‍♂️ This section is still under development.',
                'TARIFF_SELECTED': 'Tariff selected',
                'PROMPTS_REMAINS': 'You have requests left:',
                'YOUR_TARIFF': 'Your tariff: ',
                'COUNT_OF_RECENT': 'Select the number of recent queries: ',
                'TARIFF_WORD': 'Tariff',
                'PROMPTS_WORD': 'prompts',
                'CURRENCY_WORD': 'rub',
            },
}

COMMAND = {'ru':{
                '/start': 'Запуск бота',
                '/cancel': 'Выйти из диалого',
                '/profile': 'Перейти в профиль пользователя',
                '/feedback': 'Написать админу',
                '/lang': 'Переключить язык',
                '/help': 'Справка',
                },
            'en':{
                '/start': 'Starts bot',
                '/cancel': 'Exit the dialogue',
                '/profile': 'Go to user profile',
                '/feedback': 'Message to admin',
                '/lang': 'change language',
                '/help': 'Help',
            }

}

TARIFF = {'ru':{
                'tariff-1': 'Тариф "Лайт" (25 запросов)',
                'tariff-2': 'Тариф "Оптима" (50 запросов)', 
                'tariff-3': 'Тариф "Макс" (100 запросов)',
            },
        'en':{
                'tariff-1': 'Tariff "Light" (25 prompts)',
                'tariff-2': 'Tariff "Optima" (50 prompts)', 
                'tariff-3': 'Tariff "Max" (100 prompts)',
            }

}

BROADCAST = {'ru':{
                'whats_new': 'Бот был обновлен до новой версии. В новой версии: \n'\
                '- Добавлена возможность отправки сообщения администратору (команда /feedback). \n'\
                '- Добавлена возможность переключения языков интерфейса между Русским и Английским '\
                '(команда /lang). \n'\
                '- Бот обновлен до модели ChatGPT 3.5 Turbo. \n'\
                '- Исправлены некоторые ошибки при попытке выполнить команду находясь в состоянии диалога с ИИ.',
                'spam-1': 'Тариф "Оптима" (50 запросов)', 
                'spam-2': 'Тариф "Макс" (100 запросов)',
            },
        'en':{
                'whats_new': 'Bot was updated to new version. In new version: \n'\
                '- Added the ability to send a message to the administrator. (command /feedback). \n'\
                '- Added the ability to switch interface languages between Russian and English '\
                '(команда /lang). \n'\
                '- Bot was updated to model ChatGPT 3.5 Turbo. \n'\
                '- Fixed some errors when trying to execute a command while in a dialog state',
                'spam-1': 'Тариф "Оптима" (50 запросов)', 
                'spam-2': 'Тариф "Макс" (100 запросов)',
            }
}