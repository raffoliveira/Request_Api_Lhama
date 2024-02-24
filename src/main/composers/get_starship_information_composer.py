from src.presenters.controllers.starship_information_collector_controller import StarshipInformationColectorController
from src.data.usecases.starship_information_collector import StarshipInformationCollector
from src.infra.swap_api_consumer import SwapiApiConsumer


def get_starship_information_composer():
    ''' Composer '''

    infra = SwapiApiConsumer()
    usecase = StarshipInformationCollector(infra)
    controller = StarshipInformationColectorController(usecase)

    return controller
