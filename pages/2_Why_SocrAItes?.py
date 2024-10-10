import streamlit as st

st.set_page_config(
    page_title="Why should you use SocrAItes?",
    page_icon="icon.jpg",
)

st.image("icon.jpg", width=100)

markdown_text = """
# Unlock Your Inner Thinker with the Socratic Method

Are you ready to go beyond rote memorization and truly understand what you’re learning? The Socratic method transforms the way you think by challenging you to question, probe, and reflect. Here’s why it works:

1. **Active Participation**: Instead of passively receiving information, you’ll engage deeply with ideas. It’s not about getting the answer correctly, but about thinking critically and arriving at your own conclusions backed by reason.
2. **Deeper Understanding**: By asking open-ended questions, you peel back the layers of a topic. This method helps you identify gaps in your knowledge and strengthens your grasp of the subject matter.
3. **Sharpened Critical Thinking**: The Socratic method teaches you how to break complex ideas into manageable pieces, analyze them, and apply what you know and learn in new contexts. It’s perfect for problem-solving and innovation.
4. **Fosters Curiosity and Growth**: The method encourages you to be curious, to explore the unknown, and to never settle for surface-level understanding. With every question, you unlock new perspectives and possibilities.
5. **Personalized Learning**: It meets you where you are. Whether you’re a beginner or an expert, the questions evolve with your growing knowledge, making learning a dynamic, ongoing conversation.

In a world that often emphasizes quick results, the Socratic method gives you a powerful tool for lifelong learning. It builds your ability to think for yourself, collaborate effectively with others, and embrace the process of discovery. Wouldn’t you want a method that helps you master any topic by tapping into your natural curiosity?

Let’s rethink how we learn.
"""

st.markdown(markdown_text)