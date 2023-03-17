import os 

from flask import Flask

def create_app(): # FUNCION QUE SE EJECUTA PRIMERO EN UNA APLICACION HECHA EN FLASK
    app= Flask(__name__)

    app.config.from_mapping(   #CONFIGURA A PARTIR DE LAS VARIBALES DE ENTORNO QUE VAMOS A TENER
        FROM_EMAIL = os.environ.get('FROM_EMAIL'),
        SENDGRID_KEY = os.environ.get('SENDGRID_API_KEY'),   #ACA SE OBTIENEN LAS VARIBALES DE ENTORNO #SENGRID_KEY ES UN SERVICIO DE CORREO # DENTRO SE COLOCA LA VARIABLE DE ENTORNO QUE EN ESTE CASO ES "SENDGRID_API_KEY"
        SECRET_KEY = os.environ.get('SECRET_KEY'),
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE = os.environ.get('FLASK_DATABASE'),
        DATABASE_PORT=os.environ.get('FLASK_DATABASE_PORT')
    )

    from . import db
    
    db.init_app(app)
    
    from . import mail
    
    app.register_blueprint(mail.bp)

    return app