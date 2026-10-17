import os
import argparse
import shutil
import tempfile
from pathlib import Path

def copy_unique(source: Path, destination_dir: Path) -> Path:
    destination = destination_dir / source.name
    counter = 1

    while destination.exists():
        destination = destination_dir / (
            f"{source.stem} ({counter}){source.suffix}"
        )
        counter += 1

    shutil.copy2(source, destination)
    return destination


def copy_files(folderPath, destinationPath) -> None:
    for content in os.listdir(folderPath):
        contentPath = Path(folderPath) / content

        if contentPath.is_file():
            if contentPath.suffix:
                ext = contentPath.suffix.lstrip(".")
            else:
                ext = "no_extension"
            target_dir = Path(destinationPath) / ext
            target_dir.mkdir(parents=True, exist_ok=True)

            copy_unique(contentPath, target_dir)

        if contentPath.is_dir():
            copy_files(os.path.join(folderPath, content), destinationPath)


            
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Path to the source directory")
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Path to the destination directory (default: dist)",
    )
    args = parser.parse_args()
    source_dir = Path(args.source)
    destination_dir = Path(args.destination)


    if not source_dir.is_dir():
        parser.error(f"source directory does not exist: {source_dir}")
    if source_dir == destination_dir:
        parser.error("destination directory must not be the source directory")

    try:
        destination_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryFile(dir=destination_dir) as probe:
            probe.write(b"\0")
            probe.flush()
    except OSError as error:
        parser.error(
            f"cannot create or write to destination directory "
            f"'{destination_dir}': {error}"
        )

    try:
        copy_files(source_dir, destination_dir)
    except OSError as error:
        parser.error(f"failed to copy files: {error}")


if __name__ == "__main__":
    main()