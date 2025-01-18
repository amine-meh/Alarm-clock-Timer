from playsound3 import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
  time_passed = 0
  print(CLEAR)
  while time_passed < seconds:
    time.sleep(1)
    time_passed += 1

    time_left = seconds - time_passed
    minutes_left = time_left // 60
    seconds_left = time_left % 60
    print(f"{CLEAR_AND_RETURN}The time left before the alarm goes on is: {minutes_left:02d}:{seconds_left:02d}")
  playsound("sound.wav")

def main():
  minutes = int(input("Enter the number of minutes: "))
  seconds = int(input("Enter the number of seconds: "))
  total_seconds = minutes * 60 + seconds
  alarm(total_seconds)

main()