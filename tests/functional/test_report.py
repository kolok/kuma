import pytest

from pages.article import ArticlePage


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_report_content_submits(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    page.header.report_content_submits(selenium, page.URL_TEMPLATE)

@pytest.mark.smoke
@pytest.mark.nondestructive
def test_report_bug_submits(base_url, selenium):
    page = ArticlePage(selenium, base_url).open()
    page.header.report_bug_submits(selenium)
