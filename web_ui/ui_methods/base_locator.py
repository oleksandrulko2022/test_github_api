from playwright.sync_api import expect
from settings.project_setting import PW_EXPECT_TIMEOUT

expect.set_options(timeout=int(PW_EXPECT_TIMEOUT))

class BaseLocator:

    button = 'xpath=.//button'

