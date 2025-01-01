# -*- coding: utf-8 -*-

import logging

from pythontemplate.calendar_events import CalendarEvents


class TestCalendarEventsTests:
    def setUp(self) -> None:
        logging.basicConfig(
            filename="tests/data/cosycar.log",
            level="DEBUG",
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

    def tearDown(self) -> None:
        pass

    def test_instance_of_calendar_Event(self) -> None:
        events = CalendarEvents()
        assert isinstance(events, CalendarEvents)

    def test_add_next_test(self) -> None:
        assert True
