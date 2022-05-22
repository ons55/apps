from fastapi import FastAPI
import services as _services


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Annonces immobilières"}

@app.get("/annonces")
async def all_annonces():
      return _services.get_all_posts()