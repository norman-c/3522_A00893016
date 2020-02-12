"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self, bidders):
        self.bidders = bidders
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        pass

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for b in self.bidders:
            b(self)

    def accept_bid(self, bid, bidder="Starting bid"):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        self._highest_bid = bid
        self._highest_bidder = bidder
        self._notify_bidders()

    @property
    def highest_bid(self):
        return self._highest_bid

    @property
    def highest_bidder(self):
        return self._highest_bidder


class Bidder:

    def __init__(self, name, money=100, threat_chance=0.20, bid_increase=1.1):
        self.name = name
        self.threat_chance = threat_chance
        self.money = money
        self.bid_increase = bid_increase
        self.highest_bid = 0

    def __call__(self, auctioneer):
        if self.threat_chance > random.random() and self.money > auctioneer.highest_bid and auctioneer.highest_bidder is not self:
            this_bid = auctioneer.highest_bid * self.bid_increase
            self.highest_bid = this_bid
            print(self.name + " bidded " + str(this_bid) +
                  " in response to " + str(auctioneer.highest_bidder) + "'s bid of " + str(auctioneer.highest_bid))
            auctioneer.accept_bid(this_bid, self)

    def __str__(self):
        return self.name

    # def notify(self, auctioneer):
    #     if self.threat_chance > random.random():
    #         self.__call__(auctioneer)


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, auctioneer):
        self.auctioneer = auctioneer

    def simulate_auction(self, item, start_price):
        self.auctioneer.accept_bid(start_price)
        print("\nThe winner of the auction is: " + str(self.auctioneer.highest_bidder) + " at $" + str(self.auctioneer.highest_bid)+"\n")
        print("Highest Bids Per Bidder")
        for b in self.auctioneer.bidders:
            print("Bidder: " + str(b) + "  Highest Bid: $" + str(b.highest_bid))


def main():
    bidders = []

    Hardcoding the bidders.
    bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
    bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
    bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
    bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
    bidders.append(Bidder("Scott", 4000, random.random(), 2))

    # user_input = None
    # item_name = input("Enter name of item")
    # item_price = int(input("Enter the starting price"))
    # num_bidders = int(input("Enter number of bidders"))
    # for



    this_auctioneer = Auctioneer(bidders)

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(this_auctioneer)
    my_auction.simulate_auction("Antique Vase", 100)


if __name__ == '__main__':
    main()
