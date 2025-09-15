# Open Source LLM Evaluation For Student Competence Analysis
My implementation of the python task 3 for the FOSSEE semester long internship

Here, I conduct a rigorous, pairwise evaluation of two open-source Large Language Models (LLMs) that I've chosen: **[Qwen-2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)** and **[Code-Llama-7B-instruct-hf](https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf)** to assess their ability to be high level student competence analysts.

Using an "LLM as a Judge" framework, I analyze each model's performance in identifying bugs, understanding student misconceptions, and guiding them toward solutions without giving away the answer.

## Research Plan 
The research plan can be read [here](research%20plan.txt)

## Table of Contents

1.  [Data Curation](#1-data-curation)
2.  [The Approach](#2-the-approach)
3.  [Models Evaluated](#3-models-evaluated)
4.  [Key Findings](#4-key-findings)
5.  [Reasoning](#5-reasoning)
    *   [What Makes a Model Suitable for Competence Analysis?](#what-makes-a-model-suitable-for-competence-analysis)
    *   [How would you test whether a model generates meaningful prompts?](#how-would-you-test-whether-a-model-generates-meaningful-prompts)
    *   [What trade-offs might exist between accuracy, interpretability, and cost?](#what-trade-offs-might-exist-between-accuracy-interpretability-and-cost)
    *   [Why did you choose the model you evaluated, and what are its strengths or limitations?](#why-did-you-choose-the-model-you-evaluated-and-what-are-its-strengths-or-limitations)
6.  [Reproducibility](#6-reproducibility)
7.  [My Thoughts](#7-my-thoughts)
8.  [Declaration](#8-declaration)

## 1. Data Curation

To test the selected lightweight open source models, I collected and formed a representative dataset of student written python code (both correct and buggy) across 5 categories: 

1. Basic Python Operations (Count vowels and GCD)
2. String and output formatting (Framed Word and valid parentheses)
3. Data Structures (unique dates and reversed linked list)
4. Algorithmic thinking (Levensthein and quicksort)
5. Graphs and DP (Knapsack and Find first sorted item)

The student written code has been gathered from [Quixbugs](https://github.com/jkoppel/QuixBugs), [Refactorly](https://github.com/githubhuyang/refactory) and my own personal code submission attempts from the [Helsinki Python MOOC 2025 course](https://programming-25.mooc.fi). 

## 2. The Approach

To ensure a structured evaluation, I have implemented the following methodology:

#### **LLM as a Judge Framework**
An impartial evaluation framework where a more powerful LLM (acting as an expert judge) assesses the quality of the two models' outputs against a ground truth analysis of the student's code.

#### **The "Pythonix" Persona**
To get high-quality, Socratic style feedback, I developed a system prompt that instructs the models to adopt the persona of "Pythonix," a helpful and encouraging tutor inspired from my favorite comic book 'Asterix'.

> The system prompt guides the LLM to first analyze the student's code for errors and then generate questions that encourage deeper thinking and lead the student to their own discovery. Without this contextual guidance, I observed that the LLMs consistently failed to grasp the nature of the task and would often just provide the corrected code.

#### **Research-Backed Evaluation Criteria**
The evaluation rubric was designed based on established frameworks, including:
*   **Code Knowledge Tracing (CodeLKT):** To assess the model's understanding of the code's logic.
*   **Computational Thinking (CT) Concepts:** To evaluate the identification of core programming principles.
*   **Zone of Proximal Development (ZPD):** To measure the model's ability to identify the student's "next learning edge" and provide appropriate guidance.

## 3. Models Evaluated

I chose two prominent 7B-parameter models based on their cost-effectiveness, code-specific training, and instruction-following capabilities.

Of course. A more technical and robust table will provide much more context for readers familiar with LLMs.

Here is a revised "Models Evaluated" section. It replaces the original table with one that includes key technical specifications and summarizes your own findings more formally.

---

## 3. Models Evaluated

I chose two prominent 7B-parameter models for this evaluation, balancing performance on code-related tasks with the accessibility required for cost-free reproducibility. The table below provides a comparison: 

| Attribute | Qwen-2.5-Coder-7B-Instruct | CodeLlama-7B-Instruct-hf |
| :--- | :--- | :--- |
| **Developer** | Alibaba Cloud | Meta |
| **Parameters** | ~7 Billion | ~7 Billion |
| **Context Length** | 64,000 tokens | 16,000 tokens |
| **Architecture** | Qwen2.5 with Group Query Attention (GQA) | Llama 2 with Grouped-Query Attention (GQA) |
| **Fine-tuning Focus** | Optimized for a wide range of code-related tasks and instruction-following. | Instruction-following on a base model specialized for code generation and completion. |
| **Observed Strengths** | **Superior Code Analysis:**<br>Accurately identified complex structures like recursion and dynamic programming.<br><br>**Higher Pedagogical Value:**<br>Generated more relevant, Socratic-style questions that guided users to the core issue. | **Strong Format Adherence:**<br>Consistently followed the structural and tonal requirements of the "Pythonix" system prompt. |
| **Observed Limitations** | **Critical Error Blindness:**<br>Failed to detect fatal runtime errors (`IndexError`, `RecursionError`).<br><br>**Hallucination:**<br>Prone to identifying and flagging non-existent bugs in correct code. | **Shallow Code Understanding:**<br>Frequently misidentified fundamental code structures (e.g., recursion as iteration).<br><br>**Irrelevant Prompt Generation:**<br>Often produced nonsensical or unhelpful diagnostic questions. |

## 4. Key Findings

Across the 10 programming problems evaluated, **Qwen-2.5-Coder was the clear comparative winner.**

*    Qwen demonstrated a more accurate understanding of the student's code, correctly identifying algorithms like recursion and dynamic programming where CodeLlama failed.
*    Qwen's generated prompts were more relevant and effective at guiding the student toward the actual bug or misconception.
*    Both models struggled with accuracy. The most significant limitation observed was the tendency to **hallucinate non-existent issues while completely missing fatal errors** (`IndexError`, `RecursionError`). This is a major concern for reliable student competence analysis.

## 5. Reasoning

### What Makes a Model Suitable for Competence Analysis?
A model's suitability for this task depends on three criteria:
1.  The ability to adhere to a complex system prompt (like for the "Pythonix" persona) or instruction following.
2.  The model's training data must include a substantial amount of high-quality code to ensure a deep understanding of syntax, logic, and common patterns.
3.  The model must be actively maintained as its more likely to improve over time, with bug fixes and enhanced capabilities.

### How would you test whether a model generates meaningful prompts?
I found that simply asking the LLM to "find the bug" was ineffective. By creating the **"Pythonix"** persona, I framed the task within a pedagogical context, which was crucial for generating meaningful, Socratic-style prompts.

### What trade-offs might exist between accuracy, interpretability, and cost?
The use of lightweight, open-source models introduces significant trade-offs:
*   The 7B parameter size, while cost-effective, limits the models' nuanced understanding. We observed an inverse relationship between the complexity of the programming problem and the accuracy of the model's evaluation.
*   As black boxes, these models do not reveal their internal reasoning (well known problem). It's difficult to know *why* a model generated a specific prompt, which complicates debugging. These models are not primarily designed for the kind of reasoning capabilities seen in SOTA models like GPT-5 or Gemini 2.5.

### Why did you choose the model you evaluated, and what are its strengths or limitations?

I chose Qwen-2.5-Coder-Instruct and Codellama-Instruct-hf based on three considerations:

1. Cost: Both models are small enough to be run on free-tier GPU resources (like Google Colab).
2. Code-Specific Training: Both have been trained on large datasets of code.
3. Instruction Following: Both have been fine-tuned for following instructions, which is important for adhering to our "Pythonix" system prompt.

## 6. Reproducibility
From the get-go, my major goal was to make this implementation easy for anyone to verify and run. I also believe you shouldn't need a massive budget or a supercomputer to do it. So: 

1. I stuck to 7B parameter models that are freely available and lightweight.
2. The entire evaluation was designed to run on the free tier of Google Colab. Anyone with a Google account can copy and paste the code and verify the results.
3. The repository includes the models' outputs and the ground truth (as json files), so you can analyze the results without having to re-run the entire pipeline if you don't want to.

## 7. My Thoughts
My core takeaway is the dangerous inconsistency of these 7B-parameter models in this context. Their performance is a paradox of insight and failure. On one hand, the potential is undeniable. When Qwen 2.5 generated a question about how the quicksort implementation handles duplicate numbers, the exact logical flaw in the code, it demonstrated a spark of what I was looking for.  However, this results was standalone and unreliable. The same models that showed this spark also completely failed to detect fatal flaws like the RecursionError in the GCD function or IndexError in the binary search. Also, CodeLlama's repeated misidentification of recursion as a for loop reveals a shallow, pattern-matching-based understanding. 

While I do believe these same models with more parameters (32, 70 or 312B) could yield much better results, the cost of running those would be enormous. I belive, in their current state, these open source (lightweight) models are unsuitable for high student competence roles. Their value more lies in being a productivity tool for human teachers/professors. 

## 8. Declaration

The use of generative AI is declared for repetitive tasks, research and for implementing the 'LLM as a Judge' framework.
[Google AI Studio](aistudio.google.com) was used with the following settings: 
1. model = Gemini 2.5 pro
2. temperature = 0.1
3. Thinking mode = enabled
4. Thinking budget = 32768 tokens
5. Grounding in google search enabled
6. URL context enabled
7. Output length = 65536 tokens
8. Top P value = 0.95
   
   

