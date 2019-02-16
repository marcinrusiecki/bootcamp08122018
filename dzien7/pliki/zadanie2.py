

file_name = "logs.txt"


def rozwiazanie():
    user_total_time_login = {}
    user_total_time_logout = {}

    with open(file_name) as f:

        for line in f:
            user, action, time_str = line.split(";")
            time = int(time_str)
            if action == 'LOGIN':
                user_total_time_login[user] = user_total_time_login.get(user, 0) + time
            elif action == "LOGOUT":
                user_total_time_logout[user] = user_total_time_logout.get(user, 0) + time

    final_result = {}
    for user in user_total_time_login:
        final_result[user] = user_total_time_logout[user] - user_total_time_login[user]

    return final_result





print("Czas przebywania w systemie: ")
for user, time in rozwiazanie().items():
    print(f' - {user}: {time} s')



import sys

if len(sys.argv) != 3:
    print("Podałeś złą liczbę argumentów")
    exit()

_, file_in, file_out = sys.argv

print(file_in)

with open(file_in) as f:
    unique_emails = set()
    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            unique_emails.add(line)

emails = sorted(unique_emails)

with open(file_out, "w") as f:
    for email in emails:
        f.write(email + "\n")
    # lub:
    # out = "\n".join(emails)
    # f.write(out)