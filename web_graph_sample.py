# web_graph_sample.py

from sacs_algorithm import sacs_eviction

# Define web graph (directed)
web_graph = {
    'index.html': ['menu.html', 'about.html'],
    'menu.html': ['contact.html'],
    'contact.html': [],
    'about.html': []
}

# Define cache with frequency and recency
cache = {
    'menu.html': {'frequency': 2, 'recency': 3},
    'contact.html': {'frequency': 1, 'recency': 5},
    'index.html': {'frequency': 4, 'recency': 1}
}

# Most recently accessed page is the pivot
pivot = 'index.html'

# Decide which page to evict
page_to_evict = sacs_eviction(cache, pivot, web_graph)
print("Page to evict:", page_to_evict)
