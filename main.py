from queue import PriorityQueue
from Board import Board
import PySimpleGUI as sg

if __name__ == '__main__':
    # Set up Layout of the window
    sg.theme('DarkAmber')
    layout = [ [sg.Text("Some Text on row 1")],
               [sg.Text('Ooga Booga'), sg.InputText()],
               [sg.Button('OK'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window("Window Title", layout)
    while True:

        # Read player names txt file and pass them into the board
        board = Board()
        # board.test()

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        print("You entered ", values[0])

    window.close()
