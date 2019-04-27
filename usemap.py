hoge = [
  {
    'name': 'Taro',
    'age' : 24,
  },
  {
    'name': 'Goro',
    'age' : 25,
  },
  {
    'name': 'Jiro',
    'age' : 32,
  }
]

age_map = map(lambda x: x['age'], hoge)
print(age_map)

age_comprehension = [p['age'] for p in hoge]
print(age_comprehension)
