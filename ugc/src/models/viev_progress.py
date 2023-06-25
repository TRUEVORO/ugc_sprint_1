from datetime import datetime
from uuid import UUID

from pydantic import Field

from .mixin import OrjsonMixin


class ViewProgressDto(OrjsonMixin):
    """View progress dto."""

    movie_id: UUID
    user_id: UUID
    viewed_frame: int
    event_time: datetime = Field(default_factory=datetime.now)
