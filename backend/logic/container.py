from functools import lru_cache

from punq import Container, Scope

from infra.repository.room.inmemory import InMemoryRoomRepository
from infra.repository.room.interface import RoomRepository
from logic.commands.room import (
    ConnectToRoomCommand,
    ConnectToRoomCommandHandler,
    CreateRoomCommand,
    CreateRoomCommandHandler,
    LeaveRoomCommand,
    LeaveRoomCommandHandler,
)
from logic.mediator.eventmediator import EventMediator
from logic.mediator.mediator import Mediator


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(
        RoomRepository, InMemoryRoomRepository, scope=Scope.singleton
    )
    container.register(CreateRoomCommandHandler)
    container.register(ConnectToRoomCommandHandler)
    container.register(LeaveRoomCommandHandler)

    def init_mediator():
        mediator = Mediator()
        container.register(EventMediator, instance=mediator)
        mediator.register_command(
            CreateRoomCommand,
            [container.resolve(CreateRoomCommandHandler)],  # type: ignore
        )
        mediator.register_command(
            ConnectToRoomCommand,
            [container.resolve(ConnectToRoomCommandHandler)],  # type: ignore
        )
        mediator.register_command(
            LeaveRoomCommand,
            [container.resolve(LeaveRoomCommandHandler)],  # type: ignore
        )
        return mediator

    container.register(Mediator, factory=init_mediator)
    return container
