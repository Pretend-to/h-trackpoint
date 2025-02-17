from fastapi_boot.core import Controller,  Post, Get, use_dep

from dao.data.project_stat import DataDAO
from dependencies import use_login
from domain.vo.common import BaseResp

from domain.entity.project import Project
from domain.entity.record import Record
from domain.vo.data.project_stat import ProjectStatVO


@Controller('/v1/data/project-stat', tags=['项目数据统计'])
class DataController:
    user = use_dep(use_login)

    def __init__(self, data_dao: DataDAO) -> None:
        self.data_dao = data_dao

    # @Get('/base-stat', summary='获取基本统计信息', response_model=BaseResp[BaseStatVO])
    # async def get_base_stat(self):
    #     vo = BaseStatVO(client_list=await self.data_dao.get_client_list_by_user_id(self.user.id))
    #     return BaseResp[BaseStatVO].ok(data=vo)

    @Get(summary='获取项目统计信息', response_model=BaseResp[list[ProjectStatVO]])
    async def get_project_stat(self):
        vo = await self.data_dao.getProjectEventStat(self.user.id)
        return BaseResp[list[ProjectStatVO]].ok(data=vo)

    # @Get('/event-stat', summary='获取事件统计信息', response_model=BaseResp[list[EventStatVO]])
    # async def get_event_stat(self):
    #     vo = await self.data_dao.getProjCountGroupByEvent(self.user.id)
    #     return BaseResp[list[EventStatVO]].ok(data=vo)
