# 1. Semantic Similarity

Semantic similarity measures how close two pieces of text are in meaning, regardless of their exact wording.

- It’s not about matching keywords; it’s about understanding intent or context.

**Example:**

> “I am eating an apple.”  
> “I am having a fruit for lunch.”

Different words, but semantically related.

**How is it measured?**

- We use vector embeddings: Each text is converted into a high-dimensional numerical vector (e.g., 1536 dimensions from OpenAI’s embeddings model).
- If two vectors are close in direction/position, their meanings are similar.

---

# 2. Cosine Similarity

Cosine similarity quantifies semantic similarity between vectors.

- Think of two vectors as arrows from the origin in high-dimensional space.
- We check the angle between them, not their length.

**Formula:**

```
cosine similarity = (A · B) / (||A|| * ||B||)
```

Where:
- `A · B` = dot product of the vectors
- `||A||` = magnitude (length) of vector A

**Range:**
- `1` → exactly the same direction (most similar meaning)
- `0` → perpendicular (no relation)
- `-1` → opposite meaning

---

# 3. Cosine Distance

Sometimes we talk about distance instead of similarity:

```
cosine distance = 1 - cosine similarity
```

- Smaller distance = more similar
- Larger distance = less similar

**Example:**

Suppose embeddings produce these 3D vectors:

- Text 1: `[1, 2, 3]`
- Text 2: `[2, 4, 6]`

- Cosine similarity = `1` (same direction → meaning is identical)
- Cosine distance = `0`

---

✅ **In short:**

- **Semantic similarity** = conceptual closeness in meaning
- **Cosine similarity/distance** = mathematical way to measure how close the meaning is using vector angles