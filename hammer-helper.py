import subprocess
import getpass

def run_hammer_command_locally(command):
    try:
        # Run the command using subprocess
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful (exit code 0)
        if result.returncode == 0:
            print("Command execution successful.")
            print("Output:")
            print(result.stdout)
        else:
            print("Error: Command execution failed.")
            print("Error Output:")
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", e)

def run_hammer_command_remotely(command):
    try:
        # Run the command remotely using subprocess
        # Modify this part according to your remote execution mechanism
        print(f"Running command remotely: {command}")
    except Exception as e:
        print("An error occurred:", e)

def add_satellite_user():
    # Prompt the user for user details
    new_username = input("Enter username for the new user: ")
    new_password = getpass.getpass("Enter password for the new user: ")
    new_email = input("Enter email address for the new user: ")
    new_firstname = input("Enter first name for the new user: ")
    new_lastname = input("Enter last name for the new user: ")
    auth_source = input("Enter authentication source for the new user: ")

    # Construct the hammer command to add a user
    command = f"hammer user create --login {new_username} --password {new_password} --mail {new_email} --firstname '{new_firstname}' --lastname '{new_lastname}' --auth-source '{auth_source}'"
    
    # Run the command using subprocess
    run_hammer_command_locally(command)

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Run Hammer commands locally")
        print("2. Run Hammer commands remotely")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            run_hammer_locally_menu()
        elif choice == "2":
            run_hammer_remotely_menu()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def run_hammer_locally_menu():
    # Define available hammer commands in label-command format
    hammer_commands = [
        {"label": "List Organizations", "command": "hammer list-organizations"},
        {"label": "List Hosts", "command": "hammer list-hosts"},
        {"label": "Create Satellite User", "command": "create_user"}  # Option to create a new user
        # Add more commands as needed
    ]

    print("\nAvailable Hammer Commands (Locally):")
    for index, cmd in enumerate(hammer_commands, start=1):
        print(f"{index}. {cmd['label']}")

    command_choice = input("Enter the number of the command you want to execute (or 'b' to go back): ")
    if command_choice == "b":
        return
    try:
        command_choice = int(command_choice)
        if 1 <= command_choice <= len(hammer_commands):
            selected_command = hammer_commands[command_choice - 1]

            if selected_command["label"] == "Create Satellite User":
                add_satellite_user()
            else:
                run_hammer_command_locally(selected_command["command"])
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid choice. Please enter a number.")

def run_hammer_remotely_menu():
    # Define available remote hammer commands
    remote_hammer_commands = [
        {"label": "List Organizations", "command": "hammer list-organizations"},
        {"label": "List Hosts", "command": "hammer list-hosts"},
        # Add more commands as needed
    ]

    print("\nAvailable Hammer Commands (Remotely):")
    for index, cmd in enumerate(remote_hammer_commands, start=1):
        print(f"{index}. {cmd['label']}")

    command_choice = input("Enter the number of the command you want to execute remotely (or 'b' to go back): ")
    if command_choice == "b":
        return
    try:
        command_choice = int(command_choice)
        if 1 <= command_choice <= len(remote_hammer_commands):
            selected_command = remote_hammer_commands[command_choice - 1]
            run_hammer_command_remotely(selected_command["command"])
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid choice. Please enter a number.")

if __name__ == "__main__":
    main_menu()
