from PIL import Image
import numpy
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('--out', '-o', required=True)
    parser.add_argument('--blank', type=eval, default=numpy.array([255, 255, 255, 255]))
    args = parser.parse_args()

    isnan = None

    img = Image.open(args.file)
    arr = numpy.asarray(img).copy()
    arr[arr[:, :, 3] == 0] = args.blank

    blank = (arr == args.blank).all(axis=2)

    blank_y = numpy.all(blank, axis=1)
    blank_x = numpy.all(blank, axis=0)

    ok_y = numpy.where(numpy.logical_not(blank_y))[0]
    ok_x = numpy.where(numpy.logical_not(blank_x))[0]

    min_y, max_y = ok_y[0], ok_y[-1]
    min_x, max_x = ok_x[0], ok_x[-1]
    len_y = max_y - min_y
    len_x = max_x - min_x

    print('(min_x, min_y), (max_x, max_y) = (%d, %d), (%d, %d)' % (min_x, min_y, max_y, max_x))

    arr = arr[min_y : min_y + len_y, min_x : min_x + len_x]

    Image.fromarray(arr).save(args.out)


if __name__ == '__main__':
    main()
