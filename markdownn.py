#the below code is used to convert html content to markdown using markdownify
import markdownify
with open('text1.txt', 'r') as file:
    html = file.read()
h = markdownify.markdownify(html, heading_style="ATX")
print(h)
