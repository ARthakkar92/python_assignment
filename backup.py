import os
import sys
import shutil
from datetime import datetime

def backup_file(source_dir, destination_dir):

    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(destination_dir):
        print(f"Error: Destination directory '{destination_dir}' does not exist.")
        return

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)

        # Skip directories
        if not os.path.isfile(source_file):
            continue

        dest_file = os.path.join(destination_dir, filename)

        # If file exists -> add timestamp
        if os.path.exists(dest_file):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name, extension = os.path.splitext(filename)
            new_filename = f"{name}_{timestamp}{extension}"
            dest_file = os.path.join(destination_dir, new_filename)

        # Copy file
        shutil.copy2(source_file, dest_file)
        print(f"Copied: {filename} → {dest_file}")

    print("\nBackup completed successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source = sys.argv[1]
        destination = sys.argv[2]
        backup_file(source, destination)
