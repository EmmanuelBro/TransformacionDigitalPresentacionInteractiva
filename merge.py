import re

with open('old_index.html', 'r', encoding='utf-8') as f:
    old_content = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    current_content = f.read()

# 1. Get the CSS from old_content
old_css_match = re.search(r'<style>(.*?)</style>', old_content, re.DOTALL)
old_css = old_css_match.group(1)

# Extract the side-menu CSS from current_content
side_menu_match = re.search(r'/\* Side Menu \*/.*?(?=</style>)', current_content, re.DOTALL)
side_menu_css = side_menu_match.group(0) if side_menu_match else ''

# Combine CSS
new_css = old_css + "\n" + side_menu_css

# Replace CSS in current_content
current_content = re.sub(r'<style>.*?</style>', f'<style>\n{new_css}\n    </style>', current_content, flags=re.DOTALL)

# 2. Extract the 3 architectures from old_content
archs_match = re.search(r'(<!-- Slide 4: Arquitectura End-to-End -->\s*<section>.*?</section>.*?<!-- Slide 6: Azure AI Foundry Architecture \(Simplified High-Level\) -->\s*<section>.*?</section>)', old_content, re.DOTALL)
if not archs_match:
    archs_match = re.search(r'(<!-- Slide 4: Arquitectura End-to-End -->.*</section>)\s*\n\s*</div>\s*</div>\s*<div class="fixed', old_content, re.DOTALL) # broader catch

archs_html = archs_match.group(1) if archs_match else ''

# Read archs.html precisely
with open('archs.html', 'r', encoding='utf-8') as f:
    archs_html = f.read()

# Remove the single ARQUITECTURA slide from current_content
current_content = re.sub(r'<!-- ARQUITECTURA -->\s*<section>.*?</section>', archs_html, current_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(current_content)

print("Merge Python Script Completed")
