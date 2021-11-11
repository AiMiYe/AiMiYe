import wx


class CreateFrame(wx.Frame):
    def __init__(self, parent=None, title=None, size=None, name=None):
        super().__init__(parent=parent, title=title, size=size, name=name)
    # TODO


class CreateApp(wx.App):
    def __init__(self):
        super().__init__()

    def OnInit(self):
        frame = CreateFrame(parent=None, title='The calculator', size=(400, 400), name='The calculator')  # 创建窗口
        icon = wx.Icon(name=r'../others/img/1636031347382.jpg', type=wx.BITMAP_TYPE_JPEG)  # 加载图标
        frame.SetIcon(icon)  # 窗口设置图标
        frame.Show()  # 显示窗口
        return True

    def OnExit(self):
        print("退出应用程序")
        return 0


if __name__ == '__main__':
    app = CreateApp()  # 创建应用程序对象
    app.MainLoop()  # 运行主任务循环（应用程序）
