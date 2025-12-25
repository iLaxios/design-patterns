
from abc import ABC, abstractmethod
from typing import override
 
# a player with states, state as interface


class State(ABC):

    @abstractmethod
    def play(self, mediaplayer) -> None:
        pass

    @abstractmethod
    def pause(self, mediaplayer) -> None:
        pass


class PlayingState(State):

    @override
    def play(self, mediaplayer: "MediaPlayer") -> None:
        print("already playing...")

    @override
    def pause(self, mediaplayer: "MediaPlayer") -> None:
        print("pausing...")
        mediaplayer.setState(PausedState())

class PausedState(State):

    @override
    def play(self, mediaplayer) -> None:
        print("playing...")
        mediaplayer.setState(PlayingState())

    @override
    def pause(self, mediaplayer) -> None:
        print("already pausing...")


class MediaPlayer:

    def __init__(self):
        self._currentState: State = PausedState()
    

    def setState(self, state: State):
        self._currentState = state
    
    def pressPlay(self) -> None:
        self._currentState.play(self)
    
    def pressPause(self) -> None:
        self._currentState.pause(self)


if __name__ == "__main__":
    mp: MediaPlayer = MediaPlayer()
    mp.pressPlay()

    mp.pressPlay()
    mp.pressPause()
    mp.pressPause()