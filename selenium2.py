import pywinauto
from pywinauto import application
import time


def open_tsm():
    app = application.Application().connect(title='TroubleShooting Machine For Web Apps')
    main_window = app.window(class_name='Chrome_WidgetWin_1', title_re=".*TroubleShooting Machine.*")
    time.sleep(2)

    main_window.set_focus()


    input_field.type_keys("https://space-int.solihull.jlrint.com/3dspace", with_spaces=True)
open_tsm()