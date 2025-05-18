# Internal Search Engine

## Version 1.0.1

Implementation of an internal site crawler, vector-based search engine, and Google-style UI.

---

## Goal

This project implements a local search engine for any website starting from a given root URL.  
It includes:
- URL crawling and content extraction
- Graph-based network structure with PageRank
- Vectorization of content for cosine similarity search
- Combined scoring of relevance and importance
- Search UI powered by Flask

This is group project for Advanced Programming course by Sándor Juhász and Ádám Balázs Csapó, at Corvinus University of Budapest, Spring 2025

---

## Authors

- **Shayan Ghiaseddin**: MSc Business Informatics – Corvinus University of Budapest

- **Péter Orosz**: BSc Data Science – Corvinus University of Budapest

- **Bence Balázs Balás**: MSc Business Informatics – Corvinus University of Budapest

---

## License

This project is released under the **MIT License**.

---

## Configuration

In `start.py`, you can change these parameters before running:

```python
ROOT_URL = "https://www.uni-corvinus.hu/"
MARKERS = ["data-elementor-type|wp-page", "data-elementor-type|wp-post"]
REQUEST_LIMIT = 100             # Max number of pages to crawl
DURATION_LIMIT = 500            # Time limit in seconds
INTERVAL = 0.1                  # Delay between requests (in seconds)
TIMEOUT = 3                     # Request timeout (in seconds)
MAX_RESULTS = 100               # Max results to return in search
PAGERANK_DAMPING_FACTOR = 1.25  # Damping factor for PageRank calculation
```

---

## How to Build

Run the provided build script:

```bash
./build.sh
```

This will:
- Convert notebook content to Python
- Copy `app/`, `assets/`, and `templates/` into `build/`
- Prepare the Flask app for launch

---

## How to Start

After building the project:

```bash
cd build
python start.py
```

This will:
- Crawl and index the website
- Vectorize and score the pages
- Launch a local Flask web UI at:  
  [http://localhost:5999](http://localhost:5999)

Enjoy searching your website with full control and visibility!
