import re

css_file = '/home/quanglinh/Documents/Tiem_nam/Poseify-1.0.0/css/bootstrap.min.css'

with open(css_file, 'r') as f:
    content = f.read()

# Replace hex (case insensitive)
content = re.sub(r'#e41779', '#D4AF37', content, flags=re.IGNORECASE)

# Replace rgb
content = content.replace('rgb(228, 23, 121)', 'rgb(212, 175, 55)')
content = content.replace('rgb(228,23,121)', 'rgb(212,175,55)')
content = content.replace('rgba(228, 23, 121', 'rgba(212, 175, 55')
content = content.replace('rgba(228,23,121', 'rgba(212,175,55')

# Re-write the file
with open(css_file, 'w') as f:
    f.write(content)

print(f"Successfully replaced primary color in {css_file}")
