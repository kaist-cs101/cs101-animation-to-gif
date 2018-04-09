import os

def apply_to_template(**kwargs):
    f = open('template.html', 'r')
    cont = f.read()
    f.close()
    for key, value in kwargs.items():
        cont = cont.replace('<!--$%s$-->' % key, value)
    return cont

def main():
    filenames = [filename for filename in os.listdir('.') if filename.endswith('.gif')]
    code_lines = []
    for i, filename in enumerate(filenames):
        code_lines.append('<div class="item">')
        code_lines.append('<div class="title">')
        code_lines.append('<strong>%d.</strong> %s' % (i + 1, filename))
        code_lines.append('</div>')
        code_lines.append('<img src="./%s" />' % filename)
        code_lines.append('</div>')
    body = '\n'.join(code_lines)
    html = apply_to_template(body=body)
    f = open('index.html', 'w')
    f.write(html)
    f.close()

if __name__ == '__main__':
    main()
