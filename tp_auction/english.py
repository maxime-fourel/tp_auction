# pylint: disable=missing-docstring

from itertools import count

from utils import Cli


class EnglishAuction():


    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()

    def play(self):
        # Input opening bid
        self.cli.display('Started auction of type: English')
        opening_bid = self.cli.prompt('Please enter the amount for the opening bid:')
        opening_bid = int(opening_bid)
        self.cli.display(f"Opening bid is: {opening_bid}")

        # Input bidders
        bidders = []
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
            )
            if not bidder:
                break
            bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")

        # Collect bids

        self.current_bid=opening_bid
        self.current_winner = None
        i=0
        fin=1
        while i<fin:
            for bidder in bidders:
                rawbid = self.cli.prompt(
                                f"Standing bid is {self.current_bid}. {bidder} bids:"
                            )
                if not rawbid or rawbid==str(self.current_bid):
                    continue
                bid=int(rawbid) 
                
                if bid > self.current_bid:
                    self.current_bid = bid
                    self.current_winner = bidder
                    if i+1==fin:
                        fin+=1 #si il y a une enchère dans le dernier tour, on augmente le nombre de tour total 

                    
            i+=1 #nombre de tours

        self.cli.display("\n~~~~~~~~\n")
        return self.cli.display(f"Winner is {self.current_winner}. Winning bid is {self.current_bid}.")
                        
        # Display winner
        


if __name__ == "__main__":
    auction = EnglishAuction()
    auction.play()
