frutas = {"maçã": "vermelha",
          "banana": "amarela",
          "uva": "roxa"
}
print(frutas.keys())
print(frutas.values())
print(frutas.items())

frutas = {"maçã": ["vermelha", "verde"],
          "banana": ["amarela", "verde"],
          "uva": ["roxa", "verde"]}

print(frutas["maçã"])
print(frutas["banana"][0])
