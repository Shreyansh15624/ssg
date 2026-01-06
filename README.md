# Static Site Generator (SSG)

A robust, custom-built static site generator written in Python. This engine recursively crawls a directory of Markdown content, parses the text into HTML nodes, and generates a full static website with support for templates and static assets (CSS/Images).

This project was built as part of the backend engineering curriculum on [Boot.dev](https://boot.dev).

## 🚀 Features

* **Recursive Directory Traversal:** Automatically mirrors the folder structure of the `content` directory into the output site, supporting infinite nesting of sub-pages.
* **Markdown Parsing Engine:**
    * **Block-Level:** Handles Paragraphs, Headings (H1-H6), Code Blocks, Blockquotes, Unordered Lists, and Ordered Lists.
    * **Inline-Level:** Supports **Bold**, *Italic*, `Code`, [Links](url), and ![Images](url).
* **Static Asset Management:** Recursively cleans and copies images and CSS files from source to public output.
* **Templating System:** Injects generated HTML into a reusable `template.html` for consistent site-wide layout.
* **Deployment Ready:** Supports configurable base paths via command-line arguments (critical for GitHub Pages hosting).

## 🧠 Technical Implementation & Learnings

Building this project required solving several core computer science problems from scratch:

### 1. Recursion & Tree Traversal
Instead of a flat file approach, I implemented a "Traffic Controller" algorithm. It distinguishes between files and directories, recursively diving into sub-folders to maintain the exact tree structure of the input content in the final build.

### 2. The DOM as Data Structures
I avoided using libraries like `BeautifulSoup` to create HTML. Instead, I built a system of classes representing the Document Object Model:
* **`HTMLNode`:** The base class for all HTML elements.
* **`LeafNode`:** Represents elements with no children (e.g., `<b>`, `<img>`).
* **`ParentNode`:** Represents elements that contain other nodes (e.g., `<div>`, `<ul>`), enabling the construction of complex, nested HTML trees.

### 3. Text Parsing & Tokenization
Converting Markdown requires a multi-pass approach:
1.  **Block Splitting:** The raw text is first divided into "Blocks" (paragraphs, lists, etc.).
2.  **Type Detection:** Each block is analyzed to determine its HTML tag wrapper.
3.  **Inline Tokenization:** Text within blocks is scanned to convert symbols (like `**` or `[ ]`) into their respective HTML nodes.

### 4. Command Line Arguments (`sys.argv`)
To support hosting on GitHub Pages (which often uses a sub-path like `/project-name/`), the generator accepts a base URL argument. This allows the site to function correctly both on `localhost` (root path `/`) and production URLs (sub-path `/ssg/`).

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Version Control:** Git
* **Testing:** Unittest (standard library)
* **Deployment:** GitHub Pages (Docs folder strategy)

## 💻 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/shreyansh15624/ssg.git](https://github.com/shreyansh15624/ssg.git)
    cd ssg
    ```

2.  **Run the Generator:**
    ```bash
    # Runs the generator with root base path "/"
    python3 src/main.py
    ```

3.  **Start a Local Server:**
    Go to the `docs` (or `public`) folder and serve it:
    ```bash
    cd docs
    python3 -m http.server 8888
    ```
    Open your browser to `http://localhost:8888`.

## 🌐 Deployment Workflow

This project is configured to deploy via the **GitHub Pages /docs folder** method.

1.  **Generate for Production:**
    ```bash
    # Passes the repository name as the base path to fix links
    python3 src/main.py "/ssg/"
    ```
2.  **Push to GitHub:**
    The build script outputs to the `docs/` folder, which is committed to the `main` branch. GitHub Pages is configured to serve directly from `/docs`.

---
*Built with ❤️ and Python.*