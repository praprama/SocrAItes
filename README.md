# SocrAItes
Repository for the socraites project. In order to run this locally, create a file `.streamlit/secrets.toml` and add the following lines to it:

```
OPENAI_API_KEY="sk-proj-<truncated>"
LANGCHAIN_API_KEY="lsv2_pt_<truncated>"

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