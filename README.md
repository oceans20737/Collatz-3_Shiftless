# **Shiftless Collatz-3 Model**  
Hiroshi Harada — May 2, 2026

## **Overview**
This repository contains a collection of Python scripts for simulating and visualizing the **Shiftless 3-adic Collatz (Collatz-3)** model. This is an information-preserving model that eliminates the "information loss caused by right shifts" inherent in the standard 3-adic Collatz map.

The Shiftless model aims to visualize the following:

- **The geometric structure of carry avalanches**  
- **The interference moiré between Term A (pure expansion) and Term B (complement injection)**  
- **Fractal structures (gaskets) unique to 3-adic spaces**

---

## **Contents**

### **Documents**
- **TITLE_EN** (English title page for the research report)  
- **REPORT_JP / REPORT_EN**  
  Research reports detailing the theoretical background, the linear decomposition of the Shiftless Collatz-3 trajectory, and in-depth explanations for each Figure.

---

## **Source Code**
Executing each script will automatically generate the corresponding Figure (PNG format).

---

### **`code_01.py`**  
Verifies equivalence with the standard 3-adic Collatz model.  
Extracts the **non‑multiple‑of‑3 part (u<sub>k</sub>)** of the trajectory to demonstrate perfect alignment with the standard model.  
Outputs: `figure1.png`, `figure1.csv`

---

### **`code_02.py`**  
Visualizes the **compact trajectory** of the Shiftless Collatz-3 model.  
Captures the **intense carry avalanches** triggered by NZT=2.  
Output: `figure2.png`

---

### **`code_03.py`**  
Visualizes the **full trajectory** by decomposing a single step of the Shiftless model into two distinct phases:  
- **Reach (Left shift + self-superposition in ternary notation)**  
- **Fill (Local distortion via NZT injection)**  

Output: `figure3.png`

---

### **`code_04.py`**  
A time-synchronized comparison of three distinct dynamics:

- **Pure Expansion: 4n**
- **Fixed Addition: 4n + 1**
- **Shiftless: 4n + c<sub>k</sub> * 3<sup>v<sub>k</sub></sup>**

Visualizes the structural differences side-by-side.  
Output: `figure4.png`

---

### **`code_05.py`**  
Performs a perfect linear decomposition of the trajectory into the following components to visualize their **spatial interference (moiré)**:  

- **Term A (Pure Expansion)**  
- **Term B (Complement Interference)**  

Output: `figure5.png`

---

## **Requirements**
- Python 3.x  
- NumPy  
- Matplotlib  

---

## **Usage**
Run each script from your terminal or command prompt:
```bash
python code_01.py
python code_02.py
python code_03.py
python code_04.py
python code_05.py
```

---

## **License**
- Research Document: CC BY 4.0  
- Python Source Code: MIT License  
- © 2026 Hiroshi Harada

---

