import os

MODULES = [
    '1.core_prompt.md',
    '2.available_resources.md',  # Placed after core philosophy, before methodology
    '3.static_first.md',
    '4.methodology.md',
    '5.reporting_standard.md',
    '6.self_review.md'
]

OUTPUT = '.github/copilot-instructions.md'

if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as outfile:
        outfile.write('# AndroBountyAgent v2.0 - Unified Instruction\n\n')
        for module in MODULES:
            path = os.path.join(os.path.dirname(__file__), module)
            if os.path.isfile(path):
                with open(path, 'r', encoding='utf-8') as infile:
                    content = infile.read().strip()
                    if content:
                        outfile.write(content)
                        outfile.write('\n---\n\n')
                    else:
                        print(f"Warning: {module} is empty.")
            else:
                print(f"Error: {module} not found.")
    print(f"Unified instruction generated to {OUTPUT}")