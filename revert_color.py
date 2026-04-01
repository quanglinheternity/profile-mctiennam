import re

css_file = '/home/quanglinh/Documents/Tiem_nam/Poseify-1.0.0/css/bootstrap.min.css'

with open(css_file, 'r') as f:
    content = f.read()

# Replace hex (case insensitive) back to old color
content = re.sub(r'#D4AF37', '#e41779', content, flags=re.IGNORECASE)

# Replace rgb back
content = content.replace('rgb(212, 175, 55)', 'rgb(228, 23, 121)')
content = content.replace('rgb(212,175,55)', 'rgb(228,23,121)')
content = content.replace('rgba(212, 175, 55', 'rgba(228, 23, 121')
content = content.replace('rgba(212,175,55', 'rgba(228,23,121')

# Re-write the file
with open(css_file, 'w') as f:
    f.write(content)

print(f"Successfully reverted primary color in {css_file}")
