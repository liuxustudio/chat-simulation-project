from typing import Annotated
import autogen
import sys, os
from datetime import datetime
import agent_utils

import sys
import subprocess
import agents as Agents
cache = autogen.Cache.redis(redis_url="redis://localhost:6379/0")


import subprocess
import os
from datetime import datetime

start_timestamp = datetime.now()

def git_commit(repo_path, push=False):
    # Format the current date and time as "Run YYYY-MM-DD HH:MM:SS Day"
    commit_message = start_timestamp.strftime("Run %Y-%m-%d %H:%M:%S %A")
    
    # Change the current working directory to the repository path if provided
    if repo_path:
        os.chdir(repo_path)
        
    # Stage all changes
    subprocess.run(["git", "add", "."], check=True)
    
    # Commit the changes with the timestamped message
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    
    # Push the commit to the remote repository, if requested
    if push:
        subprocess.run(["git", "push"], check=True)

# Example usage
repo_path = './'  # Use your repository's path
push_commit = False  # Set to False if you don't want to push immediately

try:
    git_commit(repo_path, push_commit)
    print("Commit successful!")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")

class FileAndConsoleStdout:
    def __init__(self, filename:str):
        self.terminal = sys.stdout
        # Generate filename based on current date and time
        self.filename = filename or datetime.now().strftime("./runs/%d.%m.%y_%H.%M.txt")
        self.log = open(self.filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        try:
            self.log.write(message)
        except ValueError:
            pass

    def flush(self):  # Needed for Python 3 compatibility
        if not self.log.closed:
            self.log.flush()
        else:
            print("Log file is closed. Could not flush.")
        
    def close(self):
        self.log.close()
        
    def give_filename(self):
        return self.filename

class FileAndConsoleStdin:
    def __init__(self, filename:str):
        self.terminal = sys.stdin
        # Reuse the filename for stdin to match stdout
        self.filename = filename or datetime.now().strftime("./runs/%d.%m.%y_%H.%M.txt")
        self.log = open(self.filename, "a", encoding="utf-8")

    def readline(self):
        line = self.terminal.readline()
        self.log.write(line)
        return line

    def flush(self):  # Needed for Python 3 compatibility
        if not self.log.closed:
            self.log.flush()
        else:
            print("Log file is closed. Could not flush.")
        
    def close(self):
        self.log.close()


# Override stdout and stdin
start_timestamp_str = start_timestamp.strftime("%d.%m.%y_%H.%M.%S")

full_path = os.path.join(os.getcwd(), 'runs', start_timestamp_str)
print(full_path)
try:
    os.makedirs(full_path, exist_ok=True)
    print(f"Folder '{full_path}' created successfully.")
    
    sys.stdout = FileAndConsoleStdout(filename= os.path.join(full_path, 'log_') + start_timestamp_str + ".txt")
    sys.stdin = FileAndConsoleStdin(filename= os.path.join(full_path, 'log_') + start_timestamp_str + ".txt")
except OSError as error:
    print(f"Failed to create folder '{full_path}'. Error: {error}")
    

try:  
    def get_git_commits():
        try:
            # Führt den Git-Befehl aus, um die letzten Commits auszulesen (hier als Beispiel die letzten 5 Commits)
            commit = subprocess.check_output(['git', 'log', '--pretty=format:%H - %s', '-n', '1'], universal_newlines=True)
            print("Actual Git Commit:")
            print(commit)
        except subprocess.CalledProcessError as e:
            print("Ein Fehler ist aufgetreten beim Auslesen der Git Commits")
            print(e)

    get_git_commits()


    Agents.salesman_agent.initiate_chat(
        Agents.customer_agent,
        message="Hello, Anna. How can I support you? ",
        cache=cache)
    
    
finally:
    assistant_list = [Agents.salesman_agent, Agents.customer_agent]
    total_usage_summary, actual_usage_summary = agent_utils.gather_usage_summary(assistant_list)
    
    print("\n\nTotal usage summary:\n")
    print(total_usage_summary)
    print("\n\nActual usage summary:\n\n")
    print(actual_usage_summary)
    
    print(f"Elapsed Time:{datetime.now() - start_timestamp}\n")
    
    
    try:
        cache.close()
    except:
        print("could not close cache!")
    
    
    try:
        sys.stdout.close()
        #sys.stdin.close()
    except:
        print("could not close channel!")
    
    
