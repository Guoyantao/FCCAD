

from __future__ import print_function
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def check_images():
    count = 0
    all_seqs = np.load('/home/annus/PycharmProjects/mnist_test_seq.npy', mmap_mode='r').transpose(1,0,2,3)
    check = all_seqs[0]
    for i in range(5):
        for j in range(4):
            count += 1
            plt.subplot(5, 4, count)
            plt.axis('off')
            plt.imshow(check[count-1,:,:])
    plt.show()
    pass


def gen_sequence():
    all_seqs = np.load('/home/annus/PycharmProjects/mnist_test_seq.npy', mmap_mode='r').transpose(1,0,2,3)
    check = all_seqs[np.random.randint(0,all_seqs.shape[0])] # get one random image sequence out
    # here ims is a list of lists, each row is a list of artists to draw in the
    # current frame; here we are just animating one artist, the image, in
    # each frame
    ims = []
    fig = plt.figure()
    for i in range(check.shape[0]):
        im = plt.imshow(check[i], animated=True)
        print(np.unique(check[i]))
        ims.append([im])
    ani = animation.ArtistAnimation(fig, ims, interval=80, blit=True, repeat_delay=0)
    plt.show()
    pass


if __name__ == '__main__':
    gen_sequence()




