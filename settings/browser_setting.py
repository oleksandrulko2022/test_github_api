from settings.project_setting import BROWSER_NAME, BROWSER_HEADLESS

class BrowserSetting():

    @staticmethod
    def init_desktop_driver(playwright):
        if BROWSER_HEADLESS == "true":
            headless = True
        else:
            headless = False
        if BROWSER_NAME == "chrome":
            return playwright.chromium.launch(headless=headless)

        if BROWSER_NAME == "firefox":
            return playwright.firefox.launch(headless=headless)

        if BROWSER_NAME == "safari":
            return playwright.webkit.launch(headless=headless)
