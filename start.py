# === Configuration ===
ROOT_URL = "https://www.uni-corvinus.hu/"
MARKERS = ["data-elementor-type|wp-page", "data-elementor-type|wp-post"]
REQUEST_LIMIT = 100
DURATION_LIMIT = 500 # seconds
INTERVAL = 0.1 # seconds
TIMEOUT = 3 # seconds
MAX_RESULTS = 100
PAGERANK_DAMPING_FACTOR = 1.25

# === Dependencies ===
import time
import webbrowser
from threading import Thread
from app.app import app 
# from app.search_engine import Searching
from app.search_engine import Crawling 
from app.search_engine import Vectorizing
from app.search_engine import WebGraph 
from app.search_engine import UIHelper

# === Start Indexing ===
start_time = time.time()
print("[START] Initializing...")

webgraph = WebGraph()
crawler = Crawling(ROOT_URL, MARKERS, REQUEST_LIMIT, DURATION_LIMIT, INTERVAL, TIMEOUT)
crawler.webgraph = webgraph

vectorizer = Vectorizing()

print("[START] Starting crawl...")
crawler.handler()
print(f"[START] Crawling done in {round(time.time() - start_time, 2)} seconds.")

contents = {
    url: data["content"]
    for url, data in webgraph.graph.nodes(data=True)
    if "content" in data
}

print("[START] Starting vectorization...")
vectors = vectorizer.handler(contents)
webgraph.update_vector(vectors)
print(f"[START] Vectorizing done in {round(time.time() - start_time, 2)} seconds.")

# === Inject context into search engine ===
UIHelper.set_context(vectorizer, webgraph, MAX_RESULTS, PAGERANK_DAMPING_FACTOR)


# === Launch Flask in separate thread and open browser ===
def run_flask():
    app.run(debug=False, port=5999)

print("[START] Launching browser and web UI...")
flask_thread = Thread(target=run_flask)
flask_thread.daemon = False  # ensure it keeps running
flask_thread.start()

time.sleep(1)  # Give Flask a moment to start
webbrowser.open("http://localhost:5999")

# Hold the main thread
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[START] Server stopped by user.")