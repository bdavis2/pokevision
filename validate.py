def valdiate(mons):
    i = 0
    for n in mons:
      if(type(n) == list):
        for m in n:
          url = "https://img.pokemondb.net/artwork/large/"+ m + ".jpg"
          r = requests.get(url)
          if r.status_code == 404:
            print(url)
          i+=1
      else:
        url = "https://img.pokemondb.net/artwork/large/"+ n + ".jpg"
        r = requests.get(url)
        if r.status_code == 404:
          print(url)
        i+=1
      print(i)
    print('done')
