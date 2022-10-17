import PySimpleGUI as sg
from snippets import QuickScatter



def make_window(
    theme = 'Python',
    use_custom_titlebar = False
    ):

    sg.theme(theme)

    r_layout = [
        [sg.FolderBrowse('Working Folder'), sg.T('Folder', s=(40))],
        [sg.FileBrowse('text file', k='text', file_types=[('Text file','*.txt')]), sg.T('file.txt', s=(40))],
        [sg.FileBrowse('excel file', k='excel', file_types=[('Excel file','*.xlsx')]), sg.T('file.xlsx', s=(40))],
        ]

    l_layout = [
        [sg.Checkbox('test', False, enable_events=True, k='-TEST-')],
        [sg.T('ProgressBar'), ],
        [sg.ProgressBar(100, orientation='h', s=(9, 8), k='-PBAR-')],
        [sg.Slider((0,100), orientation='h', s=(13, 8), enable_events=True, k='-SLIDE-')],
        [sg.T('Slider')],
        ]

    layout = [
        [sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)] if use_custom_titlebar else [sg.Menu([['Fart', ['Exit']], ['Poop', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
        [sg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-')],
        [sg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 18', justification='c', expand_x=True)], [sg.Text('Combo'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
        [sg.Col(l_layout), sg.Col(r_layout)],
        ]


    window = sg.Window('My custom practice GUI', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

    #window['-PBAR-'].update(30)                                                     # Show 30% complete on ProgressBar
    #window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

    return window



#%% run
if __name__ == '__main__':
    # Start of the program...
    window = make_window()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if values['-COMBO-'] != sg.theme():
            theme = values['-COMBO-']
            window.close()
            window = make_window(theme=theme)
        if event == '-USE CUSTOM TITLEBAR-':
            use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
            window.close()
            window = make_window(use_custom_titlebar=use_custom_titlebar)
        if event == '-SLIDE-':
            window['-PBAR-'].update(values['-SLIDE-'])
        if event not in ['-COMBO-', '-SLIDE-']:
            sg.popup(event, values, keep_on_top=True)
        if event == '-TEST-':
            fig, ax = QuickScatter()
            fig.show()

    window.close()