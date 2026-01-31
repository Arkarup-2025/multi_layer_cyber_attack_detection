from flask import session, jsonify

def admin_required():
    if "user_id" not in session or not session.get("is_admin"):
        return False
    return True
