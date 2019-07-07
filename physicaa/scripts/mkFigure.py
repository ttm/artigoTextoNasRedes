import os

tdir = '../../tables/SI2/'
ff = os.listdir(tdir)

fs = [i for i in ff if i.startswith('ks') and i.endswith('_.tex')]

t1 = ' p.} & '
t2 = ' i.} & '
pa = ' & {\\bf g.} & {\\bf p.} & '
ks = []
pis = []
phs = []
ihs = []

for f in fs:
    with open(tdir + f, 'r') as f_:
        s = f_.readlines()
        for l in s:
            if pa in l:
                continue
            if t1 in l:
                ls = l.split(' & ')
                pi = float(ls[-2])
                ph = float(ls[-1].split()[0])
            if t2 in l:
                ih = float(l.split()[-2])
        print(f, 'pi, ph ih', pi, ph, ih)
        ks.extend([pi,ph,ih])
        pis.append(pi)
        phs.append(ph)
        ihs.append(ih)

import pylab as p

# p.hist(pis, [0,1.22,1.95,max(pis)+1], color=['g','y','r'])

f=p.subplot(311)
N, bins, patches = p.hist(pis, [0,1.22,1.95,max(pis)], edgecolor='white', linewidth=1)
patches[0].set_facecolor('b')
patches[1].set_facecolor('g')
patches[2].set_facecolor('r')
p.xticks((0,1.22,1.95,max(pis)), (0, r'$l$', r'$L$', max(pis))) # , rotation='vertical')
p.ylabel('count')
p.ylim(0,100)
p.title('Distances between peripheral and intermediary sectors')

p.subplot(312)
N, bins, patches = p.hist(phs, [0,1.22,1.95,max(phs)], edgecolor='white', linewidth=1)
patches[0].set_facecolor('b')
patches[1].set_facecolor('g')
patches[2].set_facecolor('r')
p.xticks((0,1.22,1.95,max(phs)), (0,r'$l$',r'$L$', max(phs)))
p.ylabel('count')
p.ylim(0,100)
p.title('Distances between peripheral and hubs sectors')

p.subplot(313)
N, bins, patches = p.hist(ihs, [0,1.22,1.95,max(ihs)], edgecolor='white', linewidth=1)
patches[0].set_facecolor('b')
patches[1].set_facecolor('g')
patches[2].set_facecolor('r')
p.xticks((0,1.22,1.95,max(ihs)), (0,r'$l$',r'$L$', max(ihs)))
p.xlabel(r"$c' \rightarrow$")
p.ylabel('count')
p.ylim(0,100)
p.title('Distances between intermediary and hubs sectors')
p.subplots_adjust(left=0.1,bottom=0.09,right=0.99,top=0.94,hspace=0.66)
p.savefig('../figs/hists.png')
# N, bins, patches = ax.hist(data, edgecolor='white', linewidth=1)
# for i in range(0,3):
#     patches[i].set_facecolor('b')
# for i in range(3,5):    
#     patches[i].set_facecolor('r')
# for i in range(5, len(patches)):
#     patches[i].set_facecolor('black')
