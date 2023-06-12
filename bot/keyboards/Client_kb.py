from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from aiogram import types
from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton

#Основное меню
"""basic_menu=InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Пассажирам', callback_data='пасажирам'))\
    .add(InlineKeyboardButton('Маршруты и расписания', callback_data='but'))\
    .add(InlineKeyboardButton('Работа у нас', callback_data='button3'))\
    .add(InlineKeyboardButton('Услуги', callback_data='button3'))\
    .add(InlineKeyboardButton('Контакты', callback_data='button3'))\

"""

#Более подробно

more_details = InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Более подробно', callback_data='Более подроб'))\

#Выйти в главное меню
Exit=InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Выйти в главное меню', callback_data='выйти главное меню'))\

#Основное меню/Пасажирам
passengers_menu=InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Тарифы и билеты', callback_data='Тарифы и билеты'))\
    .add(InlineKeyboardButton('Контролеры', callback_data='Контролеры'))\
    .add(InlineKeyboardButton('Правила пользования наземным городским транспортом', callback_data='Правила'))\
    .add(InlineKeyboardButton('Пассажирское агентство ГУП «Мосгортранс»', callback_data='Пассажирское'))\
    .add(InlineKeyboardButton('Страхование пассажиров', callback_data='Страхование пассажиров'))\
    .add(InlineKeyboardButton('Обеспечение антитеррористической безопасности', callback_data='Обеспечение'))\
    .add(InlineKeyboardButton('Профилактика коронавируса в наземном транспорте', callback_data='Профилактика'))\
    .add(InlineKeyboardButton('Склад забытых вещей', callback_data='Склад забытых вещей'))\
    .add(InlineKeyboardButton('Обратная связь', callback_data='Обратная связь'))\

#Основное меню/Пасажирам/Тарифы и билеты

passengers_menu_tarifs=InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Тарифная зона А', callback_data='Тарифная зона А'))\
    .add(InlineKeyboardButton('Тарифная зона Б', callback_data='Тарифная зона Б'))\
    .add(InlineKeyboardButton('Пополнение карты «Тройка»', callback_data='Пополнение карты «Тройка»'))\
    .add(InlineKeyboardButton('Проездные билеты»', callback_data='Проездные билеты'))\
    .add(InlineKeyboardButton('Оплата проезда бесконтактной банковской картой или смартфоном', callback_data='Оплата проезда'))\
    .add(InlineKeyboardButton('Социальные карты учащегося, студента, ординатора и аспиранта', callback_data='социальные ка'))\
    .add(InlineKeyboardButton('Социальные карты москвича', callback_data='Социальные карты москвича'))\
    .add(InlineKeyboardButton('При неисправности карты «Тройка»', callback_data='При неисправности карты «Тройка»'))\
    .add(InlineKeyboardButton('Оплата проезда при неисправности', callback_data='Оплата проезда при неисправности'))\
    .add(InlineKeyboardButton('Предприятиям и организациям', callback_data='Предприятиям и организациям'))\
    .add(InlineKeyboardButton('Оплата проезда при неисправности', callback_data='Оплата проезда при неисправности'))\
    .add(InlineKeyboardButton('Назад', callback_data='пасажирам'))\
    .add(InlineKeyboardButton('Пункты продажи билетов и пополнения баланса транспортных карт', callback_data='Пункты продажи билетов и пб'))


#Основное меню/Пасажирам/Тарифы и билеты/Тарифная зона А

tarifs_zoneA=InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Билет «Кошелёк» на карте «Тройка»', callback_data='Билет Кошелек'))\
    .add(InlineKeyboardButton('Билет «Единый» на количество поездок', callback_data='Билет Единый'))\
    .add(InlineKeyboardButton('Билеты без лимита поездок»', callback_data='Билеты без лимита поездок A'))\
    .add(InlineKeyboardButton('Бесконтактная банковская карта или смартфон', callback_data='Бесконтакт A'))\
    .add(InlineKeyboardButton('Оплата по биометрии - Facepay', callback_data='Facepay'))\
    .add(InlineKeyboardButton('Социальная карта учащегося или студента', callback_data='Социальные карты учащегося А'))\
    .add(InlineKeyboardButton('Социальные карты москвича', callback_data='Социальные карты москвича А'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))

#Основное меню/Пасажирам/Тарифы и билеты/Тарифная зона Б

tarifs_zoneB=InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Билеты на количество поездок', callback_data='Билеты на количество поездок'))\
    .add(InlineKeyboardButton('Билеты без лимита поездок»', callback_data='Билеты без лимита поездок B'))\
    .add(InlineKeyboardButton('Бесконтактная банковская карта или смартфон', callback_data='Бесконтакт B'))\
    .add(InlineKeyboardButton('Социальная карта учащегося или студента', callback_data='Социальные карты учащегося B'))\
    .add(InlineKeyboardButton('Социальные карты москвича', callback_data='Социальные карты москвича B'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))

#Основное меню/Пасажирам/Тарифы и билеты/Пополнение карты «Тройка»

tarifs_Card_replenishment=InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Билет «Кошелек» на карте «Тройка»', callback_data='Билет «Кошелек» на карте «Тройка»'))\
    .add(InlineKeyboardButton('Пополнение карты «Тройка» через мобильные приложения', callback_data='Пополнение мп'))\
    .add(InlineKeyboardButton('Пополнение карты «Тройка» в кассах и автоматах', callback_data='Пополнение в кассах'))\
    .add(InlineKeyboardButton('Удаленное пополнение карты «Тройка» (онлайн)', callback_data='Пополнение карты онлайн'))\
    .add(InlineKeyboardButton('Удаленное пополнение карты «Тройка» с помощью SMS', callback_data='Пополнение карты SMS'))\
    .add(InlineKeyboardButton('Прямое пополнение', callback_data='Прямое пополнение'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))

#Основное меню/Пасажирам/Тарифы и билеты/Социальные карты учащегося, студента, ординатора и аспиранта

soc_card=InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Пополнение социальных карт учащихся на наземный транспорт', callback_data='Пополнение соц карт'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))


#Основное меню/Пасажирам/Тарифы и билеты/Предприятиям и организациям

tarifs_organizations=InlineKeyboardMarkup()\
    .insert(InlineKeyboardButton('Мобильные приложения', callback_data='Мобильные приложения'))\
    .add(InlineKeyboardButton('Агентская сеть', callback_data='Агентская сеть'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))

#Основное меню/Пасажирам/Контролеры

passengers_menu_supervisors=InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Действия контролёра ГУП «Мосгортранс» при проверке', callback_data='Действия контролёра'))\
    .add(InlineKeyboardButton('Контролёр ГУП «Мосгортранс» имеет право', callback_data='Контролёр ГУП право'))\
    .add(InlineKeyboardButton('Контролёру ГУП «Мосгортранс» категорически запрещено»', callback_data='Контролёру ГУП запрещено'))\
    .add(InlineKeyboardButton('Удостоверение контролёра»', callback_data='Удостоверение контролёра'))\
    .add(InlineKeyboardButton('Временное удостоверение контролёра»', callback_data='Временное удостоверение'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))

#Основное меню/Пасажирам/Пассажирское агентство ГУП «Мосгортранс»

Passenger_Agency=InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Контакты', callback_data='Контакты'))\
    .add(InlineKeyboardButton('Схема проезда', callback_data='Схема проезда'))\
    .add(InlineKeyboardButton('Деятельность', callback_data='Деятельность'))\
    .add(InlineKeyboardButton('Перечень документов для получения изъятых социальных карт', callback_data='Документы для получения карт'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))

#Основное меню/Пасажирам/Страхование пассажиров

Passenger_insurance=InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Об обязательном страховании гражданской ответственности перевозчика за причинение вреда жизни, здоровью, имуществу пассажиров и о порядке возмещения вреда, причиненного при перевозках пассажиров', callback_data='Об обязательном'))\
    .add(InlineKeyboardButton('Контакты страховой компании', callback_data='Контакты страховой компании'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))


#Основное меню/Пасажирам/Обеспечение антитеррористической безопасности
Anti_terrorist_security=InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Комплект оснащения пассажирского транспортного средства ГУП «Мосгортранс»', callback_data='Комплект оснащения'))\
    .add(InlineKeyboardButton('Схема обмена данными', callback_data='Схема обмена данными'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))

#Основное меню/Пасажирам/Профилактика коронавируса в наземном транспорте
Prevention_coronavirus=InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Как защищают наземный транспорт?', callback_data='Как защищают наземный транспорт?'))\
    .add(InlineKeyboardButton('Как часто дезинфицируют наземный транспорт?', callback_data='Как часто дезинфицируют'))\
    .add(InlineKeyboardButton('Как и чем обрабатывают салон?', callback_data='Как и чем обрабатывают салон?'))\
    .add(InlineKeyboardButton('Как защищают водителей?', callback_data='Как защищают водителей?'))\
    .add(InlineKeyboardButton('Горячая линия Роспотребнадзора', callback_data='Горячая линия Роспотребнадзора'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))

#Основное меню/Склад забытых вещей
Warehouse_forgotten_things=InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Телефоны', callback_data='Телефоны'))\
    .add(InlineKeyboardButton('Время работы', callback_data='Время работы'))\
    .add(InlineKeyboardButton('Выйти в главное меню', callback_data='Выйти главное меню'))
