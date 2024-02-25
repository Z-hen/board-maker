from queue import PriorityQueue
from Board import Board
import PySimpleGUI as sg
import json

sg.theme('DarkAmber')
menuLayout = [[sg.Text("What would you like to do?")],
              [sg.Button("Check-In Players")],  # Tick off players already in the system
              [sg.Button("Register New Player")]]  # Add them to text file of players

checkInLayout = [[sg.Text("Player Check Ins")]]

createPlayerLayout = [[sg.Text('Enter new player information')],
                      [sg.Text('First Name', size=(12, 1)), sg.In(k='firstName', size=(10, 1))],
                      [sg.Text('Last Name', size=(12, 1)), sg.In(k='lastName', size=(10, 1))],
                      [sg.Button("Submit Player")]]

# Create a (list) layout of layouts
layout = [[sg.Column(menuLayout, visible=True, key='menu'),
           sg.Column(checkInLayout, visible=False, key='check in'),
           sg.Column(createPlayerLayout, visible=False, key='create player')]]

window = sg.Window("Badminton Board Maker", layout, size=(500, 500))


def createPlayer():
    """
    Use the inforamtion provided to create a player class
    Convert the player information to a json string to put into a json file
    Version 1 information:
        First Name
        Last Name
    :return:
    """
    print("e")


if __name__ == '__main__':
    # Create the Window using the main menu layout

    while True:
        event, values = window.read()
        print(event, values)  # Values is a dict

        if event in (None, 'Exit'):
            break

        # --------------------------------CHECK IN PAGE-------------------------------------------------------
        if event == 'Check-In Players':
            # Change menu layout to invis and set check in layout to visible
            window['menu'].update(visible=False)
            window['check in'].update(visible=True)

        # --------------------------------REGISTER PLAYER PAGE-------------------------------------------------------
        if event == 'Register New Player':
            window['menu'].update(visible=False)
            window['create player'].update(visible=True)

        if event == 'Submit Player':
            # Create a player class
            new Player()

    window.close()
