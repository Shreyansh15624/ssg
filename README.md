# Statis Site Generator: Markdown-to-HTML Compiler

## Description

A lightweight, high-performance static site generator built entirely from scratch in standard Python. This engine bypasses bloated external libraries, featuring a custom lexer, a recursive file-system crawler, and an in-memory Document Object Model (DOM) to compile raw Markdown into a deployable static site.

The project is structured into distinct layers separating the source content, the compilation engine, and the deployment artifacts:
* `content/`: Source Markdown files (mirrored in output)
* `static/`: Raw CSS and image assets
* `docs/`: Compiled HTML build artifacts
* `src/`: Core Python compiler engine (AST generation, multi-pass parsing, and DFS filesystem traversal)

## Motivation

This tool was architected to demonstrate a deep understanding of parsing algorithms, data structures, and zero-dependency environment execution. By building the lexer, AST, and recursive filesystem crawler entirely from scratch, it serves as a comprehensive showcase of clean backend architecture and core Python capabilities.

## Quick Start

The project utilizes bash scripts to automate the build and test pipelines, ensuring a frictionless setup.

**1. Clone the repository:**
```bash
git clone https://github.com/shreyansh15624/ssg.git
cd ssg
```

**2. Execute the Build Pipeline:**
```bash
./build.sh
```

**3. Run the Automated Test Suite:**
```bash
./test.sh
```

**4. Serve the Local Build:**
```bash
./main.sh
```
*Navigate to `http://localhost:8888`*

## Usage

To use this compiler for your own static site:
1. Place your raw Markdown files into the `content/` directory.
2. Place any required CSS, images, or static assets into the `static/` directory.
3. Modify `template.html` to adjust the base HTML injection template.
4. Run `./build.sh` to compile the site. 

The compilation engine will output directly to the `docs/` folder, generating artifacts ready for static hosting environments. The project natively supports the **GitHub Pages** deployment workflow directly from the `main` branch.

## Contributing

Contributions are welcome! If you'd like to improve the compiler or add new features:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Please ensure all new features pass the existing test suite by running `./test.sh` before submitting a PR.
