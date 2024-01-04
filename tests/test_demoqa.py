import allure
from selene import browser, have, by
import os
from selene.support.shared.jquery_style import s


def test_steps(setup_browser):
    with allure.step('Открываем страницу и проверяем текст'):
        browser.open("/automation-practice-form")
        s('.practice-form-wrapper').should(have.text('Student Registration Form'))
    with allure.step('Вводим данные пользователя'):
        s('#firstName').type('Romanov')
        s('#lastName').type('Ivan')
        s('#userEmail').type('romanov.i@mail.com')
        s('#gender-radio-1').double_click()
        s('#userNumber').type('9087658909')
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').click().element(by.text('February')).click()
        s('.react-datepicker__year-select').click().element(by.text('2002')).click()
        s('.react-datepicker__day--006').click()
        s('#subjectsInput').send_keys('Maths').press_enter()
        s('[for=hobbies-checkbox-2]').click()
        s('#uploadPicture').send_keys(os.path.abspath('resources/images.jpeg'))
        s('#currentAddress').type('city Moscow, street Lenina')
        s('#react-select-3-input').type('Haryana').press_enter()
        s('#react-select-4-input').type('Karnal').press_enter()
        s('#submit').click()

    with allure.step('Проверка данных'):
        s('.modal-header').should(have.text('Thanks for submitting the form'))
        browser.all('tbody tr td:last-child').should(have.exact_texts(
        'Romanov Ivan', 'romanov.i@mail.com', 'Male', '9087658909', '06 February,2002', 'Maths',
        'Reading', 'images.jpeg', 'city Moscow, street Lenina', 'Haryana Karnal'))

    with allure.step('Закрыть окно'):
        s('.modal-footer').click()
