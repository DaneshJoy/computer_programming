import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageEnhance
import os


class ImageProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")
        self.root.geometry("1000x700")

        # Variables
        self.image_path = tk.StringVar()
        self.brightness_var = tk.DoubleVar(value=1.0)
        self.contrast_var = tk.DoubleVar(value=1.0)
        self.color_var = tk.DoubleVar(value=1.0)

        # Image variables
        self.original_image = None
        self.processed_image = None
        self.display_size = (300, 300)

        self.setup_ui()

        # Bind slider events
        self.brightness_var.trace("w", self.process_image)
        self.contrast_var.trace("w", self.process_image)
        self.color_var.trace("w", self.process_image)

    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=BOTH, expand=True)

        # File selection frame
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=X, pady=(0, 20))

        ttk.Label(file_frame, text="Image File:").pack(side=LEFT, padx=(0, 10))

        file_entry = ttk.Entry(file_frame, textvariable=self.image_path, state=READONLY)
        file_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

        browse_btn = ttk.Button(file_frame, text="Browse", command=self.browse_file)
        browse_btn.pack(side=RIGHT)

        # Controls frame
        controls_frame = ttk.LabelFrame(
            main_frame, text="Image Adjustments", padding=15
        )
        controls_frame.pack(fill=X, pady=(0, 20))

        # Brightness slider
        brightness_frame = ttk.Frame(controls_frame)
        brightness_frame.pack(fill=X, pady=(0, 10))

        ttk.Label(brightness_frame, text="Brightness:", width=12).pack(side=LEFT)
        brightness_scale = ttk.Scale(
            brightness_frame,
            from_=0.1,
            to=2.0,
            orient=HORIZONTAL,
            variable=self.brightness_var,
        )
        brightness_scale.pack(side=LEFT, fill=X, expand=True, padx=(10, 10))

        brightness_label = ttk.Label(brightness_frame, text="1.0", width=6)
        brightness_label.pack(side=RIGHT)

        # Update brightness label
        def update_brightness_label(*args):
            brightness_label.config(text=f"{self.brightness_var.get():.2f}")

        self.brightness_var.trace("w", update_brightness_label)

        # Contrast slider
        contrast_frame = ttk.Frame(controls_frame)
        contrast_frame.pack(fill=X, pady=(0, 10))

        ttk.Label(contrast_frame, text="Contrast:", width=12).pack(side=LEFT)
        contrast_scale = ttk.Scale(
            contrast_frame,
            from_=0.1,
            to=2.0,
            orient=HORIZONTAL,
            variable=self.contrast_var,
        )
        contrast_scale.pack(side=LEFT, fill=X, expand=True, padx=(10, 10))

        contrast_label = ttk.Label(contrast_frame, text="1.0", width=6)
        contrast_label.pack(side=RIGHT)

        # Update contrast label
        def update_contrast_label(*args):
            contrast_label.config(text=f"{self.contrast_var.get():.2f}")

        self.contrast_var.trace("w", update_contrast_label)

        # Color slider
        color_frame = ttk.Frame(controls_frame)
        color_frame.pack(fill=X)

        ttk.Label(color_frame, text="Color:", width=12).pack(side=LEFT)
        color_scale = ttk.Scale(
            color_frame, from_=0.0, to=2.0, orient=HORIZONTAL, variable=self.color_var
        )
        color_scale.pack(side=LEFT, fill=X, expand=True, padx=(10, 10))

        color_label = ttk.Label(color_frame, text="1.0", width=6)
        color_label.pack(side=RIGHT)

        # Update color label
        def update_color_label(*args):
            color_label.config(text=f"{self.color_var.get():.2f}")

        self.color_var.trace("w", update_color_label)

        # Reset button
        reset_btn = ttk.Button(
            controls_frame, text="Reset", command=self.reset_values, style=OUTLINE
        )
        reset_btn.pack(pady=(15, 0))

        # Images frame
        images_frame = ttk.Frame(main_frame)
        images_frame.pack(fill=BOTH, expand=True)

        # Original image frame
        original_frame = ttk.LabelFrame(images_frame, text="Original Image")
        original_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

        self.original_label = ttk.Label(
            original_frame, text="No image loaded", anchor=CENTER
        )
        self.original_label.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Processed image frame
        processed_frame = ttk.LabelFrame(images_frame, text="Processed Image")
        processed_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=(10, 0))

        self.processed_label = ttk.Label(
            processed_frame, text="No image loaded", anchor=CENTER
        )
        self.processed_label.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def browse_file(self):
        """Open file dialog to select an image"""
        file_types = [
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff"),
            ("All files", "*.*"),
        ]

        filename = filedialog.askopenfilename(
            title="Select an image file", filetypes=file_types
        )

        if filename:
            self.image_path.set(filename)
            self.load_image(filename)

    def load_image(self, path):
        """Load and display the original image"""
        try:
            self.original_image = Image.open(path)

            # Display original image
            self.display_original_image()

            # Process and display the image with current settings
            self.process_image()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")

    def display_original_image(self):
        """Display the original image in the left panel"""
        if self.original_image:
            # Resize image to fit display area while maintaining aspect ratio
            img_copy = self.original_image.copy()
            img_copy.thumbnail(self.display_size, Image.Resampling.LANCZOS)

            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(img_copy)

            # Update label
            self.original_label.config(image=photo, text="")
            self.original_label.image = photo  # Keep a reference

    def process_image(self, *args):
        """Apply brightness, contrast, and color adjustments in sequence"""
        if not self.original_image:
            return

        try:
            # Start with original image
            img = self.original_image.copy()

            # Apply brightness first
            if self.brightness_var.get() != 1.0:
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(self.brightness_var.get())

            # Apply contrast to the brightness-adjusted image
            if self.contrast_var.get() != 1.0:
                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(self.contrast_var.get())

            # Apply color to the contrast-adjusted image
            if self.color_var.get() != 1.0:
                enhancer = ImageEnhance.Color(img)
                img = enhancer.enhance(self.color_var.get())

            self.processed_image = img

            # Display processed image
            self.display_processed_image()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image: {str(e)}")

    def display_processed_image(self):
        """Display the processed image in the right panel"""
        if self.processed_image:
            # Resize image to fit display area while maintaining aspect ratio
            img_copy = self.processed_image.copy()
            img_copy.thumbnail(self.display_size, Image.Resampling.LANCZOS)

            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(img_copy)

            # Update label
            self.processed_label.config(image=photo, text="")
            self.processed_label.image = photo  # Keep a reference

    def reset_values(self):
        """Reset all sliders to default values"""
        self.brightness_var.set(1.0)
        self.contrast_var.set(1.0)
        self.color_var.set(1.0)


if __name__ == "__main__":
    # Create the main window with ttkbootstrap theme
    # Available themes: https://ttkbootstrap.readthedocs.io/en/latest/themes/
    # Example themes: darkly, flatly, litera, cyborg, solar, etc.
    root = ttk.Window(themename="darkly")

    # Create the application
    app = ImageProcessor(root)

    # Start the application
    root.mainloop()
