import os
import json
from tkinter import Tk, filedialog, simpledialog

def main():
    root = Tk()
    root.withdraw()  # we don't want a full GUI, so keep the root window from appearing

    # Ask the user to select a folder
    folder_path = filedialog.askdirectory(title='Select Folder Containing Files')

    # Input for number of process steps and their names
    num_process_steps = simpledialog.askinteger("Input", "Number of process steps:", parent=root, minvalue=1)
    process_steps = []
    for i in range(num_process_steps):
        step_name = simpledialog.askstring("Input", f"Name of process step {i+1}:", parent=root)
        process_steps.append(step_name)

    # Input for number of manufacturing features and their names
    num_features = simpledialog.askinteger("Input", "Number of manufacturing features:", parent=root, minvalue=1)
    manufacturing_features = []
    for i in range(num_features):
        feature_name = simpledialog.askstring("Input", f"Name of manufacturing feature {i+1}:", parent=root)
        manufacturing_features.append(feature_name)

    # Process each file in the directory
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            base_name, _ = os.path.splitext(filename)
            new_filename = os.path.join(folder_path, base_name + ".json")
            data = {
                'process_steps': process_steps,
                'manufacturing_features': manufacturing_features
            }

            # Write the JSON data to a file
            with open(new_filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
    
    print("JSON files created successfully.")

if __name__ == "__main__":
    main()
