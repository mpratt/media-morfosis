import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from os.path import basename
from .converter import Converter
from .options import OPTIONS

def run_gui():
    window = tk.Tk()
    window.geometry('340x150')
    window.title('Media Morfosis')
    selection = tk.StringVar(window, value='Choose an operation...')
    progress_bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length='330', mode='determinate')
    progress_label = ttk.Label(window, text= '')

    def action_dropdown_selected_event(choice):
        selected = OPTIONS[choice]
        extension = selected.split('_')[0]
        files = fd.askopenfilenames(filetypes = [ (('Media Files', '*.{}'.format(extension))) ], title = 'Choose Files to be converted' )

        if not files:
            return

        percent = int(100/len(files))
        progress_bar.place(x=5, y=40)
        progress_label.place(x=5, y=60)

        progress_bar['value'] = 0
        window.update_idletasks()
        for f in files:
            progress_label['text'] = 'Processing: {}'.format(basename(f))
            window.update_idletasks()

            converter = Converter(f)
            method = getattr(converter, selected)
            method()

            progress_bar['value'] += percent

        progress_label['text'] = 'Done!'

    action_dropdown = tk.OptionMenu(window, selection, *OPTIONS.keys(), command = action_dropdown_selected_event)
    action_dropdown.config(width=340)
    action_dropdown.pack()

    window.mainloop()

if __name__ == '__main__':
    run_gui()
