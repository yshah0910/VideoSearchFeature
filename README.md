
# Video Search Feature
This project implements a Python API to systematically download 50 NPR YouTube channel videos, along with their corresponding closed captions. The main focus is on building a video preprocessing pipeline and an efficient search feature for video content.

## Youtube Link for GUI Demo: https://youtu.be/PsP9Tgq1WbQ

## Key Features:

### Video Downloading & Preprocessing:


Downloads videos and closed captions from NPR's YouTube channel.
Processes video frames and captions into a structured format for analysis.
### Embedding with Word2Vec:

Utilizes a vector database to store video frames as vector embeddings and video transcripts as text embeddings using Word2Vec.

This enables a unified, efficient storage solution for video content.
### Efficient Search Capability:

Combines frame and transcript embeddings using dot product functionality to offer an integrated video search experience.

Implements cosine similarity search on the GUI to retrieve relevant video segments based on user queries.

## Tech Stack

Python: (Pandas, PyTorch, OpenCV, TensorFlow)

Docker: ankane/pgvector for vector search

PostgreSQL: Used for managing and querying vectorized data

