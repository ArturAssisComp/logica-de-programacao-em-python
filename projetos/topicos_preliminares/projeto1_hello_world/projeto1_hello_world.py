import re
import argparse
import subprocess
import re

def main(execution_command: str):
    try:
        process = subprocess.run(
            execution_command, shell=True, check=True, capture_output=True, text=True
        )

        if re.search(r"Hello World(\r\n|\n)", process.stdout):
            print("Test passed: 'Hello World' output detected.")
        else:
            print(f"Test failed: 'Hello World' output not found. '{process.stdout}' instead")

    except subprocess.CalledProcessError as e:
        print(f"Test failed: Command execution failed with error: {e.stderr}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test a process for 'Hello World' output.")
    
    parser.add_argument(
        "execution_command", 
        type=str, 
        help="The command to execute the program to test"
    )
    
    args = parser.parse_args()

    main('python ' + args.execution_command)
