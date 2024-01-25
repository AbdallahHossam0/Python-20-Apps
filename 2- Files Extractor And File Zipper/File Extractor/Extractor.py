import zipfile

def extract(archivePath, DirectoryPath):
    with zipfile.ZipFile(archivePath, 'r') as archive:
        archive.extractall(path= DirectoryPath)


