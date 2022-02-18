from flask import jsonify, make_response

def res(code,data,success,error):
    out = {
        "code": code,
        "data": data,
        "success": success,
        "error": error
    }

    return make_response(jsonify(out)), code


