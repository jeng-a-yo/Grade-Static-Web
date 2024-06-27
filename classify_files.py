from timer import timing_decorator
import os
import shutil

# The directory containing all the PDF files
source_dir = "all_files"

# List of subjects and their corresponding directories
subjects = ["國文", "英文", "數學", "自然", "社會"]
subjects_map = {
    ("國文", "國語", "國綜", "國寫", "chinese", "01-96"): subjects[0],
    ("英文", "english", "03-96"): subjects[1],
    ("數學", "math", "02-96", "數a", "數b"): subjects[2],
    ("自然", "nature", "05-96"): subjects[3],
    ("社會", "society", "04-96"): subjects[4]
}
subject_dirs = {subject: os.path.join(source_dir, subject) for subject in subjects}

# Create directories for each subject if they don't exist
for subject, directory in subject_dirs.items():
    if not os.path.exists(directory):
        os.makedirs(directory)

@timing_decorator  # Apply the decorator to time the function
def classify_files():
    # Move files to their corresponding subject directories
    for filename in os.listdir(source_dir):
        if filename.endswith('.pdf'):
            moved = False
            for keywords, subject in subjects_map.items():
                if any(keyword in filename for keyword in keywords):
                    source_file = os.path.join(source_dir, filename)
                    destination_file = os.path.join(subject_dirs[subject], filename)
                    shutil.move(source_file, destination_file)
                    print(f"Moved {filename} to {subject} folder")
                    moved = True
                    break
            if not moved:
                print(f"Could not classify {filename}, no matching keyword found.")

# Start classifying files
classify_files()

print("All files have been categorized successfully.")
