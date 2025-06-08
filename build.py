import os

MODULES = [
    'core_prompt.md',
    'static_first.md',
    'methodology.md',
    'reporting_standard.md',
    'self_review.md'
]

OUTPUT = '.github/copilot-instructions.md'

if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)  # إضافة هذا السطر
    with open(OUTPUT, 'w', encoding='utf-8') as outfile:
        outfile.write('### AndroBountyAgent v2.0 - Unified Instruction\n\n')
        for module in MODULES:
            path = os.path.join(os.path.dirname(__file__), module)
            if os.path.isfile(path):
                with open(path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n---\n\n')
    print(f"Unified instruction generated to {OUTPUT}")
