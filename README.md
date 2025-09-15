# Open Source LLM Evaluation For Student Competence Analysis
My implementation of the python task 3 for the FOSSEE semester long internship

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project conducts a rigorous, pairwise evaluation of two open-source Large Language Models (LLMs)—**Qwen-2.5-Coder** and **Code-Llama-7B-instruct**—to assess their ability to provide meaningful pedagogical feedback on student-written Python code.

Using an "LLM as a Judge" framework, we analyze each model's performance in identifying bugs, understanding student misconceptions, and guiding them toward solutions without giving away the answer.

## Table of Contents
1.  [Data Curation](#1-Data-Curation)
2.  [The Approach](#2-the-approach)
3.  [Models Evaluated](#3-models-evaluated)
4.  [Key Findings](#4-key-findings)
5.  [Reasoning](#5-Reasoning)
    *   [What Makes a Model Suitable for Competence Analysis?](#what-makes-a-model-suitable-for-competence-analysis)
    *   [How would you test whether a model generates meaningful prompts?](#How-would-you-test-whether-a-model-generates-meaningful-prompts?)
    *   [Trade-Offs: Accuracy, Interpretability, and Cost](#trade-offs-accuracy-interpretability-and-cost)
    *   [Why did you choose the model you evaluated, and what are its strengths or limitations?](#why-did-you-choose-the-model)
6.  [How to Replicate](#6-how-to-replicate)

## Data Curation

To test the selected lightweight open source models, I collect and formed a representative dataset of student written python code (both correct and buggy) across 5 categories: 

1. Basic Python Operations (Count vowels and GCD)
2. String and output formatting (Framed Word and valid parentheses)
3. Data Structures (unique dates and reversed linked list)
4. Algorithmic thinking (Levensthein and quicksort)
5. Graphs and DP (Knapsack and Find first sorted item)

The code is from Quixbugs, Refactorly and my own attempts from the Helsinki Python MOOC 2025 course. 

## 2. The Approach

To ensure a structured and pedagogically sound evaluation, I implemented the following methodology:

#### **LLM as a Judge Framework**
We employed an impartial evaluation framework where a more powerful LLM (acting as an expert judge) assesses the quality of the two models' outputs against a ground truth analysis of the student's code.

#### **The "Pythonix" Persona**
To elicit high-quality, Socratic-style feedback, we developed a system prompt that instructs the models to adopt the persona of "Pythonix," a helpful and encouraging tutor inspired from the world of the comic 'Asterix'.

> The system prompt guides the LLM to first analyze the student's code for errors and then generate questions that encourage deeper thinking and lead the student to their own discovery. Without this contextual guidance, the LLMs consistently failed to grasp the nature of the task and would often just provide the corrected code.

#### **Research-Backed Evaluation Criteria**
The evaluation rubric was designed based on established frameworks, including:
*   **Code Knowledge Tracing (CodeLKT):** To assess the model's understanding of the code's logic.
*   **Computational Thinking (CT) Concepts:** To evaluate the identification of core programming principles.
*   **Zone of Proximal Development (ZPD):** To measure the model's ability to identify the student's "next learning edge" and provide appropriate guidance.

## 3. Models Evaluated

We chose two prominent 7B-parameter models based on their cost-effectiveness, code-specific training, and instruction-following capabilities.

| Model | Strengths | Limitations |
| :--- | :--- | :--- |
| **Qwen-2.5-Coder-7B** | ✅ Better grasp of Python code nuances.<br>✅ More consistent in identifying the student's area of struggle.<br>✅ Generated on-point, guiding questions.<br>✅ Adhered to the instruction of not revealing the direct answer. | ❌ Prone to hallucinating non-existent bugs.<br>❌ Occasionally failed to identify critical, ground-truth errors. |
| **Code-Llama-7B-instruct** | ✅ Fine-tuned for following instructions.<br>✅ Trained on a large corpus of code. | ❌ Less accurate in code analysis compared to Qwen.<br>❌ Generated less relevant or helpful guiding prompts.<br>❌ Frequently misidentified core code structures (e.g., seeing loops where there was recursion). |

## 4. Key Findings

Across the 10 programming problems evaluated, **Qwen-2.5-Coder was the clear comparative winner.**

*   **Superior Code Analysis:** Qwen demonstrated a more accurate understanding of the student's code, correctly identifying algorithms like recursion and dynamic programming where CodeLlama failed.
*   **Higher Pedagogical Value:** Qwen's generated prompts were more relevant and effective at guiding the student toward the actual bug or misconception.
*   **Critical Weakness:** Both models struggled with accuracy. The most significant limitation observed was the tendency to **hallucinate non-existent issues while completely missing fatal errors** (e.g., `IndexError`, `RecursionError`). This is a major concern for reliable student competence analysis.

## 5. Reasoning

### What Makes a Model Suitable for Competence Analysis?
A model's suitability for this task depends on three criteria:
1.  **Instruction Following:** The ability to adhere to a complex system prompt (like the "Pythonix" persona) is paramount.
2.  **Coding Data Training:** The model's training data must include a substantial amount of high-quality code to ensure a deep understanding of syntax, logic, and common patterns.
3.  **Active Maintenance:** An actively developed model is more likely to improve over time, with bug fixes and enhanced capabilities.

### How would you test whether a model generates meaningful prompts?
I found that simply asking the LLM to "find the bug" was ineffective. By creating the **"Pythonix"** persona, I framed the task within a pedagogical context, which was crucial for generating meaningful, Socratic-style prompts.

### Trade-Offs: Accuracy, Interpretability, and Cost
The use of lightweight, open-source models introduces significant trade-offs:
*   **Accuracy vs. Cost:** The 7B parameter size, while cost-effective, limits the models' nuanced understanding. We observed an inverse relationship between the complexity of the programming problem and the accuracy of the model's evaluation.
*   **Interpretability:** As black boxes, these models do not reveal their internal reasoning. It's difficult to know *why* a model generated a specific prompt, which complicates debugging and refinement. These models are not primarily designed for the kind of reasoning capabilities seen in SOTA models like GPT-5 or Gemini 2.5.

### Why did you choose the model you evaluated, and what are its strengths or limitations?

I chose Qwen-2.5-Coder and Codellama-Instruct based on three considerations:

1. Cost: Both models are small enough to be run on free-tier GPU resources (like Google Colab).
2. Code-Specific Training: Both have been trained on large datasets of code.
3. Instruction Following: Both have been fine-tuned for following instructions, which is important for adhering to our "Pythonix" system prompt.
 

#Resources Used 
1. [colab.research.google.com]
2. aistudio.google.com (Gemini 2.5 Pro; LLM As a Judge)
3. [https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf]
  
   

