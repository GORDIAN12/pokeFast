from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import GenreURLChoices, PokeBase, PokeCreate, Pokemon, Evolucion
from contextlib import asynccontextmanager
from db import init_db, get_session 
from sqlmodel import Session, select

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app=FastAPI(lifespan=lifespan)
Bands = [
        {'id': 1, 'name': 'Bulbasaur', 'tipo1': "Planta",'tipo2':  "Veneno", 'evoluciones': [
            {'subname': 'Ivysaur', 'fecha_aparicion': '2001-12-28'},
            {'subname': 'Venusaur', 'fecha_aparicion': '2001-12-28'}
        ]},
        {'id': 2, 'name': 'Charmander', 'tipo1': ["Fuego"], 'tipo2': "", 'evoluciones': [
            {'subname': 'Charmeleon', 'fecha_aparicion': '2001-12-28'},
            {'subname': 'Charizard', 'fecha_aparicion': '2001-12-28'}
        ]},
        {'id': 3, 'name': 'Squirtle', 'tipo': "Agua", 'tipo2': "", 'evoluciones': [
            {'subname': 'Wartortle', 'fecha_aparicion': '2001-12-28'},
            {'subname': 'Blastoise', 'fecha_aparicion': '2001-12-28'}
        ]},
        {'id': 4, 'name': 'Pikachu', 'tipo1': "Electrico", "tipo2": "", 'evoluciones': [
            {'subname': 'Raichu', 'fecha_aparicion': '2001-12-28'}
        ]},
        {'id': 5, 'name': 'Sandshrew', 'tipo1': 'Tierra', 'tipo2': "", 'evoluciones': [
                {'subname': 'Sandslash', 'fecha_aparicion': '2001-12-28'}
        ]},
        {'id': 6, 'name': 'Sandshrew', 'tipo1': 'Tierra', 'tipo2': "", 'evoluciones': [
            {'subname': 'Sandslash', 'fecha_aparicion': '2001-12-28'}
        ]},

        {'id': 7, 'name': 'Tauros', 'tipo1': 'Normal', 'tipo2': "", 'evoluciones': []},
        {'id': 8, 'name': 'Lapras', 'tipo1': 'agua','tipo2': 'hielo', 'evoluciones': []}
]

@app.get("/pokemons")
async def bands(tipo: GenreURLChoices | None=None, q : Annotated[str | None, Query(max_length=10)] = None,
session: Session = Depends(get_session)
 ) -> list[Pokemon]:
    poke_list=session.exec(select(Pokemon)).all()
    if tipo:
        poke_list = [
            b for b in poke_list
            if tipo.value.lower() in [t.lower() for t in b.tipo]
        ]
    if q:
        poke_list = [
            b for b in poke_list if q.lower() in b.name.lower()
        ]
    return poke_list


"""
@app.get("/bands_evolve")
async def bands2(evoluciones: str | None=None, has_evolve:bool=False ) -> list[BandWithId]:
    band_list=[BandWithId(**b) for b in Bands]
    if evoluciones:
        band_list=[ b for b in band_list if any(t.lower() == evoluciones.value.lower() for t in b.evoluciones)]
    if has_evolve:
        band_list=[b for b in band_list if len(b.evoluciones) > 0]
    return band_list




@app.get("/bands/pokemon/{name}", status_code=206)
async def search_name(name: str) -> BandWithId:
    band=next((BandWithId(**r) for r in Bands if r["name"].lower() == name.lower()), None)
    if band==None:
        raise HTTPException(status_code=404, detail="error obtain pokemon name")
    return band
@app.get("/bands/poketipo/{tipo}")
async def funct_tipo(tipo: GenreURLChoices) -> list[BandWithId]:
    return [BandWithId(**n) for n in Bands if any(t.lower() == tipo.value.lower() for t in n["tipo"])]
"""

@app.get("/pokemons/{poke_id}", status_code=206)
async def funct_id(
        poke_id: Annotated[int, Path(title="the poke ID")],
        session: Session = Depends(get_session)
) -> Pokemon:
    pokemon=session.get(Pokemon, poke_id)
    if pokemon==None:
        raise HTTPException(status_code=404, detail="error obtain band_id")
    return pokemon
@app.post("/pokemons")
async def create_poke(
        poke_data: PokeCreate,
        session: Session=Depends(get_session)
        )-> Pokemon:
    pokemon=Pokemon(name=poke_data.name, tipo1=poke_data.tipo1, tipo2=poke_data.tipo2)
    session.add(pokemon)

    if poke_data.evoluciones:
        for evolucion in poke_data.evoluciones:
            evol_obj=Evolucion(subname=evolucion.subname, fecha_aparicion=evolucion.fecha_aparicion, band=pokemon)
            session.add(evol_obj)

    session.commit()
    session.refresh(pokemon)

    return pokemon

