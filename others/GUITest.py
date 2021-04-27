import pyautogui


class AutoGui:

    @classmethod
    def get_current_coordinates(cls):
        return pyautogui.position()

    @classmethod
    def get_screen_resolution(cls):
        return pyautogui.size()


if __name__ == '__main__':
    print(AutoGui.get_current_coordinates())
    print(AutoGui.get_screen_resolution())
