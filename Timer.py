from playsound import playsound
import time
import sys

def countdown_timer(seconds):
    try:
        while seconds>=0:
            mins,secs= divmod(seconds,60)
            timer_display= f"{mins:02d}:{secs:02d}"
            print(timer_display,end='\r')

            time.sleep(1)
            seconds -=1

        print("\n⏰ Time's up! ⏰")

    except KeyboardInterrupt:
        print("\n || Countdown interrupted!")


def get_user_time():
    while True:
        try:
            user_input= input("Enter time (e.g., '2m' for 2 minutes or '30s' for 30 seconds): ").strip().lower()
            if user_input.endswith('m'):
                return int(user_input[:-1]) * 60  # Convert minutes to seconds
            elif user_input.endswith('s'):
                return int(user_input[:-1])
            else:
                print("⚠️ Invalid format! Use 'Xm' for minutes or 'Ys' for seconds.")

        except ValueError:
            print("⚠️ Please enter a valid number followed by 'm' or 's'.")

def alert_user():
    print("\n⏰ Time's up! ⏰")
    try:
        for _ in range(1):
            #print("\a",end='')
            playsound("alarm.mp3")
            time.sleep(0.5)
    except:
        pass

if __name__ == "__main__":
    print("===== ⏳ Countdown Timer ⏳ =====")
    user_seconds= get_user_time()
    countdown_timer(user_seconds)
    alert_user()