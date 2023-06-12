from aiogram import types, Dispatcher
from aiogram.types import InputFile, update
from create_bot import dp, bot
from keyboards import passengers_menu, passengers_menu_tarifs, passengers_menu_supervisors \
    , Exit, tarifs_zoneA, tarifs_zoneB, tarifs_Card_replenishment, tarifs_organizations, Passenger_Agency, \
    Passenger_insurance \
    , Anti_terrorist_security, Prevention_coronavirus, Warehouse_forgotten_things, soc_card
from aiogram.types import ReplyKeyboardRemove
from random import randint
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dataclasses import dataclass
import openpyxl

wb1 = openpyxl.load_workbook(r'Пассажирам.xlsx', read_only=True)
sheet1 = wb1.active
rt = 0


def exel(b, d):
    a = ['A', 'B', 'C']
    for i in range(1, 100):
        p = str(i)
        nameL = sheet1[a[0] + p].value
        if b in nameL:
            nameR = sheet1[a[d] + p].value
            return (nameR)


def message(where, photo_n, exel_n, to_who, photo_n2):
    @dp.callback_query_handler(text=where)
    async def process_callback_button1(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        global rt

        back_n_more_det = InlineKeyboardMarkup() \
            .insert(InlineKeyboardButton('более подробно', callback_data='Более подробно' + str(rt))) \
            .insert(InlineKeyboardButton('выйти в главное меню', callback_data='Выйти главное меню'))
        if photo_n is not None:
            photo_bytes = InputFile(path_or_bytesio=('photo/' + photo_n))
            await bot.send_photo(callback_query.from_user.id, photo=photo_bytes)

        if photo_n2 is not None:
            photo_bytes = InputFile(path_or_bytesio=('photo/' + photo_n2))
            await bot.send_photo(callback_query.from_user.id, photo=photo_bytes)

        if exel(exel_n, 1) == 'картинка' or None:
            await bot.send_message(callback_query.from_user.id, 'Заголовок', reply_markup=back_n_more_det)
        else:
            await bot.send_message(callback_query.from_user.id, exel(exel_n, 1), reply_markup=back_n_more_det)

        @dp.callback_query_handler(text='Более подробно' + str(rt))
        async def process_callback_button1(callback_query: types.CallbackQuery):
            global rt

            if exel(exel_n, 1) == 'картинка' or None:
                pass
            else:
                await bot.send_message(callback_query.from_user.id, exel(exel_n, 2), reply_markup=back)

        rt += 1
        await callback_query.message.delete()
        if to_who is not None:
            await bot.send_message(callback_query.from_user.id, exel_n, reply_markup=to_who)


# Выйти в главное меню
@dp.callback_query_handler(text='Выйти главное меню')
async def process_callback_butto1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Главное меню', reply_markup=passengers_menu)


back_n_more_det = InlineKeyboardMarkup() \
    .insert(InlineKeyboardButton('более подробно', callback_data='Более подробно')) \
    .insert(InlineKeyboardButton('выйти в главное меню', callback_data='Выйти главное меню'))

back = InlineKeyboardMarkup() \
    .insert(InlineKeyboardButton('выйти в главное меню', callback_data='Выйти главное меню'))


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, text='**Здравствуйте**', reply_markup=passengers_menu)


# ------------------------------------------------------------------------------------


# Пассажирам
@dp.callback_query_handler(text='пасажирам')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Пассажирам', reply_markup=passengers_menu)
    await callback_query.message.delete()


# Тарифы и билеты
@dp.callback_query_handler(text='Тарифы и билеты')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Тарифы и билеты', reply_markup=passengers_menu_tarifs)
    await callback_query.message.delete()

    # Тарифа и билеты_Зона А


message('Тарифная зона А', 'Тарифы и билеты/тарифная зона а_по этим билетам можно проехать....png', 'Тарифная зона А',
        tarifs_zoneA, None)

# Билет «Кошелек» на карте «Тройка»
message('Билет Кошелек', 'Тарифы и билеты/Билет «Кошелёк» на карте «Тройка»_до текста.png',
        'Билет «Кошелек» на карте «Тройка»', None, None)

# Билет «Единый» на количество поездок
message('Билет Единый', 'Тарифы и билеты/Билет «Единый» на количество поездок_до текста.png',
        'Билет «Единый» на количество поездок', None, None)

# Билеты без лимита поездок
message('Билеты без лимита поездок A', 'Тарифы и билеты/Билеты без лимита поездок_до текста.png',
        'Билеты без лимита поездок', None, None)

# Бесконтактная банковская карта или смартфон
message('Бесконтакт A', 'Тарифы и билеты/Бесконтактная банковская карта или смартфон_до текста.png',
        'Бесконтактная банковская карта или смартфон', None, None)

# Оплата по биометрии - Facepay
message('Facepay', 'Тарифы и билеты/Оплата по биометрии - Facepay.png', 'Оплата по биометрии - Facepay', None, None)

# Социальная карта учащегося или студента
message('Социальные карты учащегося А', 'Тарифы и билеты/Социальная карта учащегося или студента.png',
        'Социальная карта учащегося или студента', None, None)

# Социальная карта москвича
message('Социальные карты москвича А', 'Тарифы и билеты/Социальная карта москвича.png', 'Социальная карта москвича',
        None, None)

# Тарифа и билеты_Зона B

message('Тарифная зона Б', None, 'Тарифная зона Б', tarifs_zoneB, None)

# Билеты на количество поездок
message('Билеты на количество поездок', 'Тарифы и билеты/Билеты на количество поездок.png',
        'Билеты на количество поездок B', None, None)

# Билеты без лимита поездок
message('Билеты без лимита поездок B', 'Тарифы и билеты/Билеты без лимита поездок_до текста.png',
        'Билеты без лимита поездок B', None, 'Билеты без лимита поездок.png')

# Бесконтактная банковская карта или смартфон
message('Бесконтакт B', 'Тарифы и билеты/Бесконтактная банковская карта или смартфон.png',
        'Бесконтактная банковская карта или смартфон B', None, None)

# Социальная карта учащегося или студента
message('Социальные карты учащегося B', 'Тарифы и билеты/Социальная карта учащегося или студента.png',
        'Социальная карта учащегося или студента B', None, None)

# Социальная карта москвича
message('Социальные карты москвича B', 'Тарифы и билеты/Социальная карта москвича(зона Б).png',
        'Социальная карта москвича B', None, None)


# Пополнение карты «Тройка»
@dp.callback_query_handler(text='Пополнение карты «Тройка»')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Пополнение карты «Тройка»',
                           reply_markup=tarifs_Card_replenishment)
    await callback_query.message.delete()


# Билет «Кошелек» на карте «Тройка»
message('Билет «Кошелек» на карте «Тройка»', 'Тарифы и билеты/Билет «Кошелёк» на карте «Тройка»_до текста.png',
        'Билет «Кошелек» на карте «Тройка».', None, None)

# Пополнение карты «Тройка» через мобильные приложения.
message('Пополнение мп', None, 'Пополнение карты «Тройка» через мобильные приложения.', None, None)

# Пополнение карты «Тройка» в кассах и автоматах
message('Пополнение в кассах', None, 'Пополнение карты «Тройка» в кассах и автоматах', None, None)

# Удаленное пополнение карты «Тройка» (онлайн)
message('Пополнение карты онлайн', None, 'Удаленное пополнение карты «Тройка» (онлайн)', None, None)

# Удаленное пополнение карты «Тройка» с помощью SMS
message('Пополнение карты SMS', None, 'Удаленное пополнение карты «Тройка» с помощью SMS', None, None)

# Прямое пополнение
message('Прямое пополнение', None, 'Прямое пополнение', None, None)

# Проездные билеты
message('Проездные билеты', None, 'Проездные билеты', None, None)

# Оплата проезда бесконтактной банковской картой или смартфоном
message('Оплата проезда',
        'Тарифы и билеты/Оплата проезда бесконтактной банковской картой или смартфоном/Оплата проезда бесконтактной банковской картой или смартфоном_после текста.jpg', \
        'Оплата проезда бесконтактной банковской картой или смартфоном', None,
        'Тарифы и билеты/Оплата проезда бесконтактной банковской картой или смартфоном/Социальные карты учащегося, студента, ординатора и аспиранта.png')


# социальные карты учащегося, студента,
@dp.callback_query_handler(text='социальные ка')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Социальные карты учащегося, студента, ординатора и аспиранта..', reply_markup=soc_card)
    await callback_query.message.delete()


# Пополнение социальных карт учащихся на наземный транспорт
message('Пополнение соц карт', None, 'Пополнение социальных карт учащихся на наземный транспорт', None, None)

# Социальные карты москвича
message('Социальные карты москвича', 'Тарифы и билеты/Социальные карты москвича/Социальные карты москвича.jpg',
        'Социальные карты москвича.', None, None)

# При неисправности карты «Тройка»
message('При неисправности карты «Тройка»',
        'Тарифы и билеты/Социальные карты москвича/При неисправности карты «Тройка».png', 'При неисправности карты «Тройка»', None, None)

# Оплата проезда при неисправности
message('Оплата проезда при неисправности', None, 'Оплата проезда при неисправности', None, None)


# Предприятиям и организациям
@dp.callback_query_handler(text='Предприятиям и организациям')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Предприятиям и организациям',
                           reply_markup=tarifs_organizations)
    await callback_query.message.delete()


# Мобильные приложения
message('Мобильные приложения', None, 'Мобильные приложения', None, None)

# Агентская сеть
message('Агентская сеть', None, 'Агентская сеть', None, None)

# Пункты продажи билетов и пополнения баланса транспортных карт
message('Пункты продажи билетов и пб', None, 'Пункты продажи билетов и пополнения баланса транспортных карт',
        None, None)


# Контролеры
@dp.callback_query_handler(text='Контролеры')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Контролеры', reply_markup=passengers_menu_supervisors)
    await callback_query.message.delete()

# Действия контролёра ГУП «Мосгортранс» при проверке
message('Действия контролёра', None, 'Действия контролёра ГУП «Мосгортранс» при проверке', None, None)

# Контролёр ГУП «Мосгортранс» имеет право
message('Контролёр ГУП право', None, 'Контролёр ГУП «Мосгортранс» имеет право', None, None)

# Контролёру ГУП «Мосгортранс» категорически запрещено
message('Контролёру ГУП запрещено', None, 'Контролёру ГУП «Мосгортранс» категорически запрещено', None, None)

# Удостоверение контролера
message('Удостоверение контролёра', None, 'Удостоверение контролера', None, None)

# Правила пользования наземным городским транспортом
message('Правила', None, 'Правила пользования наземным городским транспортом', None, None)

# Пассажирское агентство ГУП «Мосгортранс»
@dp.callback_query_handler(text='Пассажирское')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Пассажирское агентство ГУП «Мосгортранс»', reply_markup=Passenger_Agency)
    await callback_query.message.delete()

# Контакты
message('Контакты', None, 'Контакты', None, None)

# Схема проезда
message('Схема проезда', None, 'Схема проезда', None, None)

# Деятельность
message('Деятельность', None, 'Деятельность', None, None)

# Перечень документов для получения изъятых социальных карт
message('Документы для получения карт', None, 'Перечень документов для получения изъятых социальных карт', None, None)


# Страхование пассажиров
@dp.callback_query_handler(text='Страхование пассажиров')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Страхование пассажиров', reply_markup=Passenger_insurance)
    await callback_query.message.delete()

#
message('Об обязательном', None, 'Об обязательном страховании гражданской ответственности перевозчика за причинение вреда жизни, здоровью, имуществу пассажиров и о порядке возмещения вреда, причиненного при перевозках пассажиров', None, None)

# Контакты страховой компании
message('Контакты страховой компании', None, 'Контакты страховой компании', None, None)

# Страхование пассажиров
@dp.callback_query_handler(text='Обеспечение')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Обеспечение антитеррористической безопасности', reply_markup=Anti_terrorist_security)
    await callback_query.message.delete()

# Комплект оснащения пассажирского транспортного средства ГУП «Мосгортранс»
message('Комплект оснащения', None, 'Комплект оснащения пассажирского транспортного средства ГУП «Мосгортранс»', None, None)

# Схема обмена данными
message('Схема обмена данными', None, 'Схема обмена данными', None, None)


# Профилактика коронавируса в наземном транспорте
@dp.callback_query_handler(text='Профилактика')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Профилактика коронавируса в наземном транспорте', reply_markup=Prevention_coronavirus)
    await callback_query.message.delete()

# Как защищают наземный транспорт?
message('Как защищают наземный транспорт?', None, 'Как защищают наземный транспорт?', None, None)

# Как часто дезинфицируют наземный транспорт?
message('Как часто дезинфицируют', None, 'Как часто дезинфицируют наземный транспорт?', None, None)

# Как и чем обрабатывают салон?
message('Как и чем обрабатывают салон?', None, 'Как и чем обрабатывают салон?', None, None)

# Как защищают водителей?
message('Как защищают водителей?', None, 'Как защищают водителей?', None, None)

# Горячая линия Роспотребнадзора:
message('Горячая линия Роспотребнадзора', None, 'Горячая линия Роспотребнадзора:', None, None)



# Склад забытых вещей
@dp.callback_query_handler(text='Склад забытых вещей')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Склад забытых вещей', reply_markup=Warehouse_forgotten_things)
    await callback_query.message.delete()

# Телефоны
message('Телефоны', None, 'Телефоны', None, None)

# Время работы
message('Время работы', None, 'Время работы', None, None)



# Обратная связь
message('Обратная связь', None, 'Обратная связь', None, None)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, state='*', commands=['start', 'help'])
