import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

@pytest.mark.parametrize('mobile_os_settings',
                         [('9.0', 'android', 'Motorola Moto G7 Play')],
                         ids=['android'],
                         indirect=True)
def test_search_and_click(mobile_os_settings):

    with step('Searching "Appium"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify found page'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

    with step ('Open "Appium" page'):
        appium_page = results.first
        appium_page.click()


