# p2app/engine/main.py
#created by Johnny Do
#johnnyhd@uci.edu
#46849652
# ICS 33 Spring 2023
# Project 2: Learning to Fly
#
# An object that represents the engine of the application.
#
# This is the outermost layer of the part of the program that you'll need to build,
# which means that YOU WILL DEFINITELY NEED TO MAKE CHANGES TO THIS FILE.
import p2app.events.database as database
import p2app.events.app as app
import p2app.events.continents as continents
import sqlite3
import p2app.engine.continent_events as continent_events
import os



    # Send ContinentSearchResultEvents for each continent found
class Engine:
    """An object that represents the application's engine, whose main role is to
    process events sent to it by the user interface, then generate events that are
    sent back to the user interface in response, allowing the user interface to be
    unaware of any details of how the engine is implemented.
    """

    def __init__(self):
        """Initializes the engine"""
        self._conn = sqlite3.connect('user', isolation_level = None)
        self.path = None


    def process_event(self, event):
        """A generator function that processes one event sent from the user interface,
        yielding zero or more events in response."""
        if isinstance(event, database.OpenDatabaseEvent):
            try:
                path = event._path
                self.path = event._path
                file_extension = os.path.splitext(path)[1]
                if file_extension != '.db':
                    yield database.DatabaseOpenFailedEvent('This is not a .db or database file')
                else:

                    self._conn = sqlite3.connect(path, isolation_level = None)
                    cursor = self._conn.execute('PRAGMA foreign_keys = ON;')
                    cursor.close()
                    yield database.DatabaseOpenedEvent(self.path)
            except:
                yield database.DatabaseOpenFailedEvent('This is not a .db or database file')
        elif isinstance(event, app.QuitInitiatedEvent):
            try:
                yield app.EndApplicationEvent()
            except:
                error = app.ErrorEvent('Cannot quit right now')
                yield error
        elif isinstance(event, database.CloseDatabaseEvent):
            try:
                yield database.DatabaseClosedEvent()
            except:
                error = app.ErrorEvent('Cannot close right now')
                yield error
        elif isinstance(event, continents.StartContinentSearchEvent):
            try:
                results = continent_events.search_continents(self._conn, event)
                for result in results:
                    continent = continents.Continent(*result)
                    yield continents.ContinentSearchResultEvent(continent)
            except:
                error = app.ErrorEvent('No continents that match')
                yield error
        elif isinstance(event, continents.LoadContinentEvent):
            try:
                results = continent_events.load_continents(self._conn, event)
                for result in results:
                    continent = continents.Continent(*result)
                    yield continents.ContinentLoadedEvent(continent)
            except:
                error = app.ErrorEvent('Cannot Load the continent')
                yield error
        elif isinstance(event, continents.SaveNewContinentEvent):
            try:
                new_cont = continent_events.new_continent(self._conn, event)
                yield continents.ContinentSavedEvent(new_cont)
            except:
                yield continents.SaveContinentFailedEvent('Check your continent code it has to be unique')
        elif isinstance(event, continents.SaveContinentEvent):
            try:
                save_cont = continent_events.edited_continent(self._conn, event)
                yield continents.ContinentSavedEvent(save_cont)
            except:
                yield continents.SaveContinentFailedEvent(
                    'Check your continent code it has to be unique')


        # This is a way to write a generator function that always yields zero values.
        # You'll want to remove this and replace it with your own code, once you start
        # writing your engine, but this at least allows the program to run.

