import openai
import os

def build_prompt(summary):
    """
    Formats the scanner summary into a prompt for the LLM
    """

    prompt = """
    You are an expert software documentarian. Given the following project information, generate a professional and production-level README.md file including project description, features, installation steps
    ,usage examples, and dependencies. Project structure and docstrings:

    """
    for module in summary["modules"]:
        mod_name = os.path.basename(module)
        prompt += f"- {mod_name}\n"
    if summary["docstrings"]:
        for d in summary['docstrings']:
            if d["type"] == "module":
                prompt += f" Module {d['name']}: {d['doc']}\n"
            elif d["type"] == "class":
                prompt += f"  Class {d['name']}: {d['doc']}\n"
            elif d["type"] == "function":
                prompt += f"  Function {d['name']}: {d['doc']}\n"
    if summary['requirements']:
        prompt += "\nDependencies:\n- " + "\n- ".join(summary['requirements']) + "\n"
    if summary.get('scripts'):
        prompt += "\nScripts/Entry points:\n- " + "\n- ".join(summary['scripts']) + "\n"
    prompt += "\nIf any important information is missing, mention it as a TODO or placeholder in the README.\n"
    return prompt

def generate_readme(summary):
    prompt = build_prompt(summary)
    # openai_api_key = "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"



    client = openai.OpenAI(api_key=openai_api_key)  # use OpenAI(api_key="...") for 1.x+
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes production-level README.md files."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
        max_tokens=2048
    )
    


    readme_content = response.choices[0].message.content
    return readme_content
