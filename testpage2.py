from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    
    for i in locators['xpath'].keys():
        ids[i] = (By.XPATH, locators['xpath'][i])
    
    for i in locators['css'].keys():
        ids[i] = (By.CSS_SELECTOR, locators['css'][i])

class Operations(BasePage, TestLocators):
    
    with open('C:/Users/alexa/OneDrive/Рабочий стол/FinalProject/testdata.yaml') as f:
        info = yaml.safe_load(f)

    def enter_bad_login(self):
        logging.debug('Enter login ')
        input1 = self.find_element(self.ids['x_selector1'])
        if input1:
            input1.send_keys(self.info['bad_login'])
        else:
            logging.error('Поле для ввода логина не надено')

    def enter_bad_pass(self): 
        logging.debug('Enter password ')
        input2 = self.find_element(self.ids['x_selector2'])
        if input2:
            input2.send_keys(self.info['bad_login'])
        else:
            logging.error('Поле для ввода пароля не надено')
    
    def enter_good_login(self):
        logging.debug('Enter login ')
        input1 = self.find_element(self.ids['x_selector1'])
        if input1:
            input1.send_keys(self.info['username'])
        else:
            logging.error('Поле для ввода логина не надено')

    def enter_good_pass(self): 
        logging.debug('Enter password ')
        input2 = self.find_element(self.ids['x_selector2'])
        if input2:
            input2.send_keys(self.info['password'])
        else:
            logging.error('Поле для ввода пароля не надено')

    def click_login_button(self):
        logging.debug('Click login button ')
        btn = self.find_element(self.ids['btn_selector'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')

    def get_error_text(self):
        err_label = self.find_element(self.ids['x_selector3'])
        if err_label:
            text = err_label.text
            logging.debug(f'Error {text} while loging')
            return text
        else:
            logging.error('Элемент с ошибкой не найден')
            return None
        
    def get_hello_user(self):
        hello = self.find_element(self.ids['x_selector4'])
        if hello:
            text = hello.text
            logging.info(text)
            return text
        else:
            logging.error('Пользователь не авторизовался')
            return None
    
    def click_contact_button(self):
        logging.debug('Click contact button ')
        cont_btn = self.find_element(self.ids['contact_btn'])
        if cont_btn:
            cont_btn.click()
        else:
            logging.error('Кнопка контакт не найдена')

    def enter_name(self):
        logging.debug('Enter name ')
        name_field = self.find_element(self.ids['name_field'])
        if name_field:
            name_field.send_keys(self.info['name'])
        else:
            logging.error('Поле для ввода имени не надено')
        
    def enter_email(self):
        logging.debug('Enter email ')
        email_field = self.find_element(self.ids['email_field'])
        if email_field:
            email_field.send_keys(self.info['email'])
        else:
            logging.error('Поле для ввода емейла не надено')

    def enter_content(self):
        logging.debug('Enter content ')
        content_field = self.find_element(self.ids['content_field'])
        if content_field:
            content_field.send_keys(self.info['content'])
        else:
            logging.error('Поле для ввода контента не надено')    

    def click_contact_us_button(self):
        logging.debug('Click contact us button ')
        cont_us_btn = self.find_element(self.ids['contact_us_btn'])
        if cont_us_btn:
            cont_us_btn.click()
        else:
            logging.error('Кнопка contact us не найдена')

    def switch_alert(self):
        logging.info("Switch alert")
        text = self.alert()
        logging.info(text)
        return text
    