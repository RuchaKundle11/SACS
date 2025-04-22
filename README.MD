# SACS: Semantics-Aware Caching System

A smart web cache replacement algorithm that uses recency, frequency, and semantic distance based on page links.

### 🔍 What It Does

When a cache is full and a new page is accessed, SACS:
- Calculates the **distance** from recently accessed (pivot) pages
- Considers **frequency** of access
- Includes **recency** of access
- Computes a score and evicts the page with the highest score

### 🧠 Formula

