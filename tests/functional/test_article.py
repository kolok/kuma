import pytest

from pages.article import ArticlePage


# page title
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_title_is_expected(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.title_is_expected()


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_title_in_title(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.title_in_title()


# article
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_article_title_is_expected(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.article_title_is_expected


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_article_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.article_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_article_column_left_present(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.article_column_left_present


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_article_column_content_present(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.article_column_content_present


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_article_column_right_present(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.article_column_right_present


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_article_columns_locations(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.article_columns_locations


# page buttons
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_language_menu_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.language_menu_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_edit_button_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.edit_button_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_advanced_menu_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.advanced_menu_is_displayed


# header tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_header_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Header.is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_header_menu_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Header.menu_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_header_platform_submenu_displays(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.header.platform_submenu_displays()


# footer tests
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_footer_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Footer.is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_privacy_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Footer.privacy_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_license_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Footer.license_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_select_language_is_displayed(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Footer.select_language_is_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_select_language_is_locale_match(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    assert page.Footer.select_language_is_locale_match
