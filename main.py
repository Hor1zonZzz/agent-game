import subprocess

def run_agent_with_input(input_str):
    result = subprocess.run(
        ['python', 'agent.py', input_str],
        capture_output=True, text=True
    )
    return result.stdout

if __name__ == "__main__":
    with open('tasks/task1.txt', 'r', encoding='utf-8') as file:
        user_input = file.read().strip()
    output = run_agent_with_input(user_input)
    print("Agent output:", output)
