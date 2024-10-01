# SocrAItes

## Introduction

This is a project being worked upon as part of the [Google Gen AI Exchange Hackathon](https://cloud.google.com/resources/gen-ai-exchange). The specific problem statement being worked upon is provided by Blume Ventures.

## Video demo
Coming soon!

## Problem statement

Develop a Gen AI powered tool to make a teaching assistant to teach a student using the Socratic teaching method. The Socratic method is where the assistant asks probing questions and leads the student to the answer instead of revealing the answer. Given this is a hard problem, we want to restrict it to one particular topic viz. Learning of Data Structures and Algorithms. Feel free to narrow it down even further if it helps make a high-quality assistant e.g. only for Algorithms of Sorting. That is a topic that should be familiar to most software engineers working on this. As an example, if a test-case times out, the assistant shouldn’t just say: “It timed out because it was a large input size”. It should first pick the right question to ask the student e.g. “What can you say about the difference between this test-case and the other test-cases that passed?” Then depending on what answer the student gives, ask the next relevant question, eventually making the student see that this test-case is quite large and some particular section of their code timed out processing that size. Hence that section needs to be optimized. Several studies have shown that the Socratic method of teaching is very effective for learning, but it is very challenging to scale for any commercial viability anywhere in education, because of a. limited supply of effective teachers who can do this and b. it is not very effective in 1xMany teaching, needing it to be 1x1. AI assistants have the potential to overcome both of these challenges.

## Solution

Our solution to the problem statement is **SocrAItes**. In essence, it's an AI powered assistant that enables learners of any age or experience learn at their own speed. It encourages learners to break down topics and concepts that they are struggling with into more easy to understand chunks. Not only does it use Socratic thinking as outlined in the problem statement, it also provides a summary of the entire learning experience to the user leveraging the power **Feynman** notes concept. 

## Feature roadmap

One of the key features the team is looking to build is to create a second assistant that guides learners through the process of taking effective notes following Richard Feynman's techniques. We will be using "Check for Understanding" questions that will take the users step-by-step through the process.

## Access to SocrAItes

You can access the tool here - https://socraites-yjgeqnfwor3t6wzsgqxtqn.streamlit.app/. If you are interested in trying this out, please reach out to the authors below.

## To run it locally
Repository for the socraites project. In order to run this locally, create a file `.streamlit/secrets.toml` and add the following lines to it:

```
OPENAI_API_KEY="sk-proj-<truncated>"
LANGCHAIN_API_KEY="lsv2_pt_<truncated>"
SOCRAITES_ASST="<assistant_id>"
FAINMAN_ASST="<assistant_id>"
MONGO_URL="<MONGO_CONNECTION_URL>"

[passwords]
username = "password"

[roles]
username = "<user|admin>"
```
Each line under `[passwords]` represents a username and its password. Add multiple lines as required. Make sure to set complex password.
Each username should also have a role defined under `[roles]`. The value can either be `user` or `admin`. Only `admin` users get the ability to change the system instructions.

Before running your app, install the requirements using `pip install -r requirements.txt`.

Run the app using `streamlit run SocrAItes.py`. 

NOTE: You need to create an assistant on OpenAI and replace the assistant ID in the 2 streamlit files.

## Authors
Prapanch Ramamoorthy - prap.ram@gmail.com
Atri Basu - mailbasuatri@gmail.com
Bhavik Shah - bhavikt2012@gmail.com