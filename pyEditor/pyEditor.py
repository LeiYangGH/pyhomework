import sys
import os                                    
from tkinter import *
from tkinter.filedialog   import Open              
from tkinter.messagebox   import showinfo, showerror, askyesno
from tkinter.simpledialog import askstring, askinteger
from tkinter.colorchooser import askcolor

SEL_FIRST = SEL + '.first'                 
SEL_LAST = SEL + '.last'                  
class TextEditor:                        
    
    editwindows = []                    
    testfile = 'test.txt'
    utf8 = 'utf-8'

    def __init__(self):
        self.lastfind = None
        self.openDialog = None
        self.text.focus()                           
        self.update()                           

    def start(self):                                
        self.toolBar = [('Open',  self.onOpen,   {'side': LEFT}),
            ('Save',  self.onSave,   {'side': LEFT}),
            ('Cut',   self.onCut,    {'side': LEFT}),
            ('Copy',  self.onCopy,   {'side': LEFT}),
            ('Paste', self.onPaste,  {'side': LEFT}),
            ('Find',  self.onRefind, {'side': LEFT}),
            ('Count',  self.onCount, {'side': LEFT})]

    def makeWidgets(self):                          
        name = Label(self, bg='black', fg='white')  
        name.pack(side=TOP, fill=X)                 
                                                    
        vbar = Scrollbar(self)
        hbar = Scrollbar(self, orient='horizontal')
        text = Text(self, padx=5, wrap='none')        

        vbar.pack(side=RIGHT,  fill=Y)
        hbar.pack(side=BOTTOM, fill=X)                 
        text.pack(side=TOP,    fill=BOTH, expand=YES)  

        text.config(yscrollcommand=vbar.set)    
        text.config(xscrollcommand=hbar.set)
        vbar.config(command=text.yview)         
        hbar.config(command=text.xview)         

        self.text = text
        self.filelabel = name

    def my_askopenfilename(self):
        if not self.openDialog:
           self.openDialog = Open(initialdir='.',
                                  filetypes=[('txt files',     '.txt')])
        return self.openDialog.show()

    def onOpen(self):
        self.testfile = self.my_askopenfilename()
        if not self.testfile: 
            return
        text = open(self.testfile, 'r', encoding=self.utf8).read()
        self.knownEncoding = self.utf8
        self.setAllText(text)
        self.setFileName(self.testfile)
        self.text.edit_reset()             
        self.text.edit_modified(0)         
        return
        
    def onSave(self):
        text = self.getAllText()
        self.update()
        file = open(self.testfile, 'w', encoding=self.utf8)
        file.write(text)
        file.close()
        self.setFileName(self.testfile)          
        self.text.edit_modified(0)          
        self.knownEncoding = self.utf8        

    def onCopy(self):                           
        if not self.text.tag_ranges(SEL):       
            showerror('PyEdit', 'No text selected')
        else:
            text = self.text.get(SEL_FIRST, SEL_LAST)
            self.clipboard_clear()
            self.clipboard_append(text)

    def onDelete(self):                         
        if not self.text.tag_ranges(SEL):
            showerror('PyEdit', 'No text selected')
        else:
            self.text.delete(SEL_FIRST, SEL_LAST)

    def onCut(self):
        if not self.text.tag_ranges(SEL):
            showerror('PyEdit', 'No text selected')
        else:
            self.onCopy()                       
            self.onDelete()

    def onPaste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
        except TclError:
            showerror('PyEdit', 'Nothing to paste')
            return
        self.text.insert(INSERT, text)          
        self.text.tag_remove(SEL, '1.0', END)
        self.text.tag_add(SEL, INSERT + '-%dc' % len(text), INSERT)
        self.text.see(INSERT)                   

    def onFind(self, lastkey=None):
        key = lastkey or askstring('PyEdit', 'Enter search string')
        self.text.update()
        self.text.focus()
        self.lastfind = key
        if key:                                                    
            nocase = True              
            where = self.text.search(key, INSERT, END, nocase=nocase)
            if not where:                                          
                showerror('PyEdit', 'String not found')
            else:
                pastkey = where + '+%dc' % len(key)           
                self.text.tag_remove(SEL, '1.0', END)         
                self.text.tag_add(SEL, where, pastkey)        
                self.text.mark_set(INSERT, pastkey)           
                self.text.see(where)                          

    def onRefind(self):
        self.onFind(self.lastfind)

    def onCount(self):
        text = self.getAllText()
        showinfo(title=None, message=str(len(text)))

    def getAllText(self):
        return self.text.get('1.0', END + '-1c')    
    def setAllText(self, text):
        self.text.delete('1.0', END)              
        self.text.insert(END, text)               
        self.text.mark_set(INSERT, '1.0')         
        self.text.see(INSERT)                     

    def setFileName(self, name):                  
        self.currfile = name  
        self.filelabel.config(text=str(name))

######################
class GuiMaker(Frame):
    toolBar = []                       

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)        
        self.start()                            
        self.makeToolBar()                      
        self.makeWidgets()                      

    def makeToolBar(self):
        if self.toolBar:
            toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
            toolbar.pack(side=BOTTOM, fill=X)
            for (name, action, where) in self.toolBar:
                Button(toolbar, text=name, command=action).pack(where)

    def makeWidgets(self):
        name = Label(self,
                     width=40, height=10,
                     relief=SUNKEN, bg='white',
                     text   = self.__class__.__name__,
                     cursor = 'crosshair')
        name.pack(expand=YES, fill=BOTH, side=TOP)

    def start(self): 
        "override me in subclass: set menu/toolbar with self"
        pass
######################
class TextEditorMain(TextEditor, GuiMaker):
    def __init__(self, parent=None):
        GuiMaker.__init__(self, parent)                  
        TextEditor.__init__(self) 
        self.master.protocol('WM_DELETE_WINDOW', self.onQuit)
        TextEditor.editwindows.append(self)

    def onQuit(self):
        GuiMaker.quit(self)

class TextEditorMainPopup(TextEditor, GuiMaker):
    def __init__(self, parent=None, winTitle=''):
        self.popup = Toplevel(parent)
        GuiMaker.__init__(self, self.popup)               
        TextEditor.__init__(self)  
        assert self.master == self.popup
        self.popup.protocol('WM_DELETE_WINDOW', self.onQuit)
        TextEditor.editwindows.append(self)

    def onQuit(self):
        self.popup.destroy()                       
        TextEditor.editwindows.remove(self)        

    def onClone(self): 
        TextEditor.onClone(self, makewindow=False)  
   
class TextEditorComponent(TextEditor, GuiMaker):
    def __init__(self, parent=None):     
        GuiMaker.__init__(self, parent)                   
        TextEditor.__init__(self)  

    def onQuit(self):
        self.destroy()   

class TextEditorComponentMinimal(TextEditor, GuiMaker):
    def __init__(self, parent=None, deleteFile=True):
        self.deleteFile = deleteFile
        GuiMaker.__init__(self, parent)                  
        TextEditor.__init__(self) 

    def start(self):
        TextEditor.start(self)                         

if __name__ == '__main__':                            
    fname = None
    TextEditorMain().pack(expand=YES, fill=BOTH)   
    mainloop()