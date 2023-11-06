import argparse
import zipfile
import hashlib

def calculate_zip_hash(zip_filename):
    """
    Calculate the hash of the contents of a zip file.
    """
    hash_obj = hashlib.sha256()
    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        for file_info in zip_file.infolist():
            with zip_file.open(file_info) as file:
                while True:
                    data = file.read(8192)
                    if not data:
                        break
                    hash_obj.update(data)
    return hash_obj.hexdigest()

def compare_zip_files(zip_file1, zip_file2):
    """
    Compare two zip files by calculating their hashes.
    """
    hash1 = calculate_zip_hash(zip_file1)
    hash2 = calculate_zip_hash(zip_file2)

    return hash1 == hash2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two zip files.")
    parser.add_argument("zip_file1", help="Path to the first zip file")
    parser.add_argument("zip_file2", help="Path to the second zip file")
    args = parser.parse_args()

    zip_file1 = args.zip_file1
    zip_file2 = args.zip_file2

    if compare_zip_files(zip_file1, zip_file2):
        print("The zip files are the same.")
    else:
        print("The zip files are different.")
