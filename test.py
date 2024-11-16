import requests

# print(requests.get("example.com").text)


r = requests.get(
    "")
r = str(r.text)

counter = 0
tags = []
prev_loc = 0
length = len(r)
while "<img" in r:

    loc = r.find(f"""<img id="image-{}"""")
    if loc == -1 or prev_loc == loc:
        exit()
    tag = r[loc:loc + 4]
    loc = loc + 4
    while "/>" not in tag:
        loc += 1
        tag += r[loc]
        # print(tag)
    print(tag + f" count:{counter}/{length}")
    print("_" * 100)
    if counter > 1:
        print(len(tags))
        # if tags[counter-1] == tag:
        #     print("\nSame\n")
        #     pass

    prev_loc = loc
    tags.append(tag)
    r = r.replace(tag, " ", 1)
    counter += 1

print("*" * 100)
print(counter, "\n")
print(tags)

# print(r)
