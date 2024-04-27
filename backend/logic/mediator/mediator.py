from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Iterable

from domain.events.base import BaseEvent
from logic.commands.base import (
    BaseCommand,
    BaseCommandHandler,
)
from logic.events.base import BaseEventHandler
from logic.mediator.eventmediator import EventMediator


@dataclass
class Mediator(EventMediator):
    commands_map: dict[type[BaseCommand], list[BaseCommandHandler]] = field(
        default_factory=lambda: defaultdict(list)
    )

    events_map: dict[type[BaseEvent], list[BaseEventHandler]] = field(
        default_factory=lambda: defaultdict(list)
    )

    def register_event(
        self,
        event: type[BaseEvent],
        event_handlers: Iterable[BaseEventHandler],
    ):
        self.events_map[event].extend(event_handlers)

    def register_command(
        self,
        command: type[BaseCommand],
        command_handlers: Iterable[BaseCommandHandler],
    ):
        self.commands_map[command].extend(command_handlers)

    def publish_events(self, event: list[BaseEvent]): ...

    def handle_command(self, command: BaseCommand) -> list[Any]:
        command_type = command.__class__
        print(123)
        return [
            handler.handle(command)
            for handler in self.commands_map[command_type]
        ]
