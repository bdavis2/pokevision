from urllib.request import urlopen
import requests
import json
mons_forms = json.loads(urlopen("https://raw.githubusercontent.com/bdavis2/pokevision/master/mons-forms.json").read())
mons = json.loads(urlopen("https://raw.githubusercontent.com/bdavis2/pokevision/master/mons.json").read())
failed_mons = []
i = 0
for m in mons_forms:
    if (type(m) == list):
        j = 0
        for m_ in m:
            url = "https://img.pokemondb.net/artwork/large/"+ m_ + ".jpg"
            r = requests.get(url)
            if r.status_code == 404:
                failed_mons.append(m_)
            else:
                with open('F:/Downloads/pokevision/' + str(i) + '_' + str(j) + '.jpg', 'wb') as f:
                    f.write(r.content)
            j+=1
    else:
        url = "https://img.pokemondb.net/artwork/large/"+ m + ".jpg"
        r = requests.get(url)
        if r.status_code == 404:
            failed_mons.append(m)
        with open('F:/Downloads/pokevision/' + str(i) + '.jpg', 'wb') as f:
            f.write(r.content)
    i+=1
print("failed mons:" , *failed_mons, sep = ", ")
