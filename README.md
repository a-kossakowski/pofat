## Table of Contents

- [What is PoFAT?](#what-is-pofat)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example of the panel generated using PoFAT](#example-of-the-panel-generated-using-pofat)
- [Modules](#modules)
- [Contributing](#contributing)


# What is PoFAT?

PoFAT is a Python-based GUI application designed to assist in the creation of image panels from individual figures. It allows users to upload multiple images, optionally resize them, and then generate a single panel image with customizable configurations such as grid layout, spacing, and margins. Label positions can also be specified for each figure in the panel.

## Features

- **Figure Upload**: Load multiple image files for panel creation.
- **Figure Resize**: Optionally resize figures to a specified dimension before assembly.
- **Custom Grid Layout**: Configure the layout of the image panel (e.g., 2x2, 3x3).
- **Adjustable Margins and Spacing**: Set horizontal and vertical spacing between images, as well as margins.
- **Label Positioning**: Choose the position of labels on each figure in the panel.
- **Panel Generation**: Generate and save the final image panel with the configured settings.

## Getting Started

Follow these steps to get PoFAT up and running on your system, regardless of whether you're using Linux, Windows, or Mac.

### Step 1: Prerequisites

Ensure Python and pip (Python's package installer) are installed on your system. PoFAT requires Python to run, and pip to install necessary libraries.

- **Linux/Mac**: Python usually comes pre-installed. You can check by running `python --version` or `python3 --version` in your terminal.
- **Windows**: If Python is not installed, download it from [python.org](https://www.python.org/downloads/) and follow the installation instructions. Ensure you select the option to add Python to PATH during installation.

### Step 2: Clone or Download the Repository

- **Option 1: Clone with Git (recommended)**
  - Open a terminal (Linux/Mac) or Git Bash/command prompt (Windows).
  - Navigate to the directory where you want to place the PoFAT project.
  - Clone the repository:
    ```
    git clone https://github.com/a-kossakowski/pofat.git
    ```
  - This command creates a new directory named `pofat` containing the project files.

- **Option 2: Download ZIP**
  - Visit the [PoFAT repository](https://github.com/a-kossakowski/pofat) on GitHub.
  - Click the green **Code** button, then click **Download ZIP**.
  - Extract the ZIP file to your desired location.

### Step 3: Install Required Libraries

- Navigate to the `pofat` directory in your terminal or command prompt.
`cd path/to/pofat`
- Install the required Pillow library using pip:
`pip install Pillow`

### Step 4: Run PoFAT

- Within the `pofat` directory, run the main script:
`python pofat_gui.py`
- This command launches the PoFAT GUI, where you can begin uploading images, configuring your panel, and generating the final image panel.

### Troubleshooting

- If you encounter any issues running `python pofat_gui.py`, ensure your Python version is up to date and compatible with PoFAT. PoFAT is developed for Python 3.x.
- For Windows users, if Python is not recognized as an internal or external command, ensure that Python and pip are correctly added to your system's PATH as part of the installation process.

With these steps, users on Linux, Windows, and Mac should be able to get PoFAT running smoothly on their systems.

## Usage

1. Navigate to the directory containing the `pofat_gui.py` script.
2. Run the script using Python: `python pofat_gui.py`
3. The PoFAT GUI will open. Follow the on-screen instructions to upload images, set configurations, and generate your panel.

### Uploading Figures

Click on the "Upload Figures" button and select the images you want to include in your panel. The images can be in JPG, JPEG, PNG, SVG, or GIF format.

### Configuring the Panel

- Enter the desired grid layout (e.g., 2x2 for a panel with 2 rows and 2 columns).
- Optionally specify a new size for the figures (in pixels, e.g., 1920x1080) if you want them resized.
- Set the horizontal and vertical space between figures, as well as the margins around the entire panel.
- Choose the label position for each figure from the dropdown menu.

### Generating the Panel

Once all configurations are set, click on the "Generate Panel" button to create your image panel. The generated panel will be saved as `panel.png` in the same directory as the script.

#### Example of a Panel Generated Using PoFAT

![Panel of three figures in 2x2 grid layout](./test_imgs/panel.png)

## Modules

- `pofat_gui.py`: The main GUI application script.
- `panel_generator.py`: Contains functions for generating and adjusting the panel.
- `image_processor.py`: Helper module, contains the `resize_image` function used by `pofat_gui.py`.

## Contributing

Feel free to fork the repository and submit pull requests to contribute to the development of PoFAT.

