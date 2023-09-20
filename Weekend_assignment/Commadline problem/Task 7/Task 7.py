import difflib

def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1:
            file1_lines = f1.readlines()

        with open(file2, 'r') as f2:
            file2_lines = f2.readlines()

        differ = difflib.Differ()
        diff = list(differ.compare(file1_lines, file2_lines))

        added_lines = [line[2:] for line in diff if line.startswith('+ ')]
        modified_lines = [line[2:] for line in diff if line.startswith('? ')]
        deleted_lines = [line[2:] for line in diff if line.startswith('- ')]

        return added_lines, modified_lines, deleted_lines

    except FileNotFoundError:
        print("One or both files not found.")
        return [], [], []

    except Exception as e:
        print("An error occurred:", e)
        return [], [], []


file1_path = "/content/file1.txt"
file2_path = "/content/file2.txt"
added, modified, deleted = compare_files(file1_path, file2_path)

print("Added Lines:")
print("\n".join(added))
print("\nModified Lines:")
print("\n".join(modified))
print("\nDeleted Lines:")
print("\n".join(deleted))