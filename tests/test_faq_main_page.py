import pytest
from locators.main_page_locators import MainPageLocators
from testdata import AnswersFAQ
from page_objects.main_page import MainPage
import allure

class TestMainPageFAQ:
    @pytest.mark.parametrize(
        'question, answer, expected',
        [
            (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, AnswersFAQ.answer_1),
            (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, AnswersFAQ.answer_2),
            (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, AnswersFAQ.answer_3),
            (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, AnswersFAQ.answer_4),
            (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, AnswersFAQ.answer_5),
            (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, AnswersFAQ.answer_6),
            (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, AnswersFAQ.answer_7),
            (MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8, AnswersFAQ.answer_8)
        ]
        )
    @allure.title('Проверяем, что при клике на вопрос открывается соответствующий ответ')
    @allure.description('Открываем вопрос, нажимаем на него, сверяем ответ с ожидаемым текстом')
    def test_answers_in_faq(self, driver, question, answer, expected):
        landing_page = MainPage(driver)
        landing_page.click_cookie_button()
        landing_page.scroll_page(question)
        landing_page.wait_for_element_to_be_clickable(question)
        landing_page.click_element(question)
        landing_page.wait_visibility_element(answer)
        actuall_text = landing_page.get_actually_text(answer)
        assert actuall_text == expected




