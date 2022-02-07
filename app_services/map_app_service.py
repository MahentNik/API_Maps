from services.i_map_service import IMapService
from domain.request import Request


class MapAppService:
    def __init__(self, map_service: IMapService):
        self.map_service = map_service

    def execute(self, request: Request):
        return self.map_service.get_map(request)
