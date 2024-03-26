# 100DaysofCode-Disappearing-Text-App
Day 90 of the 100 Days of Code course. The goal for the day was to create a Tkinter application that has text disappear when the countdown hits zero.

For my spin on the application, I used the colors from the Pomodoro timer app (Day 28) from earlier in the course as a starting point for this project.

When the application is launched, the default value for the countdown timer is set to 5 seconds. This can be toggled between five and ten seconds depending on how long you want the inactive timer to run. Once the application detects that a keystroke is entered, the countdown timer begins to run and if a keystroke is detected, the timer is reset to the value that is specified (5 or 10 seconds). Additionally, while the application is running the buttons used to set the countdown starting point are disabled preventing the countdown timer from being interrupted by these buttons. 

Once the timer hits zero seconds, the text inside of the textbox disappears, and text can no longer be entered. The reset button can be pressed while the timer is running or once the timer hits zero seconds. Once the app is reset, the buttons to set the starting countdown time are re-enabled allowing that value to be toggled. Additionally, after the app is reset, the text box allows you to start entering text again, and repeat the functionality of the application.
