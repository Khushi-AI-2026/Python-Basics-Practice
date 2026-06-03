# ===========================
# PROBLEM 3: External Module Usage
# ===========================
# समस्या: एक बाहरी module install करो और उसे use करो
# Problem: Install an external module and use it

# Step 1: पहले colorama module को install करो
# Run this command in terminal: pip install colorama
# colorama एक module है जो terminal में रंगीन text print करता है

print("\n" + "="*50)
print("PROBLEM 3: USING EXTERNAL MODULE (colorama)")
print("="*50 + "\n")

# Step 2: Module को import करो
from colorama import Fore, Back, Style, init

# colorama को initialize करो (खासकर Windows पर)
init(autoreset=True)

# Step 3: colorama का use करके colorful text print करो
print(Fore.RED + "यह red रंग का text है (This is red colored text)")
print(Fore.GREEN + "यह green रंग का text है (This is green colored text)")
print(Fore.BLUE + "यह blue रंग का text है (This is blue colored text)")
print(Fore.YELLOW + "यह yellow रंग का text है (This is yellow colored text)")

# Background color भी लगा सकते हैं
print(Back.CYAN + Fore.BLACK + "Black text on Cyan background")

# Style भी add कर सकते हैं
print(Style.BRIGHT + Fore.MAGENTA + "यह bright magenta text है (Bright magenta text)")

print("\n✓ Problem 3 Complete!\n")


# ===========================
# PROBLEM 4: Print Directory Contents
# ===========================
# समस्या: किसी directory के सभी files और folders को print करो
# Problem: Print all files and folders in a directory

print("="*50)
print("PROBLEM 4: PRINT DIRECTORY CONTENTS (Using os module)")
print("="*50 + "\n")

# Step 1: os module को import करो
import os

# Step 2: Directory का path decide करो
# अपने project का path दो या किसी और folder का path दे सकते हो
directory_path = "."  # "." मतलब current directory (जहां यह file है)

# अगर किसी specific folder को देखना है तो:
# directory_path = "C:/Users/YourName/Documents"  # Windows
# directory_path = "/home/username/Documents"      # Linux/Mac

# Step 3: os.listdir() use करके सभी files और folders को list में store करो
contents = os.listdir(directory_path)

# Step 4: सभी contents को print करो
print(f"Directory '{directory_path}' में निम्नलिखित files/folders हैं:\n")
print(f"Total items: {len(contents)}\n")

# सभी items को एक-एक करके print करो
for item in contents:
    print(f"  • {item}")

print("\n✓ Problem 4 Complete!\n")


# ===========================
# PROBLEM 5: Labeled Program 4 With Comments
# ===========================
# समस्या: Problem 4 को detailed comments के साथ लिखो
# Problem: Write Problem 4 with detailed comments

print("="*50)
print("PROBLEM 5: LABELED PROGRAM 4 WITH COMMENTS")
print("="*50 + "\n")

# -------- शुरुआत (START) --------

# Module को import करो - यह Python की built-in library है
import os

# Directory का path दो जिसे देखना है
# "." = current directory (यह file जहां है)
directory_to_list = "."

# Check करो कि directory exist करती है या नहीं
if os.path.exists(directory_to_list):
    # अगर directory exist करती है तो आगे बढ़ो
    
    # os.listdir() function से directory के सभी contents (files + folders) को get करो
    # यह एक list return करता है
    all_items = os.listdir(directory_to_list)
    
    # List को sort करो ताकि alphabetically order में दिखे
    all_items.sort()
    
    # Directory का नाम print करो
    print(f"Directory: {directory_to_list}")
    
    # Total items की count print करो
    print(f"Total items: {len(all_items)}\n")
    
    # "Files and Folders:" header print करो
    print("Files and Folders:")
    print("-" * 40)
    
    # Loop चलाओ - हर item को एक-एक करके process करो
    for index, item in enumerate(all_items, 1):
        # अगर यह एक folder है तो "/" लगा दो, नहीं तो सिर्फ नाम print करो
        if os.path.isdir(os.path.join(directory_to_list, item)):
            item_type = "[FOLDER]"
        else:
            item_type = "[FILE]"
        
        # Index के साथ item को print करो
        print(f"{index}. {item_type} {item}")
    
    print("-" * 40)
    
else:
    # अगर directory exist नहीं करती तो error message print करो
    print(f"Error: Directory '{directory_to_list}' exist नहीं करती!")

print("\n✓ Problem 5 Complete!\n")

print("\n" + "="*50)
print("सभी Problems Complete! (All Problems Complete!)")
print("="*50 + "\n")
