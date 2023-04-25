

def create_schema(app, db):
    with app.app_context():
        db.create_all()
        print("Database Initialized")

# Create

# Read