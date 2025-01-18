# Alarm Clock/Timer

This Python project implements a simple alarm clock/timer that counts down from a specified duration and plays a sound when the timer ends.

## Features
- Countdown timer with minute and second display.
- Alarm sound playback when the timer ends.
- Interactive user input for specifying the countdown duration.

## Requirements
- Python 3.x
- `playsound3` module (for playing sound files)

## Installation
1. Clone this repository or download the source code.
2. Ensure you have Python installed on your system.
3. Install the required `playsound3` module using the following command:
   ```bash
   pip install playsound3
   ```
4. Place a sound file named `sound.wav` in the same directory as the script. This will be the alarm sound played when the timer ends.

## Usage
1. Run the script using Python:
   ```bash
   python alarm_clock.py
   ```
2. Enter the countdown duration in minutes and seconds when prompted.
3. The timer will count down, displaying the time left in the format `MM:SS`.
4. When the timer reaches zero, the specified sound (`sound.wav`) will play.

## Code Explanation
### Imports
- `playsound` is used to play the alarm sound when the timer ends.
- `time` is used to handle the countdown logic and introduce delays.

### Constants
- `CLEAR` and `CLEAR_AND_RETURN` are ANSI escape codes for clearing the console and positioning the cursor at the top.

### Functions
#### `alarm(seconds)`
- Takes the total countdown duration in seconds as input.
- Counts down and displays the remaining time in minutes and seconds.
- Plays the alarm sound when the countdown ends.

#### `main()`
- Prompts the user to enter the countdown duration in minutes and seconds.
- Converts the entered time into seconds and starts the timer using the `alarm()` function.

## Example
```plaintext
Enter the number of minutes: 0
Enter the number of seconds: 10
The time left before the alarm goes on is: 00:10
The time left before the alarm goes on is: 00:09
...
*Sound plays when timer ends*
```

## Notes
- Ensure that the `sound.wav` file is present in the same directory as the script and is playable.
- You can replace `sound.wav` with any other sound file, but you must rename it to `sound.wav` or update the code accordingly.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

Happy coding!
