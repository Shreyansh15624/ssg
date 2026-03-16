# ⚡ Zero-Dependency Python SSG: Markdown-to-HTML Compiler

A lightweight, high-performance static site generator built entirely from scratch in standard Python. This engine bypasses bloated external libraries, featuring a custom lexer, a recursive file-system crawler, and an in-memory Document Object Model (DOM) to compile raw Markdown into a deployable static site.

## 🏗️ System Architecture & Compiler Design

This tool was architected to demonstrate a deep understanding of parsing algorithms, data structures, and zero-dependency environment execution.

### 1. Lexical Analysis & Custom AST (Abstract Syntax Tree)

Instead of relying on regex hacks or `BeautifulSoup`, the engine constructs a strict internal representation of the HTML DOM.

- **Node Hierarchy:** Utilizes a polymorphic class structure (`HTMLNode`, `LeafNode`, `ParentNode`) to represent elements.
- **Multi-Pass Parsing:** The parsing engine separates concerns by first dividing raw markdown into structural blocks (Headings, Code Blocks, Lists), and subsequently executing an inline-level tokenization pass for text formatting (Bold, Italic, Links).

### 2. Recursive Filesystem Traversal

- Implements a Depth-First Search (DFS) algorithm to crawl the `content/` directory.
- Distinguishes between sub-directories and target files, mirroring the exact source tree in the final build output while recursively propagating static assets (CSS, images) to the `public/` directory.

### 3. Environment-Aware Path Resolution

- **Dynamic Routing:** Hardcoded relative links break in sub-directory deployments (like GitHub Pages). The engine accepts configurable base-path arguments via `sys.argv` at runtime, dynamically resolving and injecting environment-aware URIs into the final HTML compilation.

## 🚀 Quick Start & Compilation

### Prerequisites

- Python 3.x (Zero external dependencies required)

### Execution

1. **Clone the repository:**
```bash
git clone https://github.com/shreyansh15624/ssg.git
cd ssg

```


2. **Compile the Site (Localhost Environment):**
```bash
# Executes the build step targeting the root path "/"
python3 src/main.py

```


3. **Serve the Build Artifacts:**
```bash
cd docs
python3 -m http.server 8888

```


*Navigate to `http://localhost:8888*`

## 🌐 Production Deployment

The compilation engine is optimized to generate artifacts ready for static hosting environments (e.g., GitHub Pages, AWS S3, Vercel).

**Compile for Sub-Directory Hosting:**

```bash
# Injects the repository name as the base URL to prevent broken asset routing
python3 src/main.py "/ssg/"

```

## 🧪 Testing

The parsing engine is fully unit-tested using Python's standard `unittest` library to ensure block and inline tokenization edge cases are strictly handled.

```bash
python3 -m unittest discover -s src

```