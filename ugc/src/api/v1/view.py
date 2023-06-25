from http import HTTPStatus
from typing import Annotated
from uuid import UUID

from aiokafka.errors import KafkaError
from fastapi import APIRouter, Depends, HTTPException, Path, Query

from core import ProducerError
from models import ViewProgressDto
from services import ViewService, get_view_service

router = APIRouter(
    prefix='/api/v1',
    tags=['view'],
)


@router.post(
    '/<{movie_id}:UUID>/view_progress',
    summary='Message about watching the film',
    description='Message about watching the film',
    response_model=None,
)
async def view_progress(
    movie_id: Annotated[UUID, Path(title='movie id', description='parameter - movie id')],
    user_id: Annotated[UUID, Query(title='user id', description='parameter - user id')],
    viewed_frame: Annotated[int, Query(title='value', description='parameter - viewed frame')],
    view_service: ViewService = Depends(get_view_service),
) -> HTTPStatus | HTTPException:
    try:
        data = ViewProgressDto(movie_id=movie_id, user_id=user_id, viewed_frame=viewed_frame)
        await view_service.produce(data)
    except KafkaError:
        return ProducerError()

    return HTTPStatus.OK
