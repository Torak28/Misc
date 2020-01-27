import xlrd
import datetime
import os
from tkinter import filedialog
from tkinter import *
from string import ascii_uppercase


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=1)}
data = {
    'code' :            { 'row_xlsx': 1, 'row_txt': [8, 10], 'req': True},
    'name' :            { 'row_xlsx': 2, 'row_txt': [9, 11], 'req': True},
    'date' :            { 'row_xlsx': '','row_txt': [12], 'req': True},
    'light_color' :     { 'row_xlsx': 3, 'row_txt': [30], 'req': True},
    'cri' :             { 'row_xlsx': 4, 'row_txt': [31], 'req': True},
    'power' :           { 'row_xlsx': 5, 'row_txt': [32], 'req': True},
    'led_chip' :        { 'row_xlsx': 6, 'row_txt': [29], 'req': True},
    'type_of_lamps' :   { 'row_xlsx': 7, 'row_txt': [28], 'req': True},
    'open_file' :       { 'row_xlsx': 8, 'row_txt': []},
    'output_file' :     { 'row_xlsx': 9, 'row_txt': []},

    'symetric' :        { 'row_xlsx': False, 'row_txt': [2], 'req': False},
    'light_sym' :       { 'row_xlsx': False, 'row_txt': [3], 'req': False},
    'length' :          { 'row_xlsx': False, 'row_txt': [13], 'req': False},
    'width' :           { 'row_xlsx': False, 'row_txt': [14], 'req': False},
    'height' :          { 'row_xlsx': False, 'row_txt': [15], 'req': False},
    'length_area' :     { 'row_xlsx': False, 'row_txt': [16], 'req': False},
    'width_area' :      { 'row_xlsx': False, 'row_txt': [17], 'req': False}
}

def perform(xlxs_file, output_file):
    return_str = 'Operation done'
    fail_count = 0

    os.chdir(os.path.dirname(xlxs_file))
    output_file = xlxs_file.replace(text_xlxs.get(), output_file)
    wb = xlrd.open_workbook((xlxs_file))
    sheet = wb.sheet_by_index(0)

    all_cols = []
    for i in range(sheet.ncols):
        all_cols.append(str(sheet.cell_value(0, i)))
    
    if 'długość oprawy' in all_cols:
        data['length']['row_xlsx'] = all_cols.index('długość oprawy')
    elif 'szerokość oprawy' in all_cols:
        data['width']['row_xlsx'] = all_cols.index('szerokość oprawy')
    elif 'wysokość oprawy' in all_cols:
        data['height']['row_xlsx'] = all_cols.index('wysokość oprawy')
    elif 'długość obszaru świetlnego' in all_cols:
        data['length_area']['row_xlsx'] = all_cols.index('długość obszaru świetlnego')
    elif 'szerokość obszaru świetlnego' in all_cols:
        data['width_area']['row_xlsx'] = all_cols.index('szerokość obszaru świetlnego')
    elif 'oprawa symetryczna' in all_cols:
        data['symetric']['row_xlsx'] = all_cols.index('oprawa symetryczna')
    elif 'źródło światła symetryczne' in all_cols:
        data['light_sym']['row_xlsx'] = all_cols.index('źródło światła symetryczne')

    row_number = 0
    wat = True
    while wat:
        try:
            x = sheet.cell_value(row_number, 0)
            cell_type = sheet.cell_type(row_number, 0)
            if cell_type == 1:
                # String
                if row_number == 0:
                    pass
                else:
                    raise Exception('Bad cell type')
            elif cell_type == 2:
                # Number
                file_to_open = sheet.cell_value(row_number, data['open_file']['row_xlsx'])
                name_file_to_save = sheet.cell_value(row_number, data['output_file']['row_xlsx'])
                str_date = datetime.datetime.today().strftime('%d.%m.%Y\t%X')
                out = open(output_file, 'a')
                out_str = ''
                try:
                    with open(file_to_open) as fp:
                        str_to_save = ''
                        for i, line in enumerate(fp):
                            if i + 1 in data['code']['row_txt']:
                                str_to_save += str(sheet.cell_value(row_number, data['code']['row_xlsx'])) + '\n'
                            elif i + 1 in data['name']['row_txt']:
                                str_to_save += str(sheet.cell_value(row_number, data['name']['row_xlsx'])) + '\n'
                            elif i + 1 in data['date']['row_txt']:
                                str_to_save += str_date + '\n'
                            elif i + 1 in data['light_color']['row_txt']:
                                str_to_save += str(int(sheet.cell_value(row_number, data['light_color']['row_xlsx']))) + '\n'
                            elif i + 1 in data['cri']['row_txt']:
                                str_to_save += str(int(sheet.cell_value(row_number, data['cri']['row_xlsx']))) + '\n'
                            elif i + 1 in data['power']['row_txt']:
                                str_to_save += str(int(sheet.cell_value(row_number, data['power']['row_xlsx']))) + '\n'
                            elif i + 1 in data['led_chip']['row_txt']:
                                str_to_save += str(float(sheet.cell_value(row_number, data['led_chip']['row_xlsx']))) + '\n'
                            elif i + 1 in data['type_of_lamps']['row_txt']:
                                str_to_save += str(sheet.cell_value(row_number, data['type_of_lamps']['row_xlsx'])) + '\n'

                            elif i + 1 in data['symetric']['row_txt'] and type(data['symetric']['row_xlsx']) is int:
                                if sheet.cell_type(row_number, data['symetric']['row_xlsx']) == 2:
                                    str_to_save += str(sheet.cell_value(row_number, data['symetric']['row_xlsx'])) + '\n'
                                else:
                                    str_to_save += line
                            elif i + 1 in data['light_sym']['row_txt'] and type(data['light_sym']['row_xlsx']) is int:
                                if sheet.cell_type(row_number, data['light_sym']['row_xlsx']) == 2:
                                    str_to_save += str(sheet.cell_value(row_number, data['light_sym']['row_xlsx'])) + '\n'
                                else:
                                    str_to_save += line
                            elif i + 1 in data['length']['row_txt'] and type(data['length']['row_xlsx']) is int:
                                if sheet.cell_type(row_number, data['length']['row_xlsx']) == 2:
                                    str_to_save += str(sheet.cell_value(row_number, data['length']['row_xlsx'])) + '\n'
                                else:
                                    str_to_save += line
                            elif i + 1 in data['width']['row_txt'] and type(data['width']['row_xlsx']) is int:
                                if sheet.cell_type(row_number, data['width']['row_xlsx']) == 2:
                                    str_to_save += str(sheet.cell_value(row_number, data['width']['row_xlsx'])) + '\n'
                                else:
                                    str_to_save += line
                            elif i + 1 in data['height']['row_txt'] and type(data['height']['row_xlsx']) is int:
                                if sheet.cell_type(row_number, data['height']['row_xlsx']) == 2:
                                    str_to_save += str(sheet.cell_value(row_number, data['height']['row_xlsx'])) + '\n'
                                else:
                                    str_to_save += line
                            elif i + 1 in data['length_area']['row_txt'] and type(data['length_area']['row_xlsx']) is int:
                                if sheet.cell_type(row_number, data['length_area']['row_xlsx']) == 2:
                                    str_to_save += str(sheet.cell_value(row_number, data['length_area']['row_xlsx'])) + '\n'
                                else:
                                    str_to_save += line
                            elif i + 1 in data['width_area']['row_txt'] and type(data['width_area']['row_xlsx']) is int:
                                if sheet.cell_type(row_number, data['width_area']['row_xlsx']) == 2:
                                    str_to_save += str(sheet.cell_value(row_number, data['width_area']['row_xlsx'])) + '\n'
                                else:
                                    str_to_save += line
                            elif i + 1 in data['symetric']['row_txt'] and type(data['symetric']['row_xlsx']) is int:
                                if sheet.cell_type(row_number, data['symetric']['row_xlsx']) == 2:
                                    str_to_save += str(sheet.cell_value(row_number, data['symetric']['row_xlsx'])) + '\n'
                                else:
                                    str_to_save += line
                            elif i + 1 in data['light_sym']['row_txt'] and type(data['light_sym']['row_xlsx']) is int:
                                if sheet.cell_type(row_number, data['light_sym']['row_xlsx']) == 2:
                                    str_to_save += str(sheet.cell_value(row_number, data['light_sym']['row_xlsx'])) + '\n'
                                else:
                                    str_to_save += line
                            else:
                                str_to_save += line
                    f = open(name_file_to_save, 'w+')
                    f.write(str_to_save)
                    f.close()
                    out_str += str(sheet.cell_value(row_number, data['code']['row_xlsx'])) + '\t' + 'done' + '\n'
                except IOError:
                    out_str += str(sheet.cell_value(row_number, data['code']['row_xlsx'])) + '\t' + 'file not found(' + file_to_open + ')\n'
                    fail_count += 1
                finally:
                    out.write(out_str)

            else:
                pass
            row_number += 1
        except IndexError as bad_thing:
            wat = False
    if fail_count != 0:
        return_str += '\n' + str(fail_count) + 'file(s) were not find'
    return return_str

fields = ['XLXS File', 'Output File']

def makeform(root, fields):
    entries = []
    for field in fields:
        if field == 'XLXS File':
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            xd = Button(row, textvariable=text_xlxs, command=(lambda e=root: select_xlxs(root)))
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            xd.pack(side=RIGHT, expand=YES, fill=X)
        else:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
    return entries

def select_xlxs(root):
    root.filename =  filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
    display = os.path.basename(root.filename)
    text_xlxs.set(display)
    path_to_xlsl.set(root.filename)
    root.update_idletasks()

def Info():
    window = Toplevel(root)
    window.title('Info')
    w1 = Label(window)
    w1.pack(side='bottom')
    w2 = Label(window,  padx = 10, justify=LEFT, text="Aplikacja do generowania plików LDT na podstawie XLXS\nAutor: Jarosław Ciołek-Żelechowski\nurl: https://github.com/Torak28/Misc/tree/master/DominikJob")
    w2.pack(side='top')

def Options(e):
    window = Toplevel(root)
    window.title('Options')
    w1 = Label(window)
    w1.pack(side='bottom')
    keys = list(data.keys())
    keys.remove('date')
    keys.remove('open_file')
    keys.remove('output_file')
    keys = keys[::-1]
    for key in keys:
        w2 = Label(window)
        w2.pack(side='bottom')
        lab = Label(w2,  padx = 10, text=key, width=15, anchor='w')
        lab.pack(side=LEFT)
        lab2 = Label(w2,  padx = 10, text="xlsx column:")
        lab2.pack(side=LEFT)
        ent1Text = StringVar()
        ent1 = Entry(w2, textvariable=ent1Text)
        wtf_is_this_line = list(LETTERS.keys())[list(LETTERS.values()).index(str(data[key]['row_xlsx']))]
        ent1Text.set(wtf_is_this_line)
        ent1.pack(side=LEFT, expand=YES, fill=X)
        lab3 = Label(w2,  padx = 10, text="ldt row:")
        lab3.pack(side=LEFT)
        ent2Text = StringVar()
        ent2 = Entry(w2, textvariable=ent2Text)
        ent2Text.set(data[key]['row_txt'])
        ent2.pack(side=LEFT, expand=YES, fill=X)
        check = Checkbutton(w2, text = "required")
        check.pack(side=LEFT, expand=YES, fill=X)

def Run(e):

    def close_window(root): 
        root.destroy()

    if not path_to_xlsl.get():
        window = Toplevel(root)
        window.title('Error')
        w3 = Label(window,  padx = 10, justify=LEFT, text="File XLXS is not selected")
        w3.pack(side='top')
        Ok = Button(window, text='OK', command=(lambda e=window: close_window(e)))
        Ok.pack(side=BOTTOM, padx=5, pady=5)
    elif not e[0][1].get():
        window = Toplevel(root)
        window.title('Error')
        w3 = Label(window,  padx = 10, justify=LEFT, text="Output file field is empty")
        w3.pack(side='top')
        Ok = Button(window, text='OK', command=(lambda e=window: close_window(e)))
        Ok.pack(side=BOTTOM, padx=5, pady=5)
    else:
        odp_str = perform(str(path_to_xlsl.get()), e[0][1].get())
        window = Toplevel(root)
        window.title('Error')
        w5 = Label(window,  padx = 10, justify=LEFT, text=odp_str)
        w5.pack(side='top')
        Ok = Button(window, text='OK', command=(lambda e=window: close_window(e)))
        Ok.pack(side=BOTTOM, padx=5, pady=5)

def Exit_All(root): 
    root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('Generacja plików LDT')
    text_xlxs = StringVar()
    path_to_xlsl = StringVar()
    text_xlxs.set('No file selected')
    ents = makeform(root, fields)
    exit_all = Button(root, text='Exit', command=(lambda e=root: Exit_All(e)))
    exit_all.pack(side=RIGHT, padx=5, pady=5)
    Info = Button(root, text='Info', command=Info)
    Info.pack(side=RIGHT, padx=5, pady=5)
    run = Button(root, text='Run', command=(lambda e=ents: Run(e)))
    run.pack(side=RIGHT, padx=5, pady=5)
    # options = Button(root, text='Options', command=(lambda e=ents: Options(e)))
    # options.pack(side=RIGHT, padx=5, pady=5)
    root.mainloop()