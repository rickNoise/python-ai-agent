# AI Agent in Python
A repo for boot.dev project "Build an AI Agent in Python".

## Build an AI Agent

If you've ever used Cursor or Claude Code as an "agentic" AI editor, you'll understand what we're building in this project.

We're building a toy version of Claude Code using Google's free Gemini API! As long as you have an LLM at your disposal, its actually surprisingly simple to build a (somewhat) effective custom agent.

## What Does the Agent Do?

The program we're building is a CLI tool that:

Accepts a coding task (e.g., "strings aren't splitting in my app, pweeze fix 🥺👉🏽👈🏽")
Chooses from a set of predefined functions to work on the task, for example:
Scan the files in a directory
Read a file's contents
Overwrite a file's contents
Execute the python interpreter on a file
Repeats step 2 until the task is complete (or it fails miserably, which is possible)
For example, I have a buggy calculator app, so I used my agent to fix the code:

```
> uv run main.py "fix my calculator app, its not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. T
```
