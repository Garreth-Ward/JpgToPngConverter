import os

from PIL import Image


def convert_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Iterate through each file in the input folder
    for file_name in files:
        # Create the full path for the input file
        input_path = os.path.join(input_folder, file_name)

        # Check if the file is an image (you can customize this condition if needed)
        if file_name.lower().endswith(( '.jpg', '.jpeg', '.gif')):
            # Open the image
            with Image.open(input_path) as img:
                # Create the full path for the output file within the PyCharm project
                output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.png')

                # Convert and save the image as PNG
                img.save(output_path, format='PNG')
                print(f"Converted: {file_name} -> {os.path.basename(output_path)}")


if __name__ == "__main__":
    # Set your input folder relative to the PyCharm project directory
    input_folder = input("Enter the path to the input folder: ")

    # Enter input folder location in cmd
    # input_folder = sys.argv[1]

    # Set your output folder relative to the PyCharm project directory
    output_folder = input("Enter the path to the output folder: ")

    # Enter Output Folder in cmd
    # output_folder = sys.argv[2]

    convert_images(input_folder, output_folder)
