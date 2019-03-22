import argparse
import pyqrcode

def qrcode(link, scale=8):
    url=pyqrcode.create(link)
    url.png('qrcode.png', scale=scale)

def main(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--link',
                        dest='link',
                        default=None,
                        help='insert a link')
    parser.add_argument('--scale',
                        dest='scale',
                        default=int(8),
                        help='scale of QR code')

    args, _ = parser.parse_known_args(argv)
    qrcode(link=args.link, scale=args.scale)

if __name__ == '__main__':
    main()
