from pprint import pprint


def parse_file_line(line, files):
    dir_or_size, file_or_dirname = line.split(" ")

    if dir_or_size == "dir":
        dirname = file_or_dirname
        files[dirname] = None
    else:
        size, filename = dir_or_size, file_or_dirname
        files[filename] = size

    return files


def parse_input():
    with open("data.in") as f:
        data = f.read().splitlines()

    tree = {"/": None}
    current_dir = "/"
    for line in data:
        if line.startswith("$ cd"):
            _, argument = line.split(" ")[1:]
            if argument == "..":
                parent_dir = "/".join(current_dir.split("/")[:-1]) or "/"
                current_dir = parent_dir
            elif argument == "/":
                current_dir = "/"
            else:
                current_dir = (
                    f"{current_dir}/{argument}"
                    if current_dir != "/"
                    else f"/{argument}"
                )
        elif line.startswith("$ ls"):
            pass

        else:
            files = parse_file_line(line, tree.get(current_dir) or {})
            tree[current_dir] = files
    return tree


def find_dirs(tree, current_dir, dirs_size_map):
    files = tree.get(current_dir) or {}

    total_size = 0
    for name, size in files.items():
        if size is not None:
            total_size += int(size)
        else:
            dirname = f"{current_dir}/{name}" if current_dir != "/" else f"/{name}"
            total_size += find_dirs(tree, dirname, dirs_size_map)

    dirs_size_map[current_dir] = total_size
    return total_size


def find_smaller_dirs_total_size(size=100000):
    tree = parse_input()

    dirs_size_map = {}
    find_dirs(tree, "/", dirs_size_map)

    result = []
    for _, size in dirs_size_map.items():
        if size < 100000:
            result.append(size)

    return sum(result)


def find_smallest_dir_to_delete(total_space, required_space):
    tree = parse_input()

    dirs_size_map = {}
    find_dirs(tree, "/", dirs_size_map)

    sizes = [(size, dirname) for dirname, size in dirs_size_map.items()]
    sizes.sort()

    used_space = dirs_size_map["/"]
    space_to_delete = required_space - (total_space - used_space)

    for size, dirname in sizes:
        if size >= space_to_delete:
            return dirname, size


# part 1
print(find_smaller_dirs_total_size())

# part 2
print(find_smallest_dir_to_delete(70000000, 30000000))
