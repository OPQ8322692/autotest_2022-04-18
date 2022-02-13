import pytest
from config import conf
import os

if __name__ == '__main__':
    report_path = conf.get_report_path() + os.sep + "result"
    report_html_path = conf.get_report_path() + os.sep + "html"
    pytest.main(["-s","--alluredir", report_path])