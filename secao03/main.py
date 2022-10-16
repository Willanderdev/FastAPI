from fastapi import FastAPI
#tratar excessão
from fastapi import HTTPException
from fastapi import status
from models import Banda

app = FastAPI()

Bandas = {
    1: {'Banda': "Angra",
        "músicos": ['Rafael', 'Kiko', 'Felipe Andreoli', 'Aquiles', 'Falaski'],
        "vertente": 'power metal'
        },
    2: {
        "Banda": "Almah",
        "músicos": ['Falaski', 'Felipe Andreoli', 'Marcelo Barbosa', 'Paulo', 'Aquiles'],
        "vertente": 'Power Metal'
    }
}

@app.get('/Bandas')
async def get_bandas():
    return Bandas


@app.get('/Bandas/{banda_id}')
async def get_banda(banda_id: int):
    try:    
        banda = Bandas[banda_id]
        return banda
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Banda não encontrada.'
        )

@app.post('/Bandas')
async def post_banda(banda: Banda):
    next_id:int = len(Bandas) + 1
    Bandas[next_id] = banda
    banda.id = next_id
    return banda

@app.put('/Bandas/{banda_id}')
async def put_banda(banda_id: int, banda: Banda):
    if banda_id in Bandas:
        Bandas[banda_id] = banda
        return banda
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, DETAIL=F'Não existe curso com id {banda_id}')
    

@app.delete('/Bandas/{banda_id}')
async def del_banda(banda_id:int):
    if banda_id in Bandas:
        del Bandas[banda_id]
        return Bandas
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, DETAIL=F'Não existe curso com id {banda_id}')
        
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)