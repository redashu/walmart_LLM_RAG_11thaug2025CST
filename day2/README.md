# walmart_LLM_RAG_11thaug2025CST

### Revision 1 

<img src="rev1.png">

### LLM more info 

<img src="rev2.png">

## COT example 1 

```
ON saturday, customer traffic is usually 40% higher than weekdays,
on weekdays , we schedule 10 cashiers.
think step-by-step about how many cashiers should be scheduled on saturday to maintaince the same QOS / level or service

```

# Walmart LLM Prompt Examples with Chain-of-Thought (CoT) Reasoning

## 1. Customer Review Sentiment Classification (CoT)

**Dataset Row:**  
"The item arrived quickly, but the box was torn."

**Prompt:**  
Classify the sentiment of this Walmart customer review as Positive, Neutral, or Negative.

**Review:**  
> "The item arrived quickly, but the box was torn."

**Let's think step by step:**
1. Identify any positive statements in the review.
2. Identify any negative statements in the review.
3. Determine which sentiment dominates or if it is balanced.
4. Output the final sentiment classification.

**Expected Reasoning & Output:**
- Step 1: Positive — "The item arrived quickly."
- Step 2: Negative — "The box was torn."
- Step 3: Positive and negative balance out, so it's neutral.
- **Final sentiment:** Neutral

---

## 2. Product Category Assignment (CoT)

**Dataset Row:**  
"Stainless steel 20-piece flatware set for dining table."

**Prompt:**  
Assign the most accurate Walmart product category for the following item description.

**Item:**  
> "Stainless steel 20-piece flatware set for dining table."

**Let's think step by step:**
1. Identify the type of product mentioned.
2. Determine its main use.
3. Match it with Walmart's product category hierarchy.
4. Output the most accurate category path.

**Expected Reasoning & Output:**
- Step 1: Product is a "flatware set" made of stainless steel.
- Step 2: Main use is dining and serving food.
- Step 3: In Walmart’s hierarchy, it falls under Kitchen & Dining → Tableware → Flatware Sets.
- **Final category:** Kitchen & Dining > Tableware > Flatware Sets

---

## 3. Inventory Status Suggestion (CoT)

**Dataset Row:**  
"Store #102: Item SKU987 - sales spiked, stock almost depleted, next restock in 5 days."

**Prompt:**  
Suggest the best inventory action for the following Walmart store update.

**Inventory Update:**  
> "Store #102: Item SKU987 - sales spiked, stock almost depleted, next restock in 5 days."

**Let's think step by step:**
1. Identify the current stock status.
2. Identify the demand trend.
3. Consider restock timing and possible risks.
4. Suggest the best inventory management action.

**Expected Reasoning & Output:**
- Step 1: Stock is almost depleted.
- Step 2: Sales are increasing sharply.
- Step 3: Next restock is in 5 days, risk of stockout before delivery.
- Step 4: Best action — expedite restocking or source from nearby stores to avoid lost sales.
- **Final action:** Expedite restock or transfer inventory from nearby locations.


## prompt templating using LangChain 

<img src="lang1.png">

