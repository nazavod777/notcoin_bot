from pythonmonkey import eval as js_eval


def eval_js(function: str) -> int | None:
    match function:
        case 'document.querySelectorAll(\'body\').length':
            return 1

        case 'window.location.host == \'clicker.joincommunity.xyz\' ? 129 : 578':
            return 129

    try:
        return int(js_eval(function))

    except Exception:
        return None
