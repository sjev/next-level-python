""" main entry point for {{cookiecutter.package_name}}. """

from {{cookiecutter.package_name}} import __version__

def main() -> None:
    """main entry point for {{cookiecutter.package_name}}."""
    print(f"Hello from {{cookiecutter.package_name}} version: {__version__}!")

if __name__ == "__main__":
    main()
