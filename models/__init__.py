from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association table for the many-to-many relationship between Roles and Permissions
role_permissions = db.Table('role_permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)

# Association table for the many-to-many relationship between Users and Roles
user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    roles = db.relationship('Role', secondary=user_roles, back_populates='users')

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    permissions = db.relationship('Permission', secondary=role_permissions, back_populates='roles')
    users = db.relationship('User', secondary=user_roles, back_populates='roles')

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=False)
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'), nullable=False)
    resource = db.relationship('Resource', backref=db.backref('permissions', lazy=True))
    operation = db.relationship('Operation', backref=db.backref('permissions', lazy=True))
    roles = db.relationship('Role', secondary=role_permissions, back_populates='permissions')