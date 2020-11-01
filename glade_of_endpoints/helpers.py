"""Module containing helper functions. """

import json


def json_dumbs_ascii(obj):
    return json.dumps(obj, ensure_ascii=False)
