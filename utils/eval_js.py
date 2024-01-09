from pythonmonkey import eval as js_eval


def eval_js(function: str) -> int | None:
    try:
        return int(js_eval(function))

    except Exception:
        return None
