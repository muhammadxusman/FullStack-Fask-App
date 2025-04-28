class Config:
    SECRET_KEY = 'yoursecretkey123'  # for session and cookies
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/fullstack_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

