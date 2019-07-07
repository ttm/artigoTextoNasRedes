import os

tdir = '../tables/'
ff = os.listdir(tdir)

# no = [
#  'begin{flushleft}',
#  'Source: By the author',
#  'end{flushleft}',
# ]
# 
# for f in ff:
#     with open(tdir + f, 'r') as f_:
#         s = f_.readlines()
#         for n in no:
#             s = [l for l in s if n not in l]
#         f_.close()
#     with open(tdir + f, 'w') as f__:
#         f__.writelines(s)

for f in ff:
    with open(tdir + f, 'r') as f_:
        s = f_.readlines()
        for n in no:
            s = [l for l in s if n not in l]
    with open(tdir + f, 'w') as f__:
        f__.writelines(s)
