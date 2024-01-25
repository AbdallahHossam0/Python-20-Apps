import zipfile
import pathlib


def makeZip(filepaths, folder):
    destPath = pathlib.Path(folder, 'compressed.zip')
    with zipfile.ZipFile(destPath, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname= filepath.name)

