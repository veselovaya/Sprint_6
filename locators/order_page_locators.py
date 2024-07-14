from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_ORDER = (By.XPATH, '//input[@placeholder="* Имя"]')
    LASTNAME_ORDER = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_ORDER = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_ORDER = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_BULVAR_STATION = (By.XPATH, '//div[text()="Бульвар Рокоссовского"]')
    METRO_CHERKIZOVSKAYA = (By.XPATH, '//div[text()="Черкизовская"]')
    PHONE_ORDER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()= "Далее"]')
    DATE_ORDER = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD = (By.XPATH, '//div[text()="* Срок аренды"]')
    ONE_DAY_RENTAL = (By.XPATH, '//div[text()="сутки"]')
    TWO_DAYS_RENTAL = (By.XPATH, '//div[text()="двое суток"]')
    BLACK_COLOR = (By.ID, 'black')
    GREY_COLOR = (By.ID, 'grey')
    COMMENT_ORDER = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    CONFIRM_ORDER = (By.XPATH, '//button[text()="Да"]')
    CHECK_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]')


