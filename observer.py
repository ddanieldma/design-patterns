class YoutubeChannel:
    # Inicia o canal apenas com o nome e nenhum inscrito
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    # Inscreve alguém no canal
    def subscribe(self, sub):
        # Adicionando o inscrito na lista
        self.subscribers.append(sub)

    # Notifica todos os inscritos
    def notify(self, event):
        # percorrendo a lista
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)

from abc import ABC, abstractmethod

class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, event):
        pass

class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channel, event):
        print(f"User {self.name} received notification from {channel}: {event}")

if __name__ == "__main__":
    # Criando um canal do yt
    channel = YoutubeChannel("neetcode")

    # Adicionando alguns inscritos
    channel.subscribe(YoutubeUser("sub1"))
    channel.subscribe(YoutubeUser("sub2"))
    channel.subscribe(YoutubeUser("sub3"))

    # Mandando notificação
    channel.notify("A new video released!")