# Космический Инстаграм
Автоматизирует сбор фотографий космоса и публикует их инстаграм аккаунте.

### Как установить
- Зарегистрируйтесь на [instagram](https://www.instagram.com).
- Запомните свой логин и пароль.
- Создайте файл `.env` с переменными:
```python
INSTAGRAM_LOGIN=<Ваш логин>
INSTAGRAM_PASSWORD=<Ваш пароль>
```

- Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Примеры использования
Что-бы скачать картинки из [spacex](https://www.spacex.com), выложить картинки в инстаграм :
```
python fetch_spacex.py -p images/dsa/or.png/
python main.py -p images/dsa/or.png/
```
Что-бы скачать картинки из [hubble](https://hubblesite.org), выложить картинки в инстаграм :
```
python fetch_hubble.py -p 1\2\3\
python main.py -p 1\2\3\
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).