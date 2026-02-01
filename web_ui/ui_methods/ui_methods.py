from web_ui.ui_methods.general_method import GeneralMethod
from web_ui.ui_methods.homepage_method import HomepageMethod

class UIMethods:

    def __init__(self, page) -> None:
        self.homepage = HomepageMethod(page)
        self.general = GeneralMethod(page)