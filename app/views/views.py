from flask import(
    jsonify,
    request,
)
from app import app, db
from flask.views import MethodView
from app.models.models import (
    User,
    Category,
    Post,
    Comment,
)

from app.schemas.schemas import UserBasicSchema

class UserAPI(MethodView):
    def get(self, user_id=None):
        if user_id is None:
            users= User.query.all()
            resultado = UserBasicSchema().dump(users,many=True)
        else:
            users= User.query.get(user_id)
            resultado= UserBasicSchema.dump(users)
        return jsonify(resultado)
        
    def post(self):
        user_json = UserBasicSchema().load(request.json)
        name= user_json.get('name')
        email= user_json.get('email')
        passw= user_json.get('password')
        image= user_json.get('image')
        new_user = User(name=name, email=email,
                        password=passw, image=image
                        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(UserBasicSchema().dump(new_user))
    
    def put(self,user_id): #Cambiar contraseña
        user_put= User.query.get(user_id)
        user_json = UserBasicSchema().load(request.json)
        passw= user_json.get('password')
        user_put.password= passw
        db.session.commit()
        return jsonify(UserBasicSchema().dump(user_put))
    
    def delete(self,id):
        usr = User.query.get(id)
        db.session.delete(usr)
        db.session.commit()
        return jsonify(mensaje=f"Borraste el user {id}")

app.add_url_rule("/user",view_func=UserAPI.as_view('user'))
app.add_url_rule("/user/<user_id>", view_func=UserAPI.as_view('user_por_id'))

@app.route('/')
def index():
    return jsonify(hola="anda")
