from page_objects.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import allure

class TestLogoHeader:

    @allure.title('Тест перехода на Дзен')
    @allure.description('При клике на лого Яндекса происходит редирект на Дзен')
    def test_click_logo_yandex(self, driver):

        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.wait_for_element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        main_page.click_element(MainPageLocators.YANDEX_LOGO)
        main_page.change_window(1)
        main_page.wait_url_until_not_about_blank()
        actuall_url = main_page.get_current_url()
        assert 'dzen.ru' in actuall_url

    @allure.title('Тест перехода на главную страницу СамокатЯндекс')
    @allure.description('При клике на лого "Самокат" происходит переход на главную страниц СамокатЯндекс')
    def test_click_samokat_logo(self, driver):

        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.wait_visibility_element(MainPageLocators.SAMOKAT_LOGO)
        main_page.click_element(MainPageLocators.ORDER_BUTTON_HEADER)
        main_page.wait_for_element_to_be_clickable(MainPageLocators.SAMOKAT_LOGO)
        main_page.click_element(MainPageLocators.SAMOKAT_LOGO)
        main_page.wait_visibility_element(MainPageLocators.SAMOKAT_LOGO)
        actual_url = main_page.get_current_url()
        assert actual_url == 'https://qa-scooter.praktikum-services.ru/'
