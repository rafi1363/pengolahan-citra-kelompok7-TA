import tkinter as tk
from tkinter import filedialog, Text, Label
from PIL import Image, ImageTk
import pytesseract

# Pastikan lokasi tesseract diatur (ubah path sesuai sistem Anda)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Desktop App")

        # Label dan tombol untuk memuat gambar
        self.label = Label(root, text="Load an image to perform OCR", font=("Arial", 16))
        self.label.pack(pady=10)

        self.button_load = tk.Button(root, text="Load Image", command=self.load_image)
        self.button_load.pack(pady=5)

        # Area untuk menampilkan gambar
        self.canvas = tk.Canvas(root, width=400, height=300, bg="lightgrey")
        self.canvas.pack(pady=10)

        # Tombol untuk OCR
        self.button_ocr = tk.Button(root, text="Perform OCR", command=self.perform_ocr, state=tk.DISABLED)
        self.button_ocr.pack(pady=5)

        # Area teks untuk hasil OCR
        self.text_area = Text(root, height=10, width=50)
        self.text_area.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)
            self.button_ocr.config(state=tk.NORMAL)

    def display_image(self, image):
        # Resize image to fit canvas
        img_resized = image.resize((400, 300))
        img_tk = ImageTk.PhotoImage(img_resized)
        self.canvas.image = img_tk
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

    def perform_ocr(self):
        if hasattr(self, 'image'):
            text = pytesseract.image_to_string(self.image)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, text)

# Main aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
