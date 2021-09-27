# Context

A is an artist who creates digital art of sea shells floating in space. A also uploads her art on Instagram. B is a frequent NFT user. B sees A's art and decides to tokenise it and list it for sale in an NFT Marketplace Artation, without A's consent and with the intention of wrongfully gaining profit from the same. B calls it *seas-shells*

A's friend G, a collector on Artnation see's A's art and notifies her. Upset and furious, A tries to contact Artnation to take down A's art. Since A is an amateur and fairly unknown artist, and as B is a frequent user of its Artnation's platform, Artnation says it would take time for them to verify the claims. 

Worried, A consults a lawyer on possible remedies. The lawyer informs A that she may initiate a case in Court against both Artnation and B. However, since A lives in Kathmandu and Artnation is registered in San Jose, the costs and complications arising out of this would be high. Alternatively, A could have the dispute resolved via cheaper and more time sensitive arbitration, as the terms and conditions of Artnation provides for this. However, the terms also mandate the arbitration to be conducted in the US, and 1000s of dollars to be paid in travel, accommodation and arbitration administration fee, which A cannot afford. 

Disillusioned, A decides to wait for Artnation to get back, at the mercy of their discretionary power to grant remedies.

## Resolutio to the rescue
Resolutio is a blockchain-based dispute resolution mechanism for NFTs. It is built on Algorand. It is a great alternative to the current arbitration process that is costly, lengthy and extremely cumbersome. Resolutio aims to make the dispute resolution process affordable to the artists, faster and secure to a great extent.

## Proposed Mechanism
In Resolutio platform, A has the liberty to have their issue heard and resolved by the NFT Community in a faster, cheaper and secured way. In a higher level, the mechanism consists of the following steps.

- Artist A logs into the Platform using their wallet 
- A stakes an amount using Algorand Standard Asset (ASA) and raises an issue for initiating the dispute resolution process
- A provides the following information in support of their claim
    - Description of the NFT in question
        - Name of the NFT
        - Status of the NFT (listed/sold/pending etc.)
        - Provides proof of it's origin including when and how it was created
        
    - Nature of dispute
        - As example, Their artwork was tokenised without their consent and listed in the NFT Marketplace
        - The date the alleged theif (B) minted the NFT 
        - Whether B has been notified and warned. If yes, how they responded to the warning.

    - Link to alleged party's profile in the NFT platform
- Notification sent to alleged party B notifying that there is a dispute resolution claimed against them
- Resolusio platform mandates a reply from B addressing the claim within a pre-defined deadline. The response is recieved by the platform once sent by B.
- Summary of dispute is sent to NFT Community
- Arbitrators are randomly selected using Verifiable Random Function
- The stake sent from artist A will be splitted between the selected arbitrators. However, the group transaction will not be complete until all the arbitrators cast their votes **for** or **against** the artist. The artist can take their stake back at any times before the group transaction is complete.
- Majority vote will decide who won the resolution case. If the artist A wins, either the NFT has to be returned, burnt or A will have to be compensated through Algorand Standard Asset (ASA). 


## Codebase 
The /scripts directory contains scripts for the base smart contract and arbitration voting of a simpler and basic version of the proposed mechanism. 
- **resolutio_smart_contract.py** is the script for the artist to use for initiating the dispute resolution. The artist will connect their wallet using AlgodClient and specify the transaction amount and the number of arbitrators amongst whome the amount will be splitted. create_split_transaction() function will make sure the amount is properly splitted between the arbitrators only if all of them finish casting their votes. Right now the logic for vote casting checking has not been implemented due to time constraint. 
- **arbitration_voting.py** is the script for the arbitrators to cast their votes either for or against the artist. Each arbitrator's 
voting status (Voted or Not Voted) is added to global storage. If the vote is for the Artist, an increment is added to Artist's local storage.
If the vote is against the Artist, an increment is added to the alleged Offender's local storage. 
