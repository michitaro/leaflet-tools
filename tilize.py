from PIL import Image
import argparse
import numpy
import os
import logging ; logging.basicConfig(level=logging.INFO)


TILESIZE = 256


def main():
    parser = argparse.ArgumentParser(description='split a large image into tiles')
    parser.add_argument('--out', '-o', required=True, help='output directory')
    parser.add_argument('src', help='srouce image to be splitted')
    args = parser.parse_args()

    img = Image.open(args.src)
    arr = numpy.asarray(img)

    zi = max_level(max(arr.shape[0], arr.shape[1]))
    while zi >= 0:
        for yi in range((arr.shape[0] - 1) // TILESIZE + 1):
            os.makedirs(f'{args.out}/{zi}/{yi}', exist_ok=True)
            for xi in range((arr.shape[1] - 1) // TILESIZE + 1):
                out = f'{args.out}/{zi}/{yi}/{xi}.png'
                logging.info(f'{out}...')
                tile = arr[yi * TILESIZE:(yi + 1) * TILESIZE, xi * TILESIZE:(xi + 1) * TILESIZE]
                tile = pad(tile)
                tile = numpy.array(tile, dtype='uint8')
                Image.fromarray(tile).save(out)
        arr = half(arr)
        zi -= 1


def test(f):
    if os.environ.get('TEST'):
        f()


def half(a):
    a = a[:a.shape[0] // 2 * 2, :a.shape[1] // 2 * 2]
    a = a.reshape((a.shape[0] // 2, 2, a.shape[1] // 2, 2, -1)).sum(axis=(1,3)) // 4
    return a


def pad(a):
    if a.shape[0] != TILESIZE or a.shape[1] != TILESIZE:
        t = numpy.zeros((TILESIZE, TILESIZE, a.shape[2]))
        t[:a.shape[0], :a.shape[1]] = a
        return t
    return a


def max_level(d):
    d -= 1
    d //= TILESIZE
    z = 0
    while d != 0:
        d //= 2
        z += 1
    return z


@test
def max_level_test():
    assert max_level(256) == 0
    assert max_level(257) == 1
    assert max_level(512) == 1
    assert max_level(513) == 2


if __name__ == '__main__':
    if not os.environ.get('TEST'):
        main()
