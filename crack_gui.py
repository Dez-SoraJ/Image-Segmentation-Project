import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# === Main Processing Function ===
def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        messagebox.showerror("Error", "Could not load image. Please select a valid image file.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    blurred = cv2.GaussianBlur(enhanced, (5, 5), 0)
    edges = cv2.Canny(blurred, 30, 100)

    kernel = np.ones((3, 3), np.uint8)
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    segmented = image.copy()
    overlay = image.copy()

    cv2.drawContours(segmented, contours, -1, (0, 255, 0), 1)
    cv2.drawContours(overlay, contours, -1, (0, 255, 0), 1)

    crack_contour = None
    max_crack_area = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 50 < area < 1500:
            x, y, w, h = cv2.boundingRect(cnt)
            aspect_ratio = float(w) / h if h != 0 else 0

            if aspect_ratio < 0.4 or aspect_ratio > 2.5:
                epsilon = 0.01 * cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, epsilon, False)

                if len(approx) >= 4:
                    cv2.polylines(overlay, [approx], False, (0, 0, 255), thickness=2)

                    if area > max_crack_area:
                        max_crack_area = area
                        crack_contour = approx

    if crack_contour is not None:
        x, y, w, h = cv2.boundingRect(crack_contour)
        start_point = (x + w // 2, y + h // 2)
        end_point = (start_point[0], start_point[1] - 30)
        cv2.arrowedLine(overlay, start_point, end_point, (255, 0, 0), 2, tipLength=0.3)

    # Show outputs
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 4, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.title("Edges Detected")
    plt.imshow(edges, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.title("All Contours")
    plt.imshow(cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.title("Segmented Output")
    plt.imshow(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# === GUI Setup ===
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        process_image(file_path)

root = tk.Tk()
root.title("X-Ray Crack Detection")
root.geometry("400x200")
root.configure(bg="#f0f4f7")

header = tk.Label(root, text="X-Ray Crack Detection", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333")
header.pack(pady=20)

upload_btn = tk.Button(root, text="Upload X-Ray Image", font=("Helvetica", 12), command=upload_image, bg="#4caf50", fg="white", padx=20, pady=10)
upload_btn.pack()

root.mainloop()

