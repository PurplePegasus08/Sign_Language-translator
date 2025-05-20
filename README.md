ASL Sign Language Recognition (In Progress)

This project is focused on building a real-time **ASL (American Sign Language) hand sign recognition system**. It is currently under active development.


🔧 Technologies Used

- Python  
- PyTorch  
- OpenCV  
- MediaPipe  
- ResNet18 (Pretrained CNN Architecture)  
- Matplotlib, NumPy, etc.  


🧠 Model

We use a **pretrained ResNet18 CNN model** as the base architecture. It has been fine-tuned on a custom ASL dataset containing images of hand signs representing alphabets and gestures like **"space"** and **"nothing"**.

The model is trained to classify hand gestures in real time using webcam input, with **MediaPipe** used for hand detection and isolation.

🗂️ Dataset

- Custom ASL dataset with **28 classes** (A–Z, space, and nothing)  
- Images are resized and preprocessed using techniques like **Gaussian Blur** and **CLAHE**  
- **Data augmentation** is optionally applied to reduce overfitting and improve generalization  


🔄 Features (Under Development)

- ✅ Real-time hand sign detection from webcam  
- ✅ Live prediction using fine-tuned **ResNet18**  
- ⏳ Prediction history to form complete words  
- ⏳ Special gesture to confirm or end word prediction
- ⏳ Working on reducing overfitting 
- 
