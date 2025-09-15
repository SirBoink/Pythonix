# Open Source LLM Evaluation For Student Competence Analysis
My implementation of the python task 3 for the FOSSEE semester long internship

## Setup and Reproducibility

The entire project was designed with reproducibility and ease of verification in mind.

1.  All tasks have been executed in Google Colab using only free tier resources.
2.  To run the evaluation, you only need a Google account and the Colab website.
3.  The models were selected with compute resource in mind; models with more than 20 billion parameters were not considered due to their significant computational costs.
   
## Reasoning

### What makes a model suitable for high-level competence analysis?

A model is suitable for high-level competence analysis based on three criteria:

1.  **Instruction Following:** The model must be able to adhere to specific instructions, like in this project, a system prompt (persona) is defined for the model to follow. This contains extensive info on how to approach a student written code and what metrics to evaluate on based on research backed NLP frameworks like Code Knowledge Tracing (CodeLKT), research-validated CT concepts, practices, and perspectives framework and Zone of Proximal Development (finding out the student's next learning edge)
2.  **Training on Code Data:** The model's training data must include a substantial amount of high-quality code, particularly in the target language (Python, in this case). This ensures a deeper understanding of syntax and logic. 
3.  **Active Maintenance and Updates:** The model should be actively maintained by its developers. This indicates that the model is likely to improve over time, with bugs being fixed and new capabilities being added.

### How would you test whether a model generates meaningful prompts?

To test whether a model generates meaningful prompts, I believe the right context is crucial. In this project, I decided to create a system prompt that instructs the LLM to adopt a persona named "Pythonix" (inspired by my favorite comic "Asterix"). This persona based system prompt was designed to act as a helpful and encouraging tutor. The system prompt guides the LLM to follow a set pattern: first, analyze the provided student code for errors and misconceptions, and then, generate questions that encourage deeper thinking and lead the student to their own discovery. It was seen that without this contextual guidance, the LLMs consistently failed to grasp the  nature of the task and would often just provide the corrected code. 

### What trade-offs might exist between accuracy, interpretability, and cost?

There are quite a few significant trade-offs between accuracy, interpretability, and cost, especially with the lightweight, open-source models used in this project.

* Due to their smaller size (7B parameters), these models lack a more nuanced understanding of the input code. They are quite prone to hallucinations (like identifying bugs that don't exist while missing actual errors) in exchange for being less expensive and faster to run. Accuracy tends to be very inconsistent across different problem types. I observed an inverse relation between the complexity of the programming problem and the accuracy of the model's evaluation.

* Interpretability is yet again a major challenge. These models are indeed blackboxes and do not reveal their internal thought processes, making it difficult to understand why they outputted a certain prompt or question. This is further exacerbated by the fact that these open-source models are not designed with reasoning capabilities for tasks in the way that SOTA models like GPT, Gemini or Claude are.

### Why did you choose the model you evaluated, and what are its strengths or limitations?

I chose **Qwen 2.5 Coder** and **Codellama Instruct** for this task based on three considerations:

1.  **Cost:** Both models are small enough to be run on free tier GPU resources (google colab).
2.  **Code-Specific Training:** Both models have been trained on large datasets of code, which is a bonus for this task.
3.  **Instruction following:** Both have been fine-tuned for following instructions, which is important for adhering to our "Pythonix" system prompt.

Between the two, **Qwen 2.5 Coder** was the comparative winner in our "LLM as a Judge" evaluation.

**Strengths:**
*   Qwen 2.5 demonstrated a better understanding of the Python code snippets.
*   It was more consistently able to identify the specific area where the student was struggling.
*   The guiding questions it generated were generally on-point and aligned with the goal of the task to act as a competence analyst.
*   Importantly, it adhered to the instruction of not revealing the direct answer in all test cases.

**Limitations:**
*   The most significant weakness was its tendency to hallucinate non-existent bugs while sometimes failing to identify actual errors. This is a big concern for accurate student competence analysis and could potentially mislead a student.



