# FastParse-CLI 🚀

![C++17](https://img.shields.io/badge/C%2B%2B-17-blue.svg?style=flat&logo=c%2B%2B)
![Visual Studio 2022](https://img.shields.io/badge/Visual_Studio-2022-purple.svg?style=flat&logo=visual-studio)
![Multithreading](https://img.shields.io/badge/Architecture-Multithreaded-success.svg)

A high-performance command-line tool built in pure **ISO C++17** designed to scan massive directories, process files concurrently, and extract keyword metrics in milliseconds. No bloated frameworks, just raw execution speed.

## ⚡ Core Architecture

- **Language Standard:** Strict ISO C++17 compliance.
- **Concurrency Model:** Utilizes `std::async` and `std::future` for parallel file processing and dynamic workload distribution across available CPU cores.
- **Thread Safety:** Implemented strict lock acquisition using `std::lock_guard` and `std::mutex` to prevent data races during global state mutation (RAII compliance).
- **I/O Optimization:** Leveraged `std::filesystem` for fast directory traversal and `std::string_view` to eliminate unnecessary memory allocations and maximize disk read speeds.

## 🚀 Performance Showcase

Processing multiple files and extracting thousands of keyword occurrences in **~1.7 seconds**:

[ARRASTE_E_SOLTE_SUA_IMAGEM_AQUI]

## 🛠️ Build Instructions

1. Clone the repository:
   ```bash
   git clone [https://github.com/blackgamer_07/FastParse-CLI.git](https://github.com/blackgamer_07/FastParse-CLI.git)<img width="980" height="509" alt="7783eb0a-b6e9-4264-a3e8-8ff2d11faa81" src="https://github.com/user-attachments/assets/3590db46-e2b0-46f6-a187-5a835acbecba" />
