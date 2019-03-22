import argparse
import pyqrcode

def qrcode(link, scale=8):
    url=pyqrcode.creat(link)
    url.png('qrcodes/qrcode.png', scale=scale)

def main(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--link',
                        dest='link',
                        default=None,
                        help='insert a link')
    args, _ = parser.parse_known_args(argv)
    qrcode(args.link)

if __name__ == '__main__':
    main()
