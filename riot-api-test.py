import json
import requests




class ChampionInfo:

    def __init__(self, champion):
        self.champion = champion

    def get_champion_stats(self):
        """ Get champion stats and info """

        url = f'http://ddragon.leagueoflegends.com/cdn/10.9.1/data/en_US/champion/{self.champion}.json'
        get_champion_info = requests.get(url).content.decode("utf-8")
        champion_info = json.loads(get_champion_info)

        base_stats = champion_info['data'][self.champion]['info']
        stats = champion_info['data'][self.champion]['stats']
        abilities = champion_info['data'][self.champion]['spells']

        return base_stats, stats, abilities  # TODO: format results

    # def get_free_rotation(self):
    #     """ Find the free champion rotation (rank 10 and up) """
    #     get_champion_info = requests.get(self.url).content.decode("utf-8")
    #     free_rotation_json = json.loads(get_champion_info)
    #     return free_rotation_json.get("freeChampionIds")



def main():
    champion = input(str('what champions stats do you want to see? '))
    c = ChampionInfo(champion.lower().capitalize())
    print(c.get_champion_stats())


main()
