import codecs
import os
import re

def init_directories():
    if not os.path.exists('./frames'):
        os.makedirs('./frames')
    if not os.path.exists('./gifs'):
        os.makedirs('./gifs')

def get_prefix():
    f = open('./templates/code_prefix.py', 'r')
    s = f.read()
    f.close()
    return s

def get_suffix():
    f = open('./templates/code_suffix.py', 'r')
    s = f.read()
    f.close()
    return s

def main():
    filenames = os.listdir('./sources')
    for filename in filenames:
        if not filename.endswith('.py'):
            continue
        student_ids = re.findall(r'[0-9]{8}', filename)
        new_filename = 'src_%s.py' % ('_'.join(student_ids))

        if os.path.exists('./gifs/%s.gif' % new_filename):
            continue

        if not student_ids:
            student_ids = ['unknown']


        try:
            source_file = codecs.open('./sources/%s' % filename, 'r', errors='replace', encoding='utf-8')
            code = source_file.read()
            source_file.close()
        except UnicodeDecodeError:
            source_file = codecs.open('./sources/%s' % filename, 'r', errors='replace', encoding='cp949')
            code = source_file.read()
            source_file.close()

        new_code = '%s\n%s\n%s' % (get_prefix(), code, get_suffix())

        new_file = open('./converted/%s' % new_filename, 'w')
        new_file.write(new_code)
        new_file.close()

        # Run converted code.
        os.system('python3 ./converted/%s' % new_filename)

if __name__ == '__main__':
    main()
