# Markdown-HTML-Site-Generator

This tool converts Markdown files into HTML to build and deploy a static website. It's simple, fast, and ideal for lightweight documentation or personal websites.

---

## 🚀 Features

- Converts Markdown (`.md`) files to HTML
- Preserves directory structure and internal links
- Serves the site locally for testing
- Supports static assets like images and CSS

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/rgibby818/Markdown-HTML-Site-Generator.git
   cd Markdown-HTML-Site-Generator/
2. Make the build scripts executable: 
    ```bash
    chmod +x main.sh build.sh
## 🛠️ Usage

1. Prepare your content:
    - Delete existing files in the docs/ and content/ directory:
    ```bash
    rm -rf docs/ content/*
    ```
    - Add your own Markdown files to the content/ directory.
    - Maintain internal link structure. For example:
        - If `file.md` links to `folder/other.file.md`, then there must be a `folder/other_file.md` inside `content/` directory. 
2. Organize static files:
    - Place images, CSS, and other static assets inside static/ directory.

3. Preview the site locally:
    -Run the main script to generate HTML files and start a local server on port 8888:
    ```bash
    ./main.sh
    ```
    - Then visit http://localhost:8888 in your browser.
4. Build your site for deployment:

    - Edit the build.sh script to include your deployment destination.
        > For example, for GitHub Pages, use your repository name.
    ```bash
    ./build.sh
    ```
    
## 📁 Directory Structure
```bash
Markdown-HTML-Site-Generator/
├── build.sh         # For building your site for deployment
├── main.sh          # For previewing your site locally
├── content/         # Your Markdown files
├── docs/            # Output directory for generated HTML
├── static/          # CSS, images, and other static assets
└── ...


```