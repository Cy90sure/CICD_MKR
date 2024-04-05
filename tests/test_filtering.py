import pytest
import os
from main import read_file, filter_lines, write_filtered_lines, get_desktop_path

@pytest.fixture
def sample_file(tmpdir):
    filepath = os.path.join(tmpdir, 'test_file.txt')
    with open(filepath, 'w') as file:
        file.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        It has survived not only five centuries, but also the leap into electronic typesetting,
        remaining essentially unchanged.
        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
        and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")
    return filepath

def test_read_file(sample_file):
    lines = read_file(sample_file)
    assert len(lines) == 7

def test_filter_lines():
    lines = [
        "Lorem Ipsum is simply dummy text",
        "It was popularised in the 1960s",
        "This line does not contain the keyword"
    ]
    filtered_lines = filter_lines(lines, "Lorem")
    assert len(filtered_lines) == 1