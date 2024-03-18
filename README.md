# Panel of Figures Assembly Tool (PoFAT)

PoFAT is a Python-based GUI application designed to assist in the creation of image panels from individual figures. It allows users to upload multiple images, optionally resize them, and then generate a single panel image with customizable configurations such as grid layout, spacing, and margins. Label positions can also be specified for each figure in the panel.

## Features

- **Figure Upload**: Load multiple image files for panel creation.
- **Figure Resize**: Optionally resize figures to a specified dimension before assembly.
- **Custom Grid Layout**: Configure the layout of the image panel (e.g., 2x2, 3x3).
- **Adjustable Margins and Spacing**: Set horizontal and vertical spacing between images, as well as margins.
- **Label Positioning**: Choose the position of labels on each figure in the panel.
- **Panel Generation**: Generate and save the final image panel with the configured settings.

## Prerequisites

To run PoFAT, you need to have Python installed on your system along with the following libraries:
- Tkinter (for the GUI)
- PIL (Python Imaging Library, for image processing)

## Installation

1. Ensure you have Python installed on your system.
2. Install PIL if you haven't already: `pip install Pillow`
3. Clone this repository or download the scripts to a local directory.

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

## Modules

- `pofat_gui.py`: The main GUI application script.
- `panel_generator.py`: Contains functions for generating the panel and resizing images.
- `image_processor.py`: Helper module, contains the `resize_image` function used by `pofat_gui.py`.

## Contributing

Feel free to fork the repository and submit pull requests to contribute to the development of PoFAT.

## License

Open-source.

