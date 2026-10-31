"""
奇点残响 · SINGULARITY ECHO —— 独立窗口版

用法：pythonw 奇点残响.pyw [页面文件名]
双击「开始游戏.bat」即可。
"""
import os
import shutil
import sys
import tempfile
import time

import webview

DEFAULT = "奇点残响-二代.html"
ALT = "奇点残响-键盘版.html"


def find_html(here, name=None):
    cands = []
    if name:
        cands.append(name)
    cands += [DEFAULT, ALT, "gravity-echo.html"]
    for n in cands:
        p = os.path.join(here, n)
        if os.path.exists(p):
            return p
    return None


def main():
    here = os.path.dirname(os.path.abspath(sys.argv[0] if sys.argv else __file__))
    want = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].lower().endswith(".html") else None
    html = find_html(here, want) or find_html(os.path.dirname(os.path.abspath(__file__)), want)
    if not html:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "没找到游戏页面文件。", "奇点残响", 0x30)
        return

    try:
        run_dir = os.path.join(tempfile.gettempdir(), "SingularityEchoRun")
        os.makedirs(run_dir, exist_ok=True)
        fresh = os.path.join(run_dir, "game-%d.html" % int(time.time() * 1000))
        shutil.copyfile(html, fresh)
        html = fresh
    except Exception:
        pass

    title = "奇点残响 · 键盘版" if "键盘" in (want or html) else "奇点残响 · SINGULARITY ECHO"
    kwargs = dict(width=1280, height=800, min_size=(960, 600),
                  background_color="#04050c", text_select=False, easy_drag=False)
    try:
        webview.create_window(title, html, maximized=True, **kwargs)
    except TypeError:
        webview.create_window(title, html, **kwargs)
    webview.start()


if __name__ == "__main__":
    main()
