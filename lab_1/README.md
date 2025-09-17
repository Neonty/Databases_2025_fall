Airport – Flight (one-to-many)
Each flight departs from one airport and arrives at one airport, but an airport can handle many flights.

Airline – Flight (one-to-many)
Each flight is operated by one airline, but an airline can operate many flights.

Passenger – Booking (one-to-many)
Each booking belongs to one passenger, but a passenger can have many bookings.

Booking – Flight (many-to-many via FlightBooking)
A booking may include several flight legs, and each flight can have many bookings.

Booking – BookingChange (one-to-many)
Each booking can have many change records, but each change record belongs to one booking.

FlightBooking – BoardingPass (one-to-one)
Each reserved seat on a specific flight produces exactly one boarding pass.

FlightBooking – Baggage (one-to-many)
Each flight segment booking can have many pieces of baggage, but each baggage item belongs to one flight segment booking.

Baggage – BaggageCheck (one-to-one)
Each baggage item is checked once, and each baggage check refers to one baggage item.

Passenger – SecurityCheck (one-to-many)
Each security check record belongs to one passenger, but a passenger can undergo many security checks.