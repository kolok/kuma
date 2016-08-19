from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from pypom import Page, Region


class BasePage(Page):

    URL_TEMPLATE = '/{locale}'

    def __init__(self, selenium, base_url, locale='en-US', **url_kwargs):
        super(BasePage, self).__init__(selenium, base_url, locale=locale, **url_kwargs)

    def wait_for_page_to_load(self):
        self.wait.until(lambda s: self.seed_url in s.current_url)
        el = self.find_element(By.TAG_NAME, 'html')
        self.wait.until(lambda s: el.get_attribute('data-ffo-opensanslight'))
        return self

    @property
    def header(self):
        return self.Header(self)

    @property
    def footer(self):
        return self.Footer(self)

    class Header(Region):
        report_content_form_url = 'https://bugzilla.mozilla.org/form.doc'
        report_bug_form_url = 'https://bugzilla.mozilla.org/form.mdn'
        # locators
        _root_locator = (By.ID, 'main-header')
        _menu_locator = (By.ID, 'nav-main-menu')
        _platform_submenu_trigger_locator = (By.XPATH, 'id(\'nav-platform-submenu\')/..')
        _platform_submenu_locator = (By.ID, 'nav-platform-submenu')
        _platform_submenu_item_locator = (By.CSS_SELECTOR, '#nav-platform-submenu a')
        _feedback_link_locator = (By.XPATH, 'id(\'nav-contact-submenu\')/../a')
        _feedback_submenu_trigger_locator = (By.XPATH, 'id(\'nav-contact-submenu\')/..')
        _feedback_submenu_locator = (By.ID, 'nav-contact-submenu')
        _report_content_locator = (By.CSS_SELECTOR, 'a[href^="' + report_content_form_url + '"]')
        _report_bug_locator = (By.CSS_SELECTOR, 'a[href^="' + report_bug_form_url + '"]')

        # is displayed?
        @property
        def is_displayed(self):
            return self.root.is_displayed()

        # nav is displayed?
        @property
        def menu_is_displayed(self):
            return self.find_element(*self._menu_locator).is_displayed()

        def platform_submenu_displays(self):
            submenu_trigger = self.find_element(*self._platform_submenu_trigger_locator)
            submenu = self.find_element(*self._platform_submenu_locator)
            hover = ActionChains(self.selenium).move_to_element(submenu_trigger)
            # trigger is diplayed
            assert submenu_trigger.is_displayed()
            assert not submenu.is_displayed()
            # hover
            hover.perform()
            self.wait.until(lambda s: submenu.is_displayed())
            # menu is displayed
            return submenu.is_displayed()

        def open_feedback(self):
            self.find_element(*self._feedback_link_locator).click()
            from pages.feedback import FeedbackPage
            return FeedbackPage(self.selenium, self.page.base_url).wait_for_page_to_load()

        def report_content_submits(self, base_url):
            submenu_trigger = self.find_element(*self._feedback_submenu_trigger_locator)
            submenu = self.find_element(*self._feedback_submenu_locator)
            report_content_link = self.find_element(*self._report_content_locator)
            hover_trigger = ActionChains(self.selenium).move_to_element(submenu_trigger)
            # trigger is diplayed
            assert submenu_trigger.is_displayed()
            assert not submenu.is_displayed()
            # hover
            hover_trigger.perform()
            # menu is displayed
            self.wait.until(lambda s: submenu.is_displayed())
            # report menu item is displayed
            assert report_content_link.is_displayed()
            # store url of reporting page
            # report_url = self.selenium.current_url
            # click link
            report_content_link.click()
            # bugzilla loads in new window
            self.selenium.switch_to_window(self.selenium.window_handles[1])
            # check form loaded
            assert self.report_content_form_url in self.selenium.current_url


        def report_bug_submits(self):
            submenu_trigger = self.find_element(*self._feedback_submenu_trigger_locator)
            submenu = self.find_element(*self._feedback_submenu_locator)
            report_bug_link = self.find_element(*self._report_bug_locator)
            hover_trigger = ActionChains(self.selenium).move_to_element(submenu_trigger)
            # trigger is diplayed
            assert submenu_trigger.is_displayed()
            assert not submenu.is_displayed()
            # hover
            hover_trigger.perform()
            # menu is displayed
            self.wait.until(lambda s: submenu.is_displayed())
            # report menu item is displayed
            assert report_bug_link.is_displayed()
            # click link
            report_bug_link.click()
            # check form loaded
            assert self.report_bug_form_url in self.selenium.current_url

    class Footer(Region):
        privacy_url = 'https://www.mozilla.org/privacy/websites/'
        copyright_id = 'Copyrights_and_licenses'
        # locators
        _root_locator = (By.CSS_SELECTOR, 'body > footer')
        _language_locator = (By.ID, 'language')
        _privacy_locator = (By.CSS_SELECTOR, 'a[href^="' + privacy_url + '"]')
        _license_locator = (By.CSS_SELECTOR, 'a[href="/docs/MDN/About#' + copyright_id + '"]')

        # is displayed?
        @property
        def is_displayed(self):
            return self.root.is_displayed()

        # language select is displayed
        @property
        def select_language_is_displayed(self):
            return self.find_element(*self._language_locator).is_displayed()

        # check lanuage selected in drop down matches locale
        @property
        def select_language_is_locale_match(self, locale):
            # get language selected
            language_select = self.find_element(*self._language_locator)
            selected_option = language_select.find_element('option[selected]')
            selected_language = selected_option.get_attribute('value')
            return (selected_language == locale)

        # privacy link is displayed
        @property
        def privacy_is_displayed(self):
            return self.find_element(*self._privacy_locator).is_displayed()

        # license link is displayed
        @property
        def license_is_displayed(self):
            return self.find_element(*self._license_locator).is_displayed()
