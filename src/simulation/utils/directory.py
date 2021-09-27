import os


def create_dir(out: str) -> str:
    file_name = out.split('/')[-1]
    path = os.path.join('./out', out.replace(file_name, ''))
    if not os.path.isdir(path):
        os.makedirs(path)
    return f"{path}/{file_name}"
