paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
d = {}
for path in paths:
    parts = path.split(" ")
    directory = parts[0]
    for file in parts[1:]:
        name, content = file.split("(")
        content = content[:-1]
        full_path = directory + "/" + name
        d.setdefault(content, []).append(full_path)
print([group for group in d.values() if len(group) > 1])