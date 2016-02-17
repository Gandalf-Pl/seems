# coding: utf8

from splinter import Browser


def test_search_google():
    with Browser() as browser:
        # Visit URL
        url = "http://www.google.com.sg"
        browser.visit(url)
        browser.fill('q', 'splinter - python acceptance testing for web applications')
        import ipdb
        ipdb.set_trace()
        # Find and click the 'search' button
        button = browser.find_by_name('btnG')
        # Interact with elements
        button.click()
        if browser.is_text_present('splinter.readthedocs.org'):
            print("Yes, the official website was found!")
        else:
            print("No, it wasn't found... We need to improve our SEO techniques")


def test_staging():
    browser = Browser()
    browser.visit("http://staging.waimaichaoren.com/")
    browser.quit()

test_staging()
