🩻 X-Ray Crack Detection — A Visual Interface for Fracture Insight
Unveiling the silent fissures within industrial materials or skeletal structures demands more than mere visual inspection. This application harmonizes computer vision algorithms with an intuitive graphical interface to discern and illustrate cracks from X-ray images with precision and artistry.

🧠 Foreword
In a world teeming with structural complexities, identifying hairline fractures or material defects through X-rays is akin to deciphering secrets whispered in grayscale. This repository bestows a finely woven Python utility, fusing OpenCV, NumPy, and Tkinter, that exhales life into raw X-ray imagery and pinpoints structural breaches using sophisticated morphological operations and contour analysis.

🔧 Requisites for Incantation
Before casting spells on images, ensure your environment houses the following libraries:
pip install opencv-python numpy matplotlib pillow
All other ingredients (i.e., tkinter) come pre-consecrated with standard Python installations.

🖼️ Functionality Unfurled
This tool is a subtle ballet of logic and lens, orchestrating the following symphony:

Grayscale Conversion — Drowns the image in monochrome for sharper abstraction.

CLAHE Enhancement — Breathes contrast into the grayscale void for deeper clarity.

Gaussian Blurring — Mutes noise that whispers false positives.

Canny Edge Detection — Etches the boundaries of truth using algorithmic ink.

Morphological Closing — Seals stray lines into unified cracks.

Contour Weaving — Outlines every suspect crevice using iterative scrutiny.

Shape Filtering — Employs aspect ratio and arc length metrics to discard the mundane.

Arrow Annotation — Marks the most menacing fracture with a visual cue for human eyes.

🎛️ User Interface Elegance
No terminal incantations necessary. The GUI—courtesy of Tkinter—summons interaction via:
A Title inscribed with gravitas
A Button that opens a chasm to your local storage for image upload
Seamless visualization through Matplotlib, rendering:
Raw input
Processed edges
All visible contours

Final annotated masterpiece
🧪 Demonstrative Echoes
Here’s a glimpse of what unfolds post-processing:

The original X-ray stands untouched.

Edges reveal sharp mysteries.

Contours whisper the geometry of flaws.

The overlay illuminates the chief fracture—painted with hues of consequence.
