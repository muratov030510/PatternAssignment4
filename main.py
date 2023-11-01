from abc import ABCMeta, abstractmethod

class Publisher(metaclass=ABCMeta):
    "The Publisher Interface"
    @abstractmethod
    def register(subscriber):
        "The registration method"
    @abstractmethod
    def unregister(subscriber):
        "The unregistration method"
    @abstractmethod
    def notify(subscriber):
        "The notification method"

class NewsAgency(Publisher):
    "The Publisher (Observable)"
    def __init__(self):
        self._subscribers = set()

    def register(self, subscriber):
        self._subscribers.add(subscriber)

    def unregister(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, *args):
        for subscriber in self._subscribers:
            subscriber.update(self, *args)

class Subscriber(metaclass=ABCMeta):
    "A method for the Subscriber to implement"
    @abstractmethod
    def update(publisher, *args):
        "Receive updates"

class NewsSubscriber(Subscriber):
    "The concrete subscriber"
    def __init__(self, publisher):
        publisher.register(self)

    def update(self, publisher, *args):
        print(f"Subscriber ID: {id(self)} received news: {args}")

# The Client
NEWS_AGENCY = NewsAgency()
SUBSCRIBER_A = NewsSubscriber(NEWS_AGENCY)
SUBSCRIBER_B = NewsSubscriber(NEWS_AGENCY)
NEWS_AGENCY.notify("Breaking News", "Important updates")
NEWS_AGENCY.unregister(SUBSCRIBER_B)
NEWS_AGENCY.notify("More News", "Exciting events")