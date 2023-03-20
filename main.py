from pokedex import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

pokemons = db.collection.find()
#for pokemon in pokemons: #printando ela
#    print(pokemon)

#dragon_aux = db.collection.find({"type": "Dragon"})
#writeAJson(dragon_aux, "pokemon_dragontype")

#pokemon = db.collection.find({"base.Attack": { "$gte": 140 }})
#writeAJson(pokemon, "highest_base_atck")

#pokemon = db.collection.find({"base.Defense": { "$gte": 110 },"base.HP": { "$gte": 50 }})
#writeAJson(pokemon, "best_tanks")

#pokemon = db.collection.find({"type": "Flying", "base.HP": { "$lte": 150 }})
#writeAJson(pokemon, "highHP_flying")

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})

mew = getPokemonByDex(151)
writeAJson(mew, "Mew")

