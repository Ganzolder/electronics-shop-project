from src.item import Item


class LangSwapper:

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self.language == 'EN':
            self._language = 'RU'

        elif self.language == 'RU':
            self._language = 'EN'

        return self


class Keyboard(Item, LangSwapper):
    pass
