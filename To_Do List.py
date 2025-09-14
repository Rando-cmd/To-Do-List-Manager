import PySimpleGUI as sg
import sys

def main():

    def restart():
        restart_choice = sg.popup_yes_no("Would you like to restart?")
        if restart_choice in ("No", sg.WIN_CLOSED):
            sg.popup_no_buttons("See you!", no_titlebar=True, auto_close=True, auto_close_duration=2)
            sys.exit()
        elif(restart_choice == "Yes"):
            sg.popup_no_buttons("Restarting...", no_titlebar=True, auto_close=True, auto_close_duration=2)
            main()
    
    task_manager = [
        [sg.Text("WELCOME TO THE TASK MANAGER!")],
        [sg.Text("Enter a task you you need a reminder for:"), sg.Input(key='-TASK-', enable_events=True)],
        [sg.Text(key='-TASK_LIST-')],
        [sg.Button("Submit", key='-SUBMIT-', disabled=True, bind_return_key=True), sg.Button("Clear Tasks", key='-TASK_COMPLETE-', disabled=True), sg.Button("Exit")]
    ]

    task_window = sg.Window("Task Manager", task_manager, finalize=True)
    task_window['-SUBMIT-'].set_focus()

    task_list = []
    task_key = 0

    while True:
        task_events, values = task_window.read()
        if task_events in ("Exit", sg.WIN_CLOSED):
            task_window.close()
            break

        elif task_events in '-TASK-':
            if values['-TASK-'].strip():
                task_window['-SUBMIT-'].update(disabled=False)
            else:
                task_window['-SUBMIT-'].update(disabled=True)
        
        elif(task_events == '-SUBMIT-'):
            task = values['-TASK-']
            if task:
                task_key += 1
                new_task = f'-TASK_{task_key}-'
                task_list.append(new_task)
                task_item = [[sg.Text(task, key=new_task)]]
                task_window.extend_layout(task_window['-TASK_LIST-'], task_item)
                task_window['-TASK_COMPLETE-'].update(disabled=False)
                task_window['-TASK-'].update('')
                task_window['-SUBMIT-'].update(disabled=True)
        
        elif(task_events == '-TASK_COMPLETE-'):
            for item in task_list:
                task_window[item].update(visible=False)
            task_list = []
            task_window['-TASK_COMPLETE-'].update(disabled=True)
            task_window['-SUBMIT-'].update(disabled=True)

    restart()

main()