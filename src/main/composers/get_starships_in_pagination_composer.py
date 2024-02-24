from src.infra.swap_api_consumer import SwapiApiConsumer
from src.data.usecases.starships_list_collector import StarshipsListCollector
from src.presenters.controllers import StarshipsListCollectorController


def get_starships_in_pagination_composer():
    """_summary_

    Returns:
        _type_: _description_
    """

    infra = SwapiApiConsumer()
    use_case = StarshipsListCollector(api_consumer=infra)
    controller = StarshipsListCollectorController(starships_list_collector=use_case)

    return controller
