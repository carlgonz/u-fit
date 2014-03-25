import os

files = os.listdir('.')
exclude = list(range(0, 16)) + [17, ]

print("Starting with {0} files...".format(len(files)))

for filename in files:
    print("\t{0}".format(filename))

    if not ".csv" in filename:
        print("\t\tExcluded")
        continue

    f_in = open(filename, 'r')
    f_out = open("out/{0}".format(filename), 'w')

    for i, line in enumerate(f_in):
        if i in exclude:
            continue
        f_out.write(line)

    f_in.close()
    f_out.close()

    print("\t\tOk")

print("End")
