import sys
import yaml
from pathlib import Path

from cookiecutter.main import cookiecutter

TEMPLATE_DIR = str(Path(__file__).parent.parent)
CONTEXT_FILE = Path(__file__).parent / "context.yaml"

with open(CONTEXT_FILE) as file_handler:
    content = yaml.safe_load(file_handler)

EXAMPLE_CONTEXT = content["default_context"]
PROJECT_NAME = EXAMPLE_CONTEXT["project_name"]


def test_generate_new_project(tmp_path: Path):
    path_to_new_project = cookiecutter(
        TEMPLATE_DIR,
        no_input=True,
        extra_context=EXAMPLE_CONTEXT,
        output_dir=tmp_path.as_posix(),
    )
    print(f"project generated in {path_to_new_project}")
    dest = (tmp_path / PROJECT_NAME).absolute().as_posix()
    print(f"{dest=}")
    assert str(path_to_new_project) == dest


if __name__ == "__main__":

    try:
        dest_path = Path(sys.argv[1])
        test_generate_new_project(dest_path)
    except IndexError as e:
        print("Please provide destination path")
