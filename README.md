# 📡 Compressed Sensing  

This repository explores **Compressed Sensing (CS)**, a signal processing technique that enables efficient data acquisition and reconstruction by leveraging signal sparsity. The project demonstrates the **mathematical foundations, reconstruction algorithms, and applications of compressed sensing** in signal and image processing.  

---

## 📌 **Project Overview**  
Compressed sensing is a technique that allows signals to be sampled **below the Nyquist rate** while still enabling accurate reconstruction. It has significant applications in **medical imaging (MRI), wireless communications, and machine learning**. This project covers:  

- **Theoretical Background** of Compressed Sensing.  
- **Signal Acquisition**: Sampling below the Nyquist rate.  
- **Reconstruction Algorithms**:  
  - Basis Pursuit (ℓ1 minimization).  
  - Orthogonal Matching Pursuit (OMP).  
  - Iterative Hard Thresholding (IHT).  
- **Applications** in real-world signal and image processing.  

---

## ✅ **Key Features**  
✔ **Mathematical Formulation**: Explanation of CS using linear algebra.  
✔ **Sparse Representation**: Transforming signals into a sparse domain.  
✔ **Implementation of Recovery Algorithms**: Comparison of **OMP, Basis Pursuit, and IHT**.  
✔ **Performance Analysis**: Error metrics and reconstruction quality.  
✔ **Applications**: Signal denoising, MRI reconstruction, and image compression.  

---

## 🛠 **Installation & Setup**  
1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/vinay2201/Compressed_Sensing.git
cd Compressed_Sensing
```

2️⃣ **Install Dependencies**
```bash
pip install numpy scipy matplotlib scikit-learn cvxpy

```

3️⃣ **Run the Code**
To test the reconstruction algorithms:
```bash
python compressed_sensing.py
```

## 📊 **How Compressed Sensing Works**
The core principle is that a signal x can be recovered from fewer samples y = Φx, where:

Φ is a sensing matrix that captures fewer measurements.
The signal is sparse in some domain (e.g., wavelet or Fourier).
Recovery is done by solving an ℓ1 minimization problem using convex optimization.

## 🚀 **Applications**
🔹 Medical Imaging (MRI scans) 📟 - Reduces scan times.
🔹 Wireless Communications 📡 - Efficient signal transmission.
🔹 Machine Learning 🧠 - Feature selection and dimensionality reduction.
🔹 Image & Audio Compression 🎵 - Reducing storage and bandwidth.
