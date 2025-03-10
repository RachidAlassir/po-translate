import os
import shutil
from subprocess import run, PIPE

# Set up the paths for the test files
test_folder = os.path.join(os.getcwd(), 'tests_files')
original_file_path = os.path.join(test_folder, 'po_translate.pot')  # Original file path
test_file_path = os.path.join(test_folder, 'ar.po')  # Test file path


# Function to restore the original file after testing
def restore_file():
    # Check if the test file exists and restore it
    if os.path.exists(test_file_path):
        # Copy the original file back
        shutil.copy(original_file_path, test_file_path)
        print(f"File restored to {test_file_path}")
    else:
        print(f"{test_file_path} does not exist. Cannot restore.")


# Test case to run the translation script on the sample PO file
def test_po_translate_with_sample_file():
    # Ensure correct path to the PO file
    po_file = os.path.join(test_folder, 'ar.po')

    # Print message before running the command
    print(f"Running command on {po_file}")

    # Run the translation command with depth set to 2
    result = run(['python', '../po_translate/cli.py', po_file, '--depth', '2'], stdout=PIPE, stderr=PIPE)

    # Check the result of the command execution
    if result.returncode == 0:
        print(f"Command executed successfully:\n{result.stdout.decode('utf-8')}")
    else:
        print(f"Command failed with error:\n{result.stderr.decode('utf-8')}")

    # After testing, restore the original file
    restore_file()


if __name__ == "__main__":
    test_po_translate_with_sample_file()
