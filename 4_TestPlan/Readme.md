# TEST PLAN:

## High Level Test Plan:

| **Test ID** | **Description**                                              | **I/P** | **O/P** |**Type Of Test**  |          
|-------------|--------------------------------------------------------------|------------|-------------| ----------------|      
| HL_01 | User shall be able to select one from the menu window | By choosing 1 or 2 for the required operation | User should be able to select either the ticket booking or PNR status | Implemented |
| HL_02 | User shall be able to enter Booking window | Source location, destination location and the privilege details | Confirmation message | Implemented |
| HL_03 | User shall be able to enter PNR status checking window | PNR number | Ticket information like the source location, destination location information along with distance, time need to be given | Implemented |


## Low Level Test Plan:
| **Test ID** | **Description**                                              | **I/P** | **O/P** |**Type Of Test**  |    
|-------------|-----------------------------|------------|-------------|------------------|
| LR01 | From the menu the passenger must be able to select any one | Select 1 or 2 for the required operation | Success | Implemented |
| LR02 | In the booking window the passenger must be able to enter source location, destination location and the privilege details | Yes/No | Success | Implemented |
| LR03 | After confirming whether to book the ticket or not, Conformation message has to be generated with PNR number | Price of ticket  |Success | Implemented |
| LR04 | Passenger must be able to enter PNR number after PNR status window appears | Source and Destination location and arrival distance | Success | Implemented |
| LR05 | Ticket information like the source location, destination location information along with distance, time need to be given | Yes/No | Success | Implemented |
| LR06 | The passenger must be able to come out of the window by pressing any key | Main menu |Success | Implemented |