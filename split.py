import os
import argparse


def split_file(file_path, chunk_size):
    base_name = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        chunk_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            chunk_name = f"{base_name}.part{chunk_num}"
            with open(chunk_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            print(f"Created {chunk_name}")
            chunk_num += 1


def merge_files(base_name):
    chunk_num = 1
    with open(base_name, 'wb') as outfile:
        while True:
            chunk_name = f"{base_name}.part{chunk_num}"
            if not os.path.exists(chunk_name):
                break
            with open(chunk_name, 'rb') as infile:
                outfile.write(infile.read())
            print(f"Merged {chunk_name}")
            chunk_num += 1
    print(f"Merged file saved as {base_name}")


def main():
    parser = argparse.ArgumentParser(description="Split or merge files")
    parser.add_argument('action', choices=['split', 'merge'], help="Action to perform")
    parser.add_argument('file_path', help="Path to the file to split or base name of files to merge")
    parser.add_argument('--chunk_size', type=int, default=20 * 1024 * 1024,
                        help="Chunk size in bytes for splitting (default: 20MB)")

    args = parser.parse_args()

    if args.action == 'split':
        split_file(args.file_path, args.chunk_size)
    else:
        merge_files(args.file_path)


if __name__ == "__main__":
    main()