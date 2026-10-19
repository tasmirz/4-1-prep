# CSE Academic Study Hub (4th Year 1st Term)

A unified study repository and examination intelligence platform for KUET Computer Science & Engineering.

🌐 **Live Website / GitHub Pages Portal:** [https://tasmirz.github.io/4-1-prep/](https://tasmirz.github.io/4-1-prep/)

---

## 🚀 One-Click Browser Launchers

Launch the Central Portal directly in your browser with any of the following options:

1. **Instant Python Launcher** (Offline File Mode):
   ```bash
   python3 /extra/Study/launch.py
   # Or directly from the study root:
   python3 launch.py
   ```
2. **Local HTTP Server Mode** (Serves on port 8000+):
   ```bash
   python3 launch.py --server
   # Custom port:
   python3 launch.py --server -p 8080
   ```
3. **Local Wi-Fi Network Access** (Study on your Phone or Tablet!):
   ```bash
   python3 launch.py --network
   # Binds to 0.0.0.0 and prints your local LAN IP (e.g., http://192.168.1.X:8000/index.html)
   ```
4. **Desktop GUI Clickable Shortcut**:
   - Double-click **`KUET Study Portal`** directly on your desktop: [`~/Desktop/KUET_Study_Portal.desktop`](file:///home/user/Desktop/KUET_Study_Portal.desktop).
5. **System CLI Command** (From any directory in terminal):
   ```bash
   study-portal
   # Or with server:
   study-portal --server
   ```

---

## 📚 Merged Textbook PDFs (Inside `final/` Folder)

All 10 merged textbook slide books are organized cleanly inside [`final/`](file:///extra/Study/final/):

| Subject & Course Code | Merged PDF Book | Pages | Key Coverage Highlights |
| :--- | :--- | :---: | :--- |
| **Machine Learning** (CSE 4111) | [`final/ml-akhand-sir.pdf`](file:///extra/Study/final/ml-akhand-sir.pdf) | 347 | Neurons, Perceptron, Backpropagation Calculus & Momentum, K-Means & RBF Networks, Negative Correlation Learning (NCL), Decision Trees (ID3/C4.5/CART), Ensembles (Random Forests/RSM), CNNs. |
| **Machine Learning** (CSE 4111) | [`final/ml-rocky-sir.pdf`](file:///extra/Study/final/ml-rocky-sir.pdf) | 181 | Nature-inspired optimization: Genetic Algorithms (GA), Particle Swarm Optimization (PSO), Ant Colony (ACO), Artificial Bee Colony (ABC). |
| **Computer Networks** (CSE 3201) | [`final/networks-sakhawat-sir.pdf`](file:///extra/Study/final/networks-sakhawat-sir.pdf) | 713 | Network layer architecture, IPv4/IPv6, Subnetting/CIDR, Routing algorithms (Dijkstra, Bellman-Ford, BGP/OSPF), Link layer & CSMA/CD, Wireless & Mobile IP. |
| **Computer Networks** (CSE 3201) | [`final/networks-sadi-sir.pdf`](file:///extra/Study/final/networks-sadi-sir.pdf) | 290 | Application layer protocols (HTTP, DNS, SMTP), Transport layer (UDP vs TCP), Reliable Data Transfer (rdt 1.0–3.0, GBN, SR), TCP Congestion Control. |
| **Computer Security** (CSE 4109) | [`final/security-dola-mam.pdf`](file:///extra/Study/final/security-dola-mam.pdf) | 305 | Software security, Buffer overflows, Memory corruption, Web attacks (SQLi, XSS, CSRF), Firewalls, Intrusion Detection Systems (IDS), Access control models. |
| **Computer Security** (CSE 4109) | [`final/security-rokib-sir.pdf`](file:///extra/Study/final/security-rokib-sir.pdf) | 193 | Applied cryptography, Classical ciphers, DES/AES, Number theory (Euclid, Fermat, Euler), RSA, Diffie-Hellman, Digital signatures (DSA), Hash functions (SHA). |
| **NLP** (CSE 4241) | [`final/nlp-shawon-sir.pdf`](file:///extra/Study/final/nlp-shawon-sir.pdf) | 521 | Deep learning for NLP, Word2Vec, GloVe, RNNs, LSTMs, GRUs, Seq2Seq, Attention mechanisms, Transformer architecture, BERT & LLMs. |
| **NLP** (CSE 4241) | [`final/nlp-azhar-sir.pdf`](file:///extra/Study/final/nlp-azhar-sir.pdf) | 329 | Statistical NLP foundations, Regular expressions, Morphology, N-gram language models, POS tagging, Hidden Markov Models (HMMs), Viterbi decoding, Syntax parsing. |
| **Computer Graphics** (CSE 4107) | [`final/graphics.pdf`](file:///extra/Study/final/graphics.pdf) | 664 | Raster displays, Bresenham & Midpoint algorithms, 2D/3D transformations, Projection matrices (Orthographic vs Perspective), Cohen-Sutherland, Lighting & Shading (Gouraud, Phong), Ray tracing, Z-buffer. |
| **Image Processing** (CSE 4125) | [`final/image-processing-masudul-ahsan.pdf`](file:///extra/Study/final/image-processing-masudul-ahsan.pdf) | 653 | Sampling & quantization, Point processing, Histogram equalization, Spatial filtering (Gaussian, Laplacian, Sobel), Frequency domain DFT/FFT, Image restoration & Wiener filtering, Otsu segmentation. |

---

## 🗺️ Master Mind Map & Question Browser (Bidirectional Integration)

The repository provides a deep, two-way integration between conceptual knowledge graphs and actual university exam archives:

### 1. Unified Master Mind Map & Hub Home
- [`index.html`](file:///extra/Study/index.html) and [`master_study_mindmap.html`](file:///extra/Study/master_study_mindmap.html):
  - A zero-dependency, graph-paper radial mind map synthesizing all 10 courses.
  - Features real-time pan & zoom, collapsible branches, and search match cycling.
  - **Embedded University Exam Intelligence:** Every node displays historical exam recurrence frequency, total marks, sample university exam questions, and a direct button to launch the Question Browser.
  - **URL Parameter Search & Deep-Linking:** Open `master_study_mindmap.html?search=Backpropagation` or `?search=CSE 4111` to automatically auto-search, expand ancestors, center the node, and open the slide-out details drawer.

### 2. Intelligent Exam Question Analyzers (With Full OCR Search Engine)
Located in [`question-browser/`](file:///extra/Study/question-browser/):
- **Machine Learning**: [`machine-learning-akhand-sir-rocky-sir.html`](file:///extra/Study/question-browser/machine-learning-akhand-sir-rocky-sir.html) (Alias: `machine-learning.html`) · 241 Qs · 1,729 Marks · 264 Scans
- **Computer Networks**: [`computer-networks-sakhawat-sir-sadi-sir.html`](file:///extra/Study/question-browser/computer-networks-sakhawat-sir-sadi-sir.html) (Alias: `computer-networks.html`) · 274 Qs · 2,457 Marks · 299 Scans
- **Computer Security**: [`computer-and-network-security-dola-mam-rokib-sir.html`](file:///extra/Study/question-browser/computer-and-network-security-dola-mam-rokib-sir.html) (Alias: `computer-and-network-security.html`) · 338 Qs · 2,867 Marks · 358 Scans
- **NLP**: [`natural-language-processing-shawon-sir-azhar-sir.html`](file:///extra/Study/question-browser/natural-language-processing-shawon-sir-azhar-sir.html) (Alias: `natural-language-processing.html`) · 196 Qs · 1,791 Marks · 211 Scans
- **Computer Graphics**: [`computer-graphics-masudul-sir.html`](file:///extra/Study/question-browser/computer-graphics-masudul-sir.html) (Alias: `computer-graphics.html`) · 255 Qs · 2,474 Marks · 282 Scans
- **Image Processing**: [`image-processing-masudul-ahsan-sir.html`](file:///extra/Study/question-browser/image-processing-masudul-ahsan-sir.html) (Alias: `image-processing-and-computer-vision.html`) · 213 Qs · 2,029 Marks · 238 Scans

**Core Capabilities**:
- **🔍 Multi-Term OCR Search Engine**:
  - **Typo & Spacing Tolerance**: Automatically expands concatenated terms (e.g., `backpropagation` ➔ `back propagation`, `kmeans` ➔ `k means`, `decisiontree` ➔ `decision tree`).
  - **Live Multi-Term Token Matching**: Type any sequence of terms (e.g., `perceptron backpropagation derivation`) and the engine matches all occurrences regardless of word order or punctuation.
  - **Keyword Highlight (`<mark>`)**: Dynamically highlights matching keywords in vibrant yellow inside questions and OCR text.
  - **Dynamic Year-by-Year Archive Filtering**: Keystrokes filter the Raw Exam Archive (`#rawCompact`), showing exactly how many subquestions match per academic year.
  - **One-Click OCR Copy**: Dedicated "📋 Copy OCR" buttons on every exam question card with instant visual feedback badge.
- **6 Comprehensive Analysis Tabs**: `Overview`, `Topics & Priorities`, `Questions & Clusters`, `Teaching Material Alignment`, `Faculty Expectations`, `Extracted JSON`.
- **📷 View Original Scan**: Click on any question to hydrate and inspect the original printed university paper scan crop.
- **🗺️ Mind Map Deep Integration**: Direct buttons on every header, topic card, and question cluster to jump into the Mind Map centered on that concept.
- **Persistent Study Tracker**: Check off topics (`Mastered` / `Needs Revision`) with live progress saved in `localStorage`.

---

## 📂 Reorganized Clean Directory Structure

```
/extra/Study/
├── final/                                             # Merged Master Textbook Slide Books
│   ├── ml-akhand-sir.pdf                              # Merged textbook PDF (Section A)
│   ├── ml-rocky-sir.pdf                               # Merged textbook PDF (Section B)
│   ├── networks-sakhawat-sir.pdf                      # Merged textbook PDF (Section A)
│   ├── networks-sadi-sir.pdf                          # Merged textbook PDF (Section B)
│   ├── security-dola-mam.pdf                          # Merged textbook PDF (Section B)
│   ├── security-rokib-sir.pdf                         # Merged textbook PDF (Section A)
│   ├── nlp-shawon-sir.pdf                             # Merged textbook PDF (Section A)
│   ├── nlp-azhar-sir.pdf                              # Merged textbook PDF (Section B)
│   ├── graphics.pdf                                   # Merged textbook PDF
│   └── image-processing-masudul-ahsan.pdf             # Merged textbook PDF
│
├── index.html                                         # Academic Study Hub Central Portal
├── launch.py                                          # One-Click Browser Launcher (Direct & HTTP Server)
├── master_study_mindmap.html                          # Unified Master Knowledge Graph (All 10 Courses)
├── README.md                                          # This reference guide
│
├── question-browser/                                  # Modern OCR-Searchable 6-Tab Exam Analyzers
│   ├── machine-learning-akhand-sir-rocky-sir.html
│   ├── computer-networks-sakhawat-sir-sadi-sir.html
│   ├── computer-and-network-security-dola-mam-rokib-sir.html
│   ├── natural-language-processing-shawon-sir-azhar-sir.html
│   ├── computer-graphics-masudul-sir.html
│   └── image-processing-masudul-ahsan-sir.html
│   (Canonical alias files also retained for backwards compatibility)
│
├── mindmaps/                                          # Standalone Radial Mind Maps for Each Faculty Module
│   ├── graphics_masudul_sir_mindmap.html
│   ├── image_processing_masudul_ahsan_sir_mindmap.html
│   ├── ml_akhand_sir_mindmap.html
│   ├── ml_rocky_sir_mindmap.html
│   ├── networks_sadi_sir_mindmap.html
│   ├── networks_sakhawat_sir_mindmap.html
│   ├── nlp_azhar_sir_mindmap.html
│   ├── nlp_shawon_sir_mindmap.html
│   ├── security_dola_mam_mindmap.html
│   └── security_rokib_sir_mindmap.html
│   (Mirrored legacy files retained for backwards compatibility)
│
├── slides/                                            # Clean 2-Level Source Slides & Notes
│   ├── Graphics/
│   ├── Image/
│   ├── ML-Akhand-Sir/
│   │   ├── pdf/                                       # 14 Clean sequential lecture PDFs
│   │   ├── pptx/                                      # 11 Clean lecture PPTXs
│   │   └── Reference/                                 # Foundations, Papers, Supplementary
│   ├── ML-Rocky-Sir/
│   ├── Networks-Sadi-Sir/
│   ├── Networks-Sakhawat-Sir/
│   ├── NLP-Azhar-Sir/
│   ├── NLP-Shawon-Sir/
│   ├── Security-Dola-Mam/
│   └── Security-Rokib-Sir/
│
├── artifacts/                                         # Centralized Data Artifacts & Knowledge Trees
│   ├── mindmap_knowledge_tree.json
│   ├── exam_intelligence_manifest.json
│   └── census_report.json
│
└── scripts/                                           # Maintenance & Generation Tooling
    ├── generate_all_exam_analyzers.py                 # Question Browser generator & OCR search builder
    ├── merge.py                                       # PDF compilation and merging engine
    └── mindmap_builders/                              # Radial mind map generator scripts
```
