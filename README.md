# 📚 readme-agent

> **“Effective solutions don’t have to be complex.”**  
> Auto-generate professional, contextual README.md files for any Python project or Jupyter notebook—with just one command.

---

![image](https://github.com/user-attachments/assets/b6b66569-9de7-4716-8e36-52be65720c5c)


---

## 🚀 Why readme-agent?

Writing and maintaining good README files is tedious—especially for fast-moving or research-heavy projects.  
**readme-agent** takes the grunt work out of documentation by scanning your code and notebooks, then leveraging LLMs to create a rich, customized README for you.

- ✨ **Supports Python files and Jupyter Notebooks out of the box**
- ⚡ **Fast, local, and privacy-friendly**
- 🧠 **Uses LLMs to summarize your code, dependencies, and usage**
- 🖊️ **Flexible: easily add more file types or templates**
- 🪄 **Perfect for solo devs, data scientists, and teams**

---

## 📦 Installation

```bash
pip install readme-agent
```
## 🏁 Quick Start
1.Get your OpenAI API key
2. Navigate to your project directory (or use any repo path)
3. 
Run:
```bash
readme-agent generate --repo . --openai-key <your-openai-key>
```
The tool will:

- Scan your repo for Python and Jupyter files
- Preview the generated README
- Show a diff if README already exists
- Ask for confirmation before overwriting

---

## 💡 Example

```bash
readme-agent generate --repo ~/projects/awesome-ml --openai-key sk-...
```
## 📝 Features

- 🧩 **Understands Python code structure:** modules, classes, functions, docstrings
- 📓 **Smartly parses Jupyter Notebooks:** extracts summaries and code samples
- 🕵️ **Detects requirements:** finds dependencies from `requirements.txt`, etc.
- 🔄 **Shows a diff** before overwriting existing README.md
- ✍️ **LLM-powered:** uses GPT or your own LLMs for fluent, high-level summaries

---

## 🛣️ Roadmap

- [x] Python + Notebook support
- [ ] Customizable README templates
- [ ] Support for `requirements.txt`, `setup.py`, `pyproject.toml`
- [ ] Web UI and drag-and-drop mode
- [ ] More languages (JS/TS, R, etc.)
- [ ] Plugin API for power users

---

## 🤖 Why Not Another “Cool Agent?”

Lots of tools call themselves agentic these days for hype.  
**readme-agent** is built for real developer needs—**no unnecessary complexity, just results**.  
Because life is too short for writing repetitive docs.

---

## 📣 License

[MIT](./LICENSE) — free for personal and commercial use.

---

## 🌟 Spread the Word

If this saved you time, please star ⭐ the repo and share with your team or on social media!

---

*Built by [Tanmay Joshi](https://www.linkedin.com/in/tanmay-joshi/) & community.  
More features coming soon—stay tuned!*
