import csv


def export_json(path, payload):
    import json
    path.write_text(json.dumps(payload, indent=2))


def export_csv(path, rules):
    rows = [_flatten(rule) for rule in rules]
    keys = set(k for r in rows for k in r)

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def _flatten(d, parent="", out=None):
    if out is None:
        out = {}

    if isinstance(d, dict):
        for k, v in d.items():
            _flatten(v, f"{parent}.{k}" if parent else k, out)
    elif isinstance(d, list):
        out[parent] = "|".join(map(str, d))
    else:
        out[parent] = str(d)

    return out