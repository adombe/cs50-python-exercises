filename = input("File name: ")

types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

extension = "." + filename.lower().strip().split(".")[-1]

if extension in types:
    print(types[extension])
else:
    print("application/octet-stream")
