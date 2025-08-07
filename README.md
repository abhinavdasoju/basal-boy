# Basal Pro by Abhinav Dasoju
Made for Bayless Lab in Summer 2025

This project was designed to use OpenCV algorithms to take pixel measurements of the cilia on a Tetrahymena cell.

## Dependencies

Make sure you have the following installed:

- **Python**  
  
- **OpenCV** (essential for image recognition)

### Step 1: Install Python:
1. Download Python [here](https://www.python.org/downloads/)

2. Follow the steps on the installer
   - On **Windows**, make sure to check the box that says: “Add Python to PATH”

3. Check if Python is properly installed:
   - Open the **Command Prompt** (Windows) or **Terminal** (Mac)
   - Type this and press Enter:
     ```bash
     python3 --version
     ```
   - You should see something like "Python 3.13.4"

### Step 2: Install OpenCV

OpenCV is a library that lets Python work with images and videos.

1. Open your **Command Prompt** (Windows) or **Terminal** (Mac)

2. Type this command and press Enter:
    ```bash
    pip install opencv-python
    ```

3. If no errors occur, you're good to go!

## Usage

To run this program, you WILL need your Terminal. Simply enter this command:
```bash
python3 [path to main.py]
```
To get the path, simply navigate to main.py in your file explorer and copy the file into your clipboard. Paste this path into your terminal window after typing in "python3"

Also, you can quickly access any previous commands you entered just by clicking the up arrow key when in your terminal. Please do this when repeatedly running this code, it will make your life a lot easier.

## Image Preprocessing
Image preprocessing is crucial for the code to work.

Ensure that these requirements are met:
- All images are converted to PNG
- Image being used is named as "source.png" and is in the "sources" folder

If the microscope image is a .tiff file, follow these instructions:
1. In Finder, select the file and do **Right click > Quick Actions > Convert Image**
2. Convert the image to PNG and save

### Creating individual cell images
The algorithm is designed to run on images of individual Tetrahymena cells. 

To do this:
1. Create a copy of the original microscope image by doing **Right click > Duplicate**
2. Rename the copied image to "sources.png"
3. Double click the image to open it in Preview, and then select a region with a single cell
4. To crop the region, click the markdown icon (shown as a pen) and then click the crop icon
5. Do Cmd + S to save the image and then close Preview

Note: You can also change the accepted filename by editing the code parameters

## Analyzing results
After running the code on your inputted image, you will have a window showing your edited image, and the image saved in the "results" folder. I suggest opening up the saved image in Preview to zoom in and have a better look.

Each line between 2 nodes (basal bodies) will have an accompanying number. This is the distance in micrometers. The line and the number will be the same font color.

## Editing the code
You will have to edit the code in order to tweak certain settings (filename, conversion factors, etc). For this, you will need some sort of text editor.
