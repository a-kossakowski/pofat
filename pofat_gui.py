import tkinter as tk
from tkinter import filedialog, Label, Entry, Button, ttk
from threading import Thread
from image_processor import resize_image  # handles image resizing
from panel_generator import generate_panel  # creates a panel from images
from PIL import Image

class ImagePanelCreator(tk.Tk):  # main application class
    
    def __init__(self):
        super().__init__()
        self.title('Panel of Figures Assembly Tool (PoFAT)')  # window title
        self.geometry('800x600')  # window size

        # initialize data structures
        self.images = {}  # original images
        self.resized_images = {}  # resized images
        self.label_positions = ["Top Left", "Top Right", "Bottom Left", "Bottom Right"]  # label position options
        self.selected_label_position = tk.StringVar(value=self.label_positions[2])  # default label position
        self.create_widgets()  # create UI widgets

    def create_widgets(self):
        # create UI components
        Button(self, text="Upload Figures", command=self.upload_action, font=('Arial', 17)).pack(pady=10)
        self.grid_entry = self.create_label_entry("Grid Layout (e.g., 2x2):")
        self.figure_size_entry = self.create_label_entry("Optional - Figures Resize (px; e.g., 1920x1080):", optional=True)
        Button(self, text="Resize Figures", command=self.resize_figures, font=('Arial', 17)).pack(pady=10)
        self.h_space_entry = self.create_label_entry("Horizontal Space (px):")
        self.v_space_entry = self.create_label_entry("Vertical Space (px):")
        self.h_margin_entry = self.create_label_entry("Horizontal Margin (px):")
        self.v_margin_entry = self.create_label_entry("Vertical Margin (px):")
        self.create_label_position_dropdown()  # dropdown for label positions
        Button(self, text="Generate Panel", command=self.generate_panel, font=('Arial', 17)).pack(pady=10)

    def create_label_entry(self, text, optional=False):
        # create a label with an entry field
        Label(self, text=text, font=('Arial', 17)).pack()
        entry = Entry(self, font=('Arial', 17))
        entry.pack()
        if optional:
            entry.insert(0, 'No Adjustements')  # default text for optional fields
        return entry

    def create_label_position_dropdown(self):
        # create a dropdown for selecting label position
        Label(self, text="Label Position:", font=('Arial', 17)).pack()
        dropdown = ttk.Combobox(self, values=self.label_positions, textvariable=self.selected_label_position, font=('Arial', 17))
        dropdown.pack()

    def upload_action(self):
        # file upload dialog
        filenames = filedialog.askopenfilenames(title="Select Figures", filetypes=[("Image files", "*.jpg *.jpeg *.png", ".svg", ".gif")])
        for i, filename in enumerate(filenames, start=1):
            self.images[chr(64+i)] = filename  # map images to alphabet labels
        print(f"{len(filenames)} files loaded.")

    def resize_figures(self):
        # resize images based on user input
        size_str = self.figure_size_entry.get()
        if 'x' in size_str and size_str.lower() != 'No Adjustements':
            Thread(target=self.process_resize, args=(size_str,)).start()  # start resize in a thread
        else:
            self.resized_images = self.images.copy()  # skip resizing
            print("Resize skipped.")

    def process_resize(self, size_str):
        # resize processing
        width, height = map(int, size_str.split('x'))
        for label, image_path in self.images.items():
            resized_img = resize_image(image_path, width, height)
            self.resized_images[label] = resized_img  # store resized image
            print(f"{label} resized.")

    def generate_panel(self):
        # start panel generation in a thread
        Thread(target=self.process_generate_panel).start()

    def process_generate_panel(self):
        # panel generation processing
        h_space = int(self.h_space_entry.get())
        v_space = int(self.v_space_entry.get())
        h_margin = int(self.h_margin_entry.get())
        v_margin = int(self.v_margin_entry.get())
        grid_layout = self.grid_entry.get()

        image_paths = list(self.resized_images.values()) if self.resized_images else list(self.images.values())
        images_list = [Image.open(path) for path in image_paths]  # open images

        label_pos = self.selected_label_position.get()
        if images_list:
            panel = generate_panel(images_list, grid_layout, h_space, v_space, h_margin, v_margin, label_pos)
            panel.save("panel.png")  # save generated panel
            print("Panel generated and saved as './panel.png'.")
        else:
            print("No images to arrange.")


if __name__ == "__main__":
    app = ImagePanelCreator()
    app.mainloop()  # start the application

