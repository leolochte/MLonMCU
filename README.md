# Machine Learning on Microcontrollers @ ETH Zurich

This repository contains a comprehensive collection of hands-on exercises for learning machine learning deployment on microcontrollers and edge devices. The course progresses from basic embedded programming to advanced ML optimization techniques.

## Repository Structure

Each exercise (`ex1`–`ex8`) contains:
- **`task/`** - Exercise materials, starter code, and instructions
- **`solution/`** - Reference solutions and implementation guides

## Exercises Overview

### Exercise 1: Introduction to Embedded Systems
- **Focus**: Environment setup, basic microcontroller programming and GPIO operations
- **Files**: Basic blinky LED example and setup

### Exercise 2: Good Practices for Training ML models  
- **Focus**: Introduction to ML model training along with digital signal processing and audio analysis fundamentals.
- **Files**: Audio processing with MLonMCU framework, Jupyter notebook tutorials

### Exercise 3: Machine Learning Pipelines
- **Focus**: End-to-end ML workflow implementation
- **Files**: Multiple Jupyter notebooks covering data preprocessing, training, and evaluation

### Exercise 4: Real-time Audio Analysis
- **Focus**: FFT profiling and real-time signal processing
- **Files**: ADF implementation, FFT profiling tools, audio playback utilities

### Exercise 5: MFCC Feature Extraction
- **Focus**: Mel-frequency cepstral coefficients for audio ML
- **Files**: MFCC training notebooks, TensorFlow Lite model conversion, STM32 deployment

### Exercise 6: Model Optimization and Quantization
- **Focus**: Neural network compression techniques
- **Files**: Fashion-MNIST models with various optimization strategies (pruning, quantization, QAT)

### Exercise 7: Knowledge Distillation
- **Focus**: Model compression through teacher-student learning
- **Files**: Knowledge distillation implementation, live inference demo, STM32 deployment packages

### Exercise 8: Computer Vision on Edge
- **Focus**: CNN deployment for image classification
- **Files**: Camera integration, AI8X framework, meme classification models

## Getting Started

1. **Prerequisites**: 
   - Docker
   - STM32 development environment
   - Python 3.8+ with TensorFlow/PyTorch
   - Jupyter Notebook

2. **Setup**:
   ```bash
   git clone <repository-url>
   cd MLonMCU/dockerfiles
   # Please follow the README.md file in MLonMCU/dockerfiles
   # Install requirements for each exercise as needed
   ```

3. **Working with Exercises**:
   - Start with the PDF instructions in each `task/` directory
   - Follow the progressive difficulty from ex1 to ex8
   - Reference solutions are available in each `solution/` directory

## Learning Objectives

By completing these exercises, you will learn:
- Embedded systems programming for ML applications
- Audio signal processing and feature extraction
- Neural network optimization for resource-constrained devices
- Model quantization and compression techniques
- Real-time inference on microcontrollers
- Computer vision pipeline deployment

## Notes

Exercises and solutions are continuously updated based on feedback and improvements.
Feel free to open issues if you find any bugs or inconsistencies!

## Contributing

We welcome contributions to this project! If you would like to contribute, follow these steps:

1. **Fork the Repository**: Start by forking this repository to your GitHub account.

2. **Create a Feature Branch**: Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```
3. **Make Your Changes**: Implement your feature or bug fix.
4. **Build and Test**: Build the project and ensure that your changes work as expected.
5. **Commit and Push**: Commit your changes with a descriptive message and push them to your fork:
   ```bash
   git commit -m "Add feature XYZ"
   git push origin feature-name
   ```
6. **Create a Pull Request**: Navigate to your fork on GitHub and create a pull request to the main repository.

Please ensure your pull request adheres to the following guidelines:

1. Clearly describe the changes and their purpose.
2. Include any relevant documentation or tests.
