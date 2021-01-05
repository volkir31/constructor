from tkinter import *
from add.code_blocks import *


class Constructor(Tk):
    my_list_of_entries = list()
    req = []
    res = []

    def __init__(self):
        super().__init__()
        self.geometry('500x600')
        self.title('Bot Constructor')
        self.iconbitmap('add/lego.ico')

        # filename
        file_name = StringVar()
        self.filename = Entry(self, textvariable=file_name)
        Label(text='File name without ".py"').pack()
        self.filename.pack()

        # token
        token = StringVar()
        self.ent = Entry(self, textvariable=token)
        Label(text='token').pack()
        self.ent.pack()

        # textfield
        self.text = Text(self, width=50, height=10)
        self.text.pack()
        Label(text='Example:\nResponse -> request\ndelete: res -> req', font=("Consolas", 10)).pack()

        # script
        self.label = Label(self, text='Your script will be here')
        self.label.pack()
        self.script = ''

        Button(self, text='Create bot', command=self.create_bot).pack(side=BOTTOM)
        Button(self, text='Create script', command=self.create_script).pack(side=BOTTOM)
        Label(text='Firstly create script, \nif you sure everything is ready then click "create bot"',
              font=("Consolas", 11)).pack(side=BOTTOM)

    def delete_part(self):
        string = self.text.get(1.0, END)
        string = string.split(':')
        deleted_str = string[1].strip() + '\n'
        self.script = self.script.replace(deleted_str, '')

    def create_script(self):
        msg = self.text.get(1.0, END)
        if 'delete' in msg.lower():
            self.delete_part()
            self.label.configure(text=f'Your script:\n\nYour token: {self.ent.get()}\n\n{self.script}')
        else:
            self.script += msg
            self.label.configure(text=f'Your script:\n\nYour token: {self.ent.get()}\n\n{self.script}')

    def create_bot(self):
        msg_list = self.script.split('\n')
        for msg in msg_list:
            mes = msg.split('->')
            if msg != '':
                self.res.append(mes[0])
                self.req.append(mes[1])
        bot_creating(self.res, self.req, self.ent.get(), self.filename.get())
        print('Success! Bot was created')


if __name__ == '__main__':
    window = Constructor()
    mainloop()
