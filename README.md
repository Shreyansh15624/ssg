# ⚡ Zero-Dependency Python SSG: Markdown-to-HTML Compiler

A lightweight, high-performance static site generator built entirely from scratch in standard Python. This engine bypasses bloated external libraries, featuring a custom lexer, a recursive file-system crawler, and an in-memory Document Object Model (DOM) to compile raw Markdown into a deployable static site.

## 🏗️ System Architecture & Compiler Design

This tool was architected to demonstrate a deep understanding of parsing algorithms, data structures, and zero-dependency environment execution.

### 1. Lexical Analysis & Custom AST (Abstract Syntax Tree)

* **Node Hierarchy (`src/htmlnode.py`, `src/textnode.py`):** Utilizes a polymorphic class structure to represent elements natively in memory.
* **Multi-Pass Parsing (`src/convex.py`):** The engine separates concerns by first dividing raw markdown into structural blocks, and subsequently executing an inline-level tokenization pass for text formatting.

### 2. Recursive Filesystem Traversal

* **Static Asset Pipeline (`src/copystatic.py`):** Implements a Depth-First Search (DFS) algorithm to crawl the `static/` directory and propagate CSS/images into the compiled build.
* **Content Generation (`src/getcontent.py`):** Mirrors the exact source tree of the `content/` directory into the final build output in `docs/`, dynamically injecting generated HTML into `template.html`.

## 📂 Repository Structure

The project is structured into distinct layers separating the source content, the compilation engine, and the deployment artifacts.

```text
├── content/            # Source Markdown files (mirrored in output)
├── static/             # Raw CSS and image assets
├── docs/               # Compiled HTML build artifacts (GitHub Pages target)
├── src/                # Core Python compiler engine
│   ├── main.py         # Entry point & execution arguments
│   ├── htmlnode.py     # DOM tree data structures
│   ├── convex.py       # Markdown parsing & tokenization logic
│   └── copystatic.py   # Filesystem traversal & asset pipeline
├── template.html       # Base HTML injection template
└── *.sh                # Bash scripts for automated build & testing

```

## 🚀 Quick Start & Execution

### Prerequisites

* Python 3.x (Zero external dependencies required)
* Bash/Zsh environment

### Execution via Shell Automation

Instead of running raw Python commands, the project utilizes bash scripts to automate the build and test pipelines, ensuring a frictionless developer experience.

1. **Clone the repository:**
```bash
git clone https://github.com/shreyansh15624/ssg.git
cd ssg

```


2. **Execute the Build Pipeline:**
```bash
# Cleans the docs/ directory and compiles a fresh build
./build.sh

```


3. **Run the Automated Test Suite:**
```bash
# Discovers and executes all unit tests in the src/ directory
./test.sh

```


4. **Serve the Local Build:**
```bash
./main.sh

```


*Navigate to `http://localhost:8888*`

## 🌐 Production Deployment

The compilation engine is optimized to generate artifacts ready for static hosting environments. By outputting directly to the `docs/` folder, the project natively supports the **GitHub Pages** deployment workflow directly from the `main` branch.
