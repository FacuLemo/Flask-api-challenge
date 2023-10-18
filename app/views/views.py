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

from app.schemas.schemas import UserBasicSchema,CategorySchema

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
app.add_url_rule("/user/<user_id>", view_func=UserAPI.as_view('user_by_id'))

class CategoryAPI(MethodView):
    def get(self, category_id=None):
        if category_id is None:
            categ= Category.query.all()
            resultado = CategorySchema().dump(categ,many=True)
        else:
            categ= User.query.get(category_id)
            resultado= CategorySchema.dump(categ)
        return jsonify(resultado)
        
    def post(self):
        categ_json = CategorySchema().load(request.json)
        name= categ_json.get('name')
        new_categ = Category(name=name)
        db.session.add(new_categ)
        db.session.commit()
        return jsonify(CategorySchema().dump(new_categ))
    
    def put(self,category_id): #Cambiar contraseña
        categ_rename= User.query.get(category_id)
        categ_json = CategorySchema().load(request.json)
        newname= categ_json.get('name')
        categ_rename.password= newname
        db.session.commit()
        return jsonify(CategorySchema().dump(categ_rename))
    
    def delete(self,id):
        ctg = Category.query.get(id)
        db.session.delete(ctg)
        db.session.commit()
        return jsonify(mensaje=f"Borraste la categoria {id}")   #ctg.name probar


app.add_url_rule("/categories",view_func=CategoryAPI.as_view('categories'))
app.add_url_rule("/categories/<category_id>", view_func=CategoryAPI.as_view('category_by_id'))

@app.route('/')
def index():
    return jsonify(hola="anda")
