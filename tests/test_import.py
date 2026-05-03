import vellum_lensed
from vellum_lensed.main_window import MainWindow


def test_version():
    assert vellum_lensed.__version__ == "0.1.0"


def test_main_window(qapp):
    window = MainWindow()
    assert window is not None
