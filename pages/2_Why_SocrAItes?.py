import streamlit as st

st.set_page_config(
    page_title="Why should you use SocrAItes?",
    page_icon="icon.jpg",
)

st.image("icon.jpg", width=100)

markdown_text = """
# Unlock Deeper Understanding with the Power of Socrates & Feynman

Are you tired of surface-level learning and rote memorization? What if you could unlock a method that helps you not only understand complex topics but also master the art of explaining them? By blending the Socratic Method with the Feynman Technique, you can achieve this transformative approach to learning. Here’s how they work together:

### 1. Active Engagement Through Questioning (Socratic Method)

The Socratic Method pushes you to go beyond just consuming information. Through thoughtful questioning, you are encouraged to reflect, challenge assumptions, and dig deeper into the “why” and “how” of a topic. It promotes:

- **Critical Thinking**: Break down complex concepts by questioning every aspect.
- **Problem Solving**: Formulate your own answers by exploring different perspectives.
- **Self-Discovery**: Reveal gaps in your understanding that you might not have noticed.

### 2. True Mastery Through Teaching (Feynman Technique)

Once you’ve questioned and reflected, it’s time to teach the concept to yourself or others—simplifying and explaining it in the clearest terms possible, just as physicist Richard Feynman advocated. This technique emphasizes:

- **Clarity of Thought**: You don’t really know something until you can explain it simply. This approach forces you to simplify and clarify complex ideas.
- **Dealing with Confusion**: Identify areas of confusion and fill in the gaps by returning to the source material until you can explain it with confidence.
- **Application in Real Life**: By teaching or explaining the topic, you strengthen your ability to use the knowledge in practical, real-world scenarios.

### 3. Bridging Theory and Practice

While the Socratic Method gets you thinking deeply and asking the right questions, the Feynman Technique ensures you can articulate what you’ve learned in a way that truly makes sense to you—and others. Together, these methods:

- **Strengthen Understanding**: Questioning helps you break down ideas, and explaining helps you rebuild them in your mind.
- **Enhance Retention**: By actively participating and teaching, you cement your learning, making it easier to recall and apply later.
- **Encourage Curiosity and Continuous Growth**: You’ll always be motivated to explore new questions and refine your knowledge through teaching.

### 4. A Personalized Learning Journey

These methods adapt to any learner. Whether you’re a beginner or a subject-matter expert, the questions and explanations evolve with your growing understanding. This combination offers a powerful, dynamic way to master any topic—one that is driven by curiosity and self-reflection.

## Inquisitorial vs. Conversational Socrates: Two Modes of Inquiry

Within the Socratic Method, there are two distinct styles of questioning: **Inquisitorial Socrates** and **Conversational Socrates**, each suited for different learning scenarios.

### Inquisitorial Socrates: The Rigorous Challenger

This approach reflects the classic image of Socratic dialogue as a form of interrogation. Inquisitorial Socrates is designed to challenge assumptions and push learners toward deep, sometimes uncomfortable, realizations. In this mode:

- **The Role of the Questioner**: The questioner adopts a more dominant role, asking probing, sometimes aggressive questions intended to expose contradictions or flawed reasoning.
- **The Goal**: To strip away misunderstandings, leading to a clearer, more refined understanding of a topic.
- **Best For**: Advanced learners or situations where the learner needs to be pushed out of their intellectual comfort zone. It is a rigorous method for those seeking to sharpen their critical thinking under pressure.

### Conversational Socrates: The Gentle Guide

Conversational Socrates takes a more collaborative and exploratory approach. It mirrors a dialogue between equals, with the goal of discovering knowledge together through thoughtful discussion. In this mode:

- **The Role of the Questioner**: The questioner plays a supportive role, asking open-ended questions to guide the learner toward their own discoveries and insights.
- **The Goal**: To foster curiosity and personal reflection, helping the learner arrive at answers in their own time and on their own terms.
- **Best For**: Beginners or those looking for a more nurturing environment to explore ideas without feeling pressured. This method is ideal for creative, open-ended inquiry and encourages a learner’s natural curiosity.

By combining **Inquisitorial Socrates** for rigorous questioning with **Conversational Socrates** for collaborative exploration, and adding the **Feynman Technique** for simplifying and teaching, you can create a robust and versatile learning strategy that adapts to any subject or learner.
"""

st.markdown(markdown_text)