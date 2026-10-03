import argparse

from . import autoload_dir, install, uninstall


def main(argv=None):
    p = argparse.ArgumentParser(prog='vs-retinex-install',
                                description='Install the Retinex plugin into the VapourSynth autoload directory.')
    p.add_argument('action', nargs='?', choices=['install', 'uninstall'], default='install')
    p.add_argument('--dir', help='target directory (default: %s)' % autoload_dir())
    args = p.parse_args(argv)
    if args.action == 'install':
        print('Installed ' + str(install(args.dir)))
    else:
        print('Removed' if uninstall(args.dir) else 'Plugin was not installed')


if __name__ == '__main__':
    main()
