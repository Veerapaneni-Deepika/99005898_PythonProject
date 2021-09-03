# Ticket Booking System

Ticket Reservation System project is written in Python. This system consists of basic function which includes reservation and to check pnr status.

While reserving tickets, the user has to enter the number of tickets and the user's details. The system asks for a certain number of inputs depending upon the number of tickets entered by the user. In this System, the user can check for pnr status. This system provides one of the simplest reservation of ticket.

## Advantages:

* In this simple system, a person can view all reserve tickets easily.
* This is a simple console based system which is very easy to use and understand.

## Applications:

* This system can be used in flight management system and railway ticket booking system.

## High Level Requirements:

| ID | Description | Category | Status |
| --- | --- | --- | --- |
| HL_01 | User shall be able to select one from the menu window | Technical | Implemented |
| HL_02 | User shall be able to enter Booking window | Technical | Implemented |
| HL_03 | User shall be able to enter PNR status checking window | Technical | Implemented |
| HL_04 | Update the PNR number after Booking | Implemented |

## Low Level Requirements:
| ID | Description | HLR ID | Status(Implemented/Future)|
| --- | --- | --- | --- |
| LR01 | From the menu the passenger must be able to select any one | HL_01 | Implemented |
| LR02 | In the booking window the passenger must be able to enter source location, destination location and the privilege details | HR_02 | Implemented |
| LR03 | After confirming whether to book the ticket or not, Conformation message has to be generated with PNR number | HR_02 | Implemented |
| LR04 | Passenger must be able to enter PNR number after PNR status window appears | HR_03 | Implemented |
| LR05 | Ticket information like the source location, destination location information along with distance, time need to be given| HR_03 | Implemented |
| LR06 | The passenger must be able to come out of the window by pressing any key | HL_04 | Implemented |