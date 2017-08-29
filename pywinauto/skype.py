from pywinauto.application import Application
import time
app = Application(). connect(path = r"C:\Program Files (x86)\Microsoft Office\root\Office16\lync.exe")
#app.SkypeforBusiness.print_control_identifiers()
time.sleep(2)
#app.OptionsDialog.print_control_identifiers() 
#app.OptionsDialog.TabControl[0].Personal.Click()
#tabc = app['Personal'].TabControl.WrapperObject()
#tabc.Select(1)

tab=app.OptionsDialog.General.ConversationWindow.Reopenmy.Click()
tab.print_control_identifiers()
#tab.Select()

