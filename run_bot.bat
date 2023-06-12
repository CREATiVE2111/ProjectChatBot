@echo off

call %~dp0Bot_telegram\bot_tel\Scripts\activate

cd %~dp0Bot_telegram

set TOKEN=your token

python bot.py

pause