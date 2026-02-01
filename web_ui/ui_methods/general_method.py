
import re
from playwright.sync_api import expect
from typing import Literal
from web_ui.ui_methods.base_locator import BaseLocator

class GeneralMethod(BaseLocator):
    def __init__(self, page):
        self.page = page

        self.h1 = 'xpath=//h1'
        self.h2 = 'xpath=//h2'
        self.all_text = 'xpath=//*'

    def check_open_page_with_url(self, url, timeout=30) -> object:
        expect(self.page).to_have_url(url, timeout=timeout*1000)

    def check_open_page_with_url_contains(self, url, timeout=30) -> object:
        expect(self.page).to_have_url(re.compile(f".*{url}.*"), timeout=timeout*1000)

    def check_open_page_with_header(self, exp_h, h_type:Literal['h1', 'h2']='h1') -> object:
        match h_type:
            case 'h1':
                act_h = self.page.locator(self.h1).filter(has_text=exp_h)
            case 'h2':
                act_h = self.page.locator(self.h2).filter(has_text=exp_h)
        expect(act_h).to_be_visible()

    def check_open_page_with_text(self, exp_text) -> object:
        act_h = self.page.locator(self.all_text).filter(has_text=exp_text)
        expect(act_h).not_to_have_count(0)

    def open_url(self, url):
        self.page.goto(url , wait_until="networkidle")
