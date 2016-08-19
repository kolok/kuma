from pypom import Region
from selenium.webdriver.common.by import By

from pages.base import BasePage


class ArticlePage(BasePage):

    URL_TEMPLATE = '/{locale}/docs/User:anonymous:uitest'
    ARTICLE_NAME = 'User:anonymous:uitest'
    ARTICLE_TITLE_SUFIX = " | MDN"

    # article meta
    _page_buttons_locator = (By.CSS_SELECTOR, '#document-main .page-buttons')
    _language_menu_locator = (By.ID, 'languages-menu')
    _edit_button_locator = (By.ID, 'edit-button')
    _advanced_menu_locator = (By.ID, 'advanced-menu')
    # article head
    _article_title_locator = (By.CSS_SELECTOR, '#wiki-document-head h1')
    # article columns
    _article_column_container = (By.ID, 'wiki-column-container')
    _article_left_column_locator = (By.ID, 'wiki-left')
    _article_content_column_locator = (By.ID, 'wiki-content')
    _article_right_column_locator = (By.ID, 'wiki-right')
    # article
    _article_locator = (By.ID, 'wikiArticle')

    # document title is what's expected
    def title_is_expected(self):
        document_title_text = self.selenium.title
        expected_title_text = self.ARTICLE_NAME + self.ARTICLE_TITLE_SUFIX
        return document_title_text == expected_title_text

    # document title contains article title
    def title_in_title(self):
        document_title_text = self.selenium.title
        page_title_text = self.find_element(*self._article_title_locator).text
        return page_title_text in document_title_text

    # article title is what's expected
    @property
    def article_title_is_expected(self):
        return self.find_element(*self._article_title_locator).text == self.ARTICLE_NAME

    # page buttons are displayed
    @property
    def language_menu_is_displayed(self):
        return self.find_element(*self._language_menu_locator).is_displayed()

    @property
    def edit_button_is_displayed(self):
        return self.find_element(*self._edit_button_locator).is_displayed()

    @property
    def advanced_menu_is_displayed(self):
        return self.find_element(*self._advanced_menu_locator).is_displayed()

    # article columns
    @property
    def article_column_left_present(self):
        article_column_container = self.find_element(*self._article_column_container)
        # parent container expects left
        left_expected = 'wiki-left-present' in article_column_container.get_attribute("class")
        # left column is present
        left_present = self.find_element(*self._article_left_column_locator).is_displayed()
        return left_expected and left_present

    @property
    def article_column_content_present(self):
        return self.find_element(*self._article_content_column_locator).is_displayed()

    @property
    def article_column_right_present(self):
        article_column_container = self.find_element(*self._article_column_container)
        # parent container expects right
        right_expected = 'wiki-right-present' in article_column_container.get_attribute("class")
        # right column is present
        right_present = self.find_element(*self._article_right_column_locator).is_displayed()
        return right_expected and right_present

    @property
    def article_columns_locations(self):
        right_column_location = self.find_element(*self._article_right_column_locator).location
        content_column_location = self.find_element(*self._article_content_column_locator).location
        left_column_location = self.find_element(*self._article_left_column_locator).location
        # check y coordinates all the same
        y_match = right_column_location['y'] == content_column_location['y'] == left_column_location['y']
        # check x coordinates are acsending
        x_acsend = (right_column_location['x'] > content_column_location['x']) and (content_column_location['x'] > left_column_location['x'])
        return y_match and x_acsend

    # article wrapper is displayed
    @property
    def article_is_displayed(self):
        return self.find_element(*self._article_locator).is_displayed()
