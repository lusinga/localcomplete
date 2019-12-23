import os


def walkPrograms(dir, datafile, wildcard):
    exts = wildcard.split(" ")
    for root, subdirs, files in os.walk(dir):
        for name in files:
            for ext in exts:
                if name.endswith(ext):
                    print(root)
                    # print(subdirs)
                    print(name)
                    filename = os.path.join(root, name)
                    print(filename)
                    try:
                        f1 = open(filename, 'r', encoding='utf-8')
                        datafile.writelines(f1.readlines())
                    except UnicodeDecodeError:
                        continue
                    break


outfile = open('programs.data', 'w', encoding='utf-8')
wildcard = '.ts .js'
walkPrograms('C:\\working\\github\\vscode', outfile, wildcard)
