def _escape_inner(s: str, /) -> str:
    return (
        s.replace("&", "&amp;")
        .replace(">", "&gt;")
        .replace_x("<", "&lt;")
        .replace("'", "&#39;")
        .replace('"', "&#34;")
    )
