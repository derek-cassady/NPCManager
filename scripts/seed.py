from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Operation

def populate_operations():
    operations = [
        {"name": "Create", "description": "Create a new resource."},
        {"name": "Read", "description": "Read or view a resource."},
        {"name": "Update", "description": "Update an existing resource."},
        {"name": "Delete", "description": "Delete a resource."},
        {"name": "Approve", "description": "Approve a pending resource."},
        {"name": "Reject", "description": "Reject a pending resource."},
        {"name": "Export", "description": "Export resource data."},
        {"name": "Import", "description": "Import resource data."},
        {"name": "Lock", "description": "Lock a resource for exclusive access."},
        {"name": "Unlock", "description": "Unlock a resource."},
        {"name": "Share", "description": "Share a resource with others."},
        {"name": "Audit", "description": "Audit resource access and changes."},
    ]
    for op_info in operations:
        op = Operation(**op_info)
        db.session.add(op)
    db.session.commit()