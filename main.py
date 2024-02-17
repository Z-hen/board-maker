from queue import PriorityQueue
from Board import Board
import PySimpleGUI as sg

sg.theme('DarkAmber')
menuLayout = [[sg.Text("What would you like to do?")],
              [sg.Button("Check-In Players")],  # Tick off players already in the system
              [sg.Button("Register New Player")]]  # Add them to text file of players

checkInLayout = [[sg.Text("Player Check Ins")]]

# Create a (list) layout of layouts
layout = [[sg.Column(menuLayout, visible=True, key='menu'),
           sg.Column(checkInLayout, visible=False, key='check in')]]

window = sg.Window("Badminton Board Maker", layout, size=(500, 500))


def readPlayerFile():
    # Read and process players.txt
    playerFile = open('players.txt', 'r')
    content = playerFile.readline()
    print(content)


if __name__ == '__main__':
    # Create the Window using the main menu layout

    while True:
        event, values = window.read()
        print(event, values)

        if event in (None, 'Exit'):
            break
        if event == 'Check-In Players':
            # Change menu layout to invis and set check in layout to visible
            window['menu'].update(visible=False)
            layout = menuLayout
            window['check in'].update(visible=True)

            # Process actions here

    window.close()
