# pip install pillow

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

class ImageAdjusterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Adjustment (Brightness → Contrast → Color)")

        self.image_path = tk.StringVar()

        # Input and browse in one row
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5, fill=tk.X, padx=10)
        
        self.path_entry = tk.Entry(input_frame, textvariable=self.image_path)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        browse_btn = tk.Button(input_frame, text="Browse", command=self.browse_image)
        browse_btn.pack(side=tk.RIGHT, padx=5)

        # Sliders
        self.slider_frame = tk.Frame(root)
        self.slider_frame.pack()

        self.brightness_slider = self.create_slider("Brightness", 1.0, self.update_image)
        self.contrast_slider = self.create_slider("Contrast", 1.0, self.update_image)
        self.color_slider = self.create_slider("Color (Saturation)", 1.0, self.update_image)

        # Image display
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack()

        self.original_label = tk.Label(self.canvas_frame)
        self.original_label.grid(row=0, column=0, padx=10)

        self.processed_label = tk.Label(self.canvas_frame)
        self.processed_label.grid(row=0, column=1, padx=10)

        # Image storage
        self.original_image = None
        self.tk_original = None
        self.tk_processed = None

    def create_slider(self, label, initial, command):
        frame = tk.Frame(self.slider_frame)
        frame.pack()
        slider = tk.Scale(frame, from_=0.1, to=2.0, resolution=0.1,
                          orient=tk.HORIZONTAL, label=label, command=command, length=400)
        slider.set(initial)
        slider.pack()
        return slider

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
        if file_path:
            self.image_path.set(file_path)
            self.load_image(file_path)

    def load_image(self, path):
        self.original_image = Image.open(path).convert("RGB")
        self.display_images()

    def update_image(self, _=None):
        if not self.original_image:
            return

        # Step 1: Brightness
        brightness = self.brightness_slider.get()
        contrast = self.contrast_slider.get()
        color = self.color_slider.get()

        image = ImageEnhance.Brightness(self.original_image).enhance(brightness)
        image = ImageEnhance.Contrast(image).enhance(contrast)
        image = ImageEnhance.Color(image).enhance(color)

        # Resize for display
        resized_original = self.original_image.resize((250, 250))
        resized_processed = image.resize((250, 250))

        self.tk_original = ImageTk.PhotoImage(resized_original)
        self.tk_processed = ImageTk.PhotoImage(resized_processed)

        self.original_label.config(image=self.tk_original)
        self.processed_label.config(image=self.tk_processed)

    def display_images(self):
        self.update_image()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageAdjusterApp(root)
    root.mainloop()
