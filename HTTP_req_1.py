import json
import requests


def hero_id_request(name_hero):
    url = "https://superheroapi.com/api/2619421814940190"
    url += f"/search/{name_hero}"
    # params = {"name": name_hero}
    params = None
    headers = {"Authorization": "2619421814940190"}
    response = requests.get(url=url, params=params, headers=headers, timeout=5)
    response.raise_for_status()
    if response.status_code != 200:
        print("Something went wrong!")
    return response


if __name__ == '__main__':
    heroes_name_list = ["Hulk", "Captain America", "Thanos"]
    max_intelligence_level = -1
    the_smart_hero = {'name': None, 'intelligence': None}

    for hero_name in heroes_name_list:
        resp = hero_id_request(hero_name)
        json_data = json.loads(resp.text)
        heroes_list = json_data['results']

        for hero in heroes_list:
            if hero['name'] == hero_name:
                # print(hero['powerstats']['intelligence'])
                hero_intelligence_level = int(hero['powerstats']['intelligence'])
                if hero_intelligence_level > max_intelligence_level:
                    max_intelligence_level = hero_intelligence_level
                    the_smart_hero['name'] = hero_name
                    the_smart_hero['intelligence'] = hero_intelligence_level

    print(f"Имя героя: {the_smart_hero['name']}. Уровень интеллекта: {the_smart_hero['intelligence']}")
