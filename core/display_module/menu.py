from display_module.display_module import TaAssisDisplay


class Menu(TaAssisDisplay):
    def __init__(self, menu_item):
        # Date Structure
        # {
        #   "selection_char": ("description", Call Back Method)
        # }
        self.__menu_item = menu_item

    def pick(self):
        menu_text = "".join(
            ["({}) {},".format(key, value[0]) for key, value in self.__menu_item.items()])
        menu_text = menu_text[0:-1]
        menu_text += ": "
        while True:
            selection = self.input_from_user(menu_text)
            if selection not in self.__menu_item:
                self.failure(
                    "Invalid input. Please input only the char in the Parenthesis")
                continue
            return self.__menu_item[selection][1]()
