import random

def getDummyVenueData():
    venueData = [
        {
        "id": 1,
        "name": "The Fillmore",
        "city": "San Francisco",
        "state": "CA",
        "capacity": 120
        },
        {
            "id": 2,
            "name": "The Regency",
            "city": "San Francisco",
            "state": "CA",
            "capacity": 80
        },
        {
            "id": 3,
            "name": "The Paramount",
            "city": "Oakland",
            "state": "CA",
            "capacity": 150
        },
        {
            "id": 4,
            "name": "The Fox",
            "city": "Oakland",
            "state": "CA",
            "capacity": 72
        },
        {
            "id": 5,
            "name": "The Grand",
            "city": "Oakland",
            "state": "CA",
            "capacity": 100
        }]
    return venueData

def getDummyShowData():
    showData = [
        {
            "id": 1,
            "venue_id": 1,
            "name": "The Lion King",
            "time": "12:00 PM",
            "price": 150,
            "tickets": 42
        },
        {
            "id": 2,
            "venue_id": 1,
            "name": "Batman",
            "time": "3:00 PM",
            "price": 100,
            "tickets": 52
        },
        {
            "id": 3,
            "venue_id": 1,
            "name": "The Avengers",
            "time": "6:00 PM",
            "price": 120,
            "tickets": 0

        },
        {
            "id": 4,
            "venue_id": 1,
            "name": "The Matrix",
            "time": "9:00 PM",
            "price": 350,
            "tickets": 12
        },
        {
            "id": 5,
            "venue_id": 2,
            "name": "The Lion King",
            "time": "12:00 PM",
            "price": 150,
            "tickets": 15
        },
        {
            "id": 6,
            "venue_id": 2,
            "name": "Batman",
            "time": "3:00 PM",
            "price": 100,
            "tickets": 5
        },
        {
            "id": 7,
            "venue_id": 2,
            "name": "The Avengers",
            "time": "6:00 PM",
            "price": 120,
            "tickets": 64
        },
        {
            "id": 8,
            "venue_id": 2,
            "name": "The Matrix",
            "time": "9:00 PM",
            "price": 350,
            "tickets": 0
        },
        {
            "id": 9,
            "venue_id": 3,
            "name": "The Lion King",
            "time": "12:00 PM",
            "price": 150,
            "tickets": 15
        },
        {
            "id": 10,
            "venue_id": 3,
            "name": "Batman",
            "time": "3:00 PM",
            "price": 100,
            "tickets": 8
        },
        {
            "id": 11,
            "venue_id": 3,
            "name": "The Avengers",
            "time": "6:00 PM",
            "price": 120
        },
        {
            "id": 12,
            "venue_id": 3,
            "name": "The Matrix",
            "time": "9:00 PM",
            "price": 350,
            "tickets": 25
        },
        {
            "id": 13,
            "venue_id": 4,
            "name": "The Lion King",
            "time": "12:00 PM",
            "price": 150,
            "tickets": 0
        },
        {
            "id": 14,
            "venue_id": 4,
            "name": "Batman",
            "time": "3:00 PM",
            "price": 100,
            "tickets": 3
        },
        {
            "id": 15,
            "venue_id": 4,
            "name": "The Avengers",
            "time": "6:00 PM",
            "price": 120,
            "tickets": 0
        },
        {
            "id": 16,
            "venue_id": 4,
            "name": "The Matrix",
            "time": "9:00 PM",
            "price": 350,
            "tickets": 0
        },
        {
            "id": 17,
            "venue_id": 5,
            "name": "The Lion King",
            "time": "12:00 PM",
            "price": 150,
            "tickets": 26
        },
        {
            "id": 18,
            "venue_id": 5,
            "name": "Batman",
            "time": "3:00 PM",
            "price": 100,
            "tickets": 63
        },
        {
            "id": 19,
            "venue_id": 5,
            "name": "The Avengers",
            "time": "6:00 PM",
            "price": 120,
            "tickets": 23
        },
        {
            "id": 20,
            "venue_id": 5,
            "name": "The Matrix",
            "time": "9:00 PM",
            "price": 350,
            "tickets": 1
        },

    ]
    return showData

def getDummyBookingData():
    '''
    {
        "id": int,
        "user_id": int,
        "venue_id": int,
        "show_id": int,
        "num_tickets": int,
        "total_price": int
    }
    '''
    bookingData = []
    for i in range(10):
        booking = {
                    "id": i+1,
                    "user_id": random.randint(1, 3),
                    "venue_id": random.randint(1, 5),
                    "show_id": random.randint(1, 20),
                    "num_tickets": random.randint(1, 10),
                    "total_price": random.randint(150, 1000)
                }
        bookingData.append(booking)
    return bookingData
    

if __name__ == '__main__':
    # print(getDummyVenueData())
    # print(getDummyShowData())
    print(getDummyBookingData())