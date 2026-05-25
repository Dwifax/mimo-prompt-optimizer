#!/usr/bin/env python3
"""MiMo Prompt Optimizer - Improve your AI prompts."""
import os, argparse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def optimize(prompt, task="general"):
    r = client.chat.completions.create(model="mimo-v2.5-pro", messages=[
        {"role": "system", "content": "Prompt engineering expert. Analyze, improve, provide optimized version."},
        {"role": "user", "content": f"Task: {task}\nPrompt: {prompt}"}])
    return r.choices[0].message.content

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("prompt"); p.add_argument("--task", default="general")
    a = p.parse_args(); print(optimize(a.prompt, a.task))
