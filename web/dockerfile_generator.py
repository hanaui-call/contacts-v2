if __name__ == "__main__":
    dockerfile = '''FROM python:3.7
RUN pip install --upgrade pip
'''
    for l in open('requirements.txt'):
        l = l.strip()
        if not l or l.startswith('#'):
            continue
        dockerfile += "RUN pip install {}\n".format(l)

    dockerfile += '\nWORKDIR /app\n'
    with open('Dockerfile', 'w') as file :
        file.write(dockerfile)
