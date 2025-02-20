import hashlib

def get_file_hash(file_path, hash_algo='sha256'):
    hash_func = hashlib.new(hash_algo)
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):    #4096 is used to read file upto 4kB
            hash_func.update(chunk)
    return hash_func.hexdigest()

def compare(pdf1, pdf2):
    hash1 = get_file_hash(pdf1)
    hash2 = get_file_hash(pdf2)
    return hash1 == hash2

# Example usage
pdf1 = 'copy file path'
pdf2 = 'Copy second File path'

if compare(pdf1, pdf2):
    print("The PDFs are identical.")
else:
    print("The PDFs are different.")
