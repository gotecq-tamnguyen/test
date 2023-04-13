from sanic import Sanic
from sanic.response import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Pet
from sqlalchemy.ext.asyncio import create_async_engine

# run mysql with docker
# docker run --name mypet-db -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=pet_api mysql:latest
# Create a SQLAlchemy engine and session
engine = create_engine('mysql+mysqlconnector://root:secret@172.17.0.2/pet_api')
# engine = create_async_engine("mysql+aiomysql://root:secret-pw@172.17.0.2/pet_api", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()



app = Sanic(__name__)

# Define a middleware for handling database sessions
@app.middleware('request')
async def db_session_middleware(request):
    request.ctx.db = Session()

@app.middleware('response')
async def db_session_cleanup_middleware(request, response):
    if hasattr(request.ctx, 'db'):
        request.ctx.db.close()


# Define the API routes
@app.route('/pets', methods=['GET'])
async def get_pets(request):
    # Get all pets from the database
    session = request.ctx.db
    pets = session.query(Pet).all()
    return json([pet.to_dict() for pet in pets])



@app.route('/pets', methods=['POST'])
async def create_pet(request):
    # Create a new pet in the database
    session = request.ctx.db
    pet_data = request.json
    pet = Pet(**pet_data)
    session.add(pet)
    session.commit()
    return json({'message': 'Pet created successfully'})

# Add Swagger 
# from sanic_openapi import swagger_blueprint
# app.blueprint(swagger_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
