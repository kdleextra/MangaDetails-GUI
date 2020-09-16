from m_functions import *
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful
SIZE = (9,1)
status_values = ["0 = Unknown", "1 = Ongoing", "2 = Completed", "3 = Licensed"]
CLEAR=True
layout = [[sg.Text('Title ', size=SIZE), sg.Input(do_not_clear=CLEAR, key='title')],
          [sg.Text('Author ', size=SIZE), sg.Input(do_not_clear=CLEAR, key='author')],
          [sg.Text('Artist ', size=SIZE), sg.Input(do_not_clear=CLEAR, key='artist')],
          [sg.Text('Description ', size=SIZE), sg.Multiline(do_not_clear=CLEAR, key='description')],
          [sg.Text('Genre ', size=SIZE), sg.Input(do_not_clear=CLEAR, key='genre')],
          [sg.Text('Status ', size=SIZE), sg.Listbox(size=(15,5), values = status_values, key='status')],
          [sg.Text('Status:'), sg.Text(size=(30,1), key='-OUTPUT-'),
                 sg.Button('Generate'), sg.HorizontalSeparator(pad=(13,1)),  sg.Button('Exit')]]

window = sg.Window('Tachiyomi \'details.json\' Generator', layout, keep_on_top=True )

while True:  # Event Loop
    event, values = window.read()
    # print(event, values)
    # ## Main Program ##
    details = open('details.json','w')
    result = '{\n'
    for x in ["title", "author", "artist", "description", "genre"]:
        if values[x] is None:
            result += skipInput(x)
        else:
            result += getInput(x, values[x])
    result += getInput('status', values['status'][0])
    
    result += '"_status values": ["0 = Unknown", "1 = Ongoing", "2 = Completed", "3 = Licensed"]\n}'
    details.write(result)
    details.close()
    print('details.json ' + '  GENERATED!\n')
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Generate':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['title']+'  DONE!')

window.close()

if __name__ == '__main__':
    main()