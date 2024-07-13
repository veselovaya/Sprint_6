from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_1 = (By.ID, 'accordion__heading-0')
    ANSWER_1 = (By.XPATH, '//div[@id="accordion__panel-0"]/p')
    QUESTION_2 = (By.ID, 'accordion__heading-1')
    ANSWER_2 = (By.XPATH, '//div[@id="accordion__panel-1"]/p')
    QUESTION_3 = (By.ID, 'accordion__heading-2')
    ANSWER_3 = (By.XPATH, '//div[@id="accordion__panel-2"]/p')
    QUESTION_4 = (By.ID, 'accordion__heading-3')
    ANSWER_4 = (By.XPATH, '//div[@id="accordion__panel-3"]/p')
    QUESTION_5 = (By.ID, 'accordion__heading-4')
    ANSWER_5 = (By.XPATH, '//div[@id="accordion__panel-4"]/p')
    QUESTION_6 = (By.ID, 'accordion__heading-5')
    ANSWER_6 = (By.XPATH, '//div[@id="accordion__panel-5"]/p')
    QUESTION_7 = (By.ID, 'accordion__heading-6')
    ANSWER_7 = (By.XPATH, '//div[@id="accordion__panel-6"]/p')
    QUESTION_8 = (By.ID, 'accordion__heading-7')
    ANSWER_8 = (By.XPATH, '//div[@id="accordion__panel-7"]/p')

    COOKIE_BUTTON = (By.CLASS_NAME, 'App_CookieButton__3cvqF')

    SAMOKAT_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    ORDER_BUTTON_HEADER = (By.XPATH, '//button[@class = "Button_Button__ra12g"]')
    ORDER_BUTTON_MAIN_PAGE = (By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]')