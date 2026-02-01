import re
from typing import Literal
from playwright.sync_api import expect
from web_ui.ui_methods.base_locator import BaseLocator

class HomepageMethod(BaseLocator):
    def __init__(self, page:object=None):
        self.page = page

        self.block_search_form = 'xpath=.//form[@id="search-form"]'
        self.block_lang_primary = 'xpath=.//nav[@data-el-section="primary links"]'
        self.block_wikipedia_in_your_lang = 'xpath=.//div[@id="js-lang-lists"]'
        self.block_app_mobile = 'xpath=.//div[@class="footer-sidebar app-badges"]'
        self.block_other_projects = 'xpath=.//nav[@class="other-projects"]'
        self.btn_search_lang = 'xpath=.//select[@id="searchLanguage"]'
        self.btn_read_wikipedia_in_your_lang = 'xpath=.//button[@id="js-lang-list-button"]'
        self.btn_wikipedia_for_android_or_ios = 'xpath=.//a[@data-jsl10n="portal.app-links.url"]'
        self.icon_search_lang = 'xpath=.//label[@for="searchLanguage"]'
        self.icon_google = 'xpath=.//li[@class="app-badge app-badge-android"]'
        self.icon_ios = 'xpath=.//li[@class="app-badge app-badge-ios"]'
        self.option = 'xpath=.//option'
        self.strong = 'xpath=.//strong'
        self.a = 'xpath=.//a'
        self.span = 'xpath=.//span'

    def check_icon_select_language(self, icon_name) -> object:
        block = self.page.locator(self.block_search_form)
        icon = block.locator(self.icon_search_lang)
        expect(icon).to_have_text(icon_name)

    def click_dandruff_in_search_field(self)->None:
        block = self.page.locator(self.block_search_form)
        block.locator(self.button).click()

    def click_select_language_icon_in_search_field(self,  return_list:bool=True):
        block = self.page.locator(self.block_search_form)
        block.locator(self.btn_search_lang).click()
        if return_list:
            return block.locator(self.btn_search_lang)
        return None

    def click_lang_under_text_the_free_encyclopedia(self,  value):
        block = self.page.locator(self.block_lang_primary)
        block.locator(self.strong).filter(has_text=value).click()

    def click_button_read_wikipedia_in_your_language(self,  return_block:bool=True):
        self.page.locator(self.btn_read_wikipedia_in_your_lang).click()
        if return_block:
            return self.page.locator(self.block_wikipedia_in_your_lang)
        return None
    
    def click_mobile_app_icon(self,  icon_type:Literal['android', 'ios']='android'):
        viewport = self.page.viewport_size
        block = self.page.locator(self.block_app_mobile)
        with self.page.context.expect_page() as window:
            match icon_type:
                case 'android':
                    block.locator(self.icon_google).click()
                case 'ios':
                    block.locator(self.icon_ios).click()
            new_page = window.value
            new_page.set_viewport_size({'width': viewport['width'], 'height': viewport['height']})
            return new_page
        
    def click_button_download_wikipedia_for_android_or_ios(self):
        block = self.page.locator(self.block_app_mobile)
        block.locator(self.btn_wikipedia_for_android_or_ios).click()

    def click_button_other_projects(self, value):
        block = self.page.locator(self.block_other_projects)
        block.locator(self.span).filter(has_text=value).click()

    def select_language_option_in_search_field(self, opened_list, value):
        opened_list.select_option(self.option, label=value)

    def select_language_in_wikipedia_in_your_lang(self, block, value):
       block.locator(self.a).filter(has_text=re.compile(rf"^{value}$")).click()

