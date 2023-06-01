""" Написать тест с использованием pytest и requests в котором:
1. адрес сайта, имя пользователя и пароль хранятся с config.yaml
2. conftest.py содержит фикстуру авторизации по адресу(///gateway/login) с
передачей параметоров username и password и возвращает токен авторизации
3. тест с использованием DDT проверяет наличие поста с определенным
 заголовком в списке постов другого пользователя, для этого выполняется
 get запрос по адресу(///api/posts) с хедером, содержащим токен
 авторизации в параметре 'X-Auth-Token'. Для отображения постов
 другого пользователя передается 'owner':'notMe' """

import requests
import logging

def get_my_posts(token):
    logging.debug('Open posts page')
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})#, 'page': 17, params={'owner': 'notMe'
    if g:
        listcont = [i['content'] for i in g.json()['data']] 
        return listcont
    else:
        logging.error('Страница с постами не открылась')
    

def get_notmy_posts(token):
    logging.debug('Open posts page')
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token}, params={'owner': 'notMe'})#, 'page': 17, params={'owner': 'notMe'
    if g:
        listcont = [i['content'] for i in g.json()['data']] 
        return listcont
    else:
        logging.error('Страница с постами не открылась')

def createpost(token):
    logging.debug('Create new post')
    p = requests.post('https://test-stand.gb.ru/gateway/posts', headers={'X-Auth-Token': token}, data={ 'title':'Новый пост для тестирования',
            'description':'informaition about post', 'content': 'Добавить в задание с REST API еще один тест, в котором создается новый пост,а потом проверяется его наличие на сервере по полю “описание”.'} )
    if p:
        return p.json()
    else:
        logging.error('Пост не создан')


def findpost(token):
    logging.debug('Find created post')
    d = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    if d:
        listdescript = [i['description'] for i in d.json()['data']]
        return listdescript
    else:
        logging.error('Пост не найден')

def test_2(login, not_my_post):
    assert not_my_post in get_notmy_posts(login)

def test_3(login, my_post):
    assert my_post in get_my_posts(login)



# """ДЗ 1. Добавить в задание с REST API еще один тест, в котором создается новый пост,
#  а потом проверяется его наличие на сервере по полю “описание”. Подсказка: Создание поста
#  выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров title,
#  description, content."""