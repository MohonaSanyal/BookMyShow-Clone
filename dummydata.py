def getDummyData():
    '''
    data schema:
    showData = [
        {
            "id": str,
            "Venue": str,
            "City": str,
            "State": str,
            "Movies": [
                {
                    "id": str,
                    "Name": str,
                    "Date": str,
                    "Time": str,
                    "Duration": str,
                    "Hall": str,
                    "Price": str,
                    "Tickets": int
                }]
        }
        ]         
    '''
    showData = [
        {
            "id": "V1",
            "Venue": "The Fillmore",
            "City": "San Francisco",
            "State": "CA",
            "Movies": [
                {
                    "id": "S1",
                    "Name": "The Lion King",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 30 Minutes",
                    "Hall": "Hall A",
                    "Price": "$30",
                    "Tickets": 110
                },
                {
                    "id": "S2",
                    "Name": "Batman",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 20 Minutes",
                    "Hall": "Hall C",
                    "Price": "$25",
                    "Tickets": 24
                },

                {
                    "id": "S3",
                    "Name": "The Avengers",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 30 Minutes",
                    "Hall": "Hall B",
                    "Price": "$30",
                    "Tickets": 52
                },
                {
                    "id": "S4",
                    "Name": "The Matrix",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 30 Minutes",
                    "Hall": "Hall B",
                    "Price": "$30",
                    "Tickets": 4
                }
            ]
        },
        {
            "id": "V2",
            "Venue": "The Regency",
            "City": "San Francisco",
            "State": "CA",
            "Movies": [
                {
                    "id": "S5",
                    "Name": "The Lion King",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 30 Minutes",
                    "Hall": "Hall A",
                    "Price": "$30",
                    "Tickets": 56
                },
                {
                    "id": "S6",
                    "Name": "Batman",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 20 Minutes",
                    "Hall": "Hall C",
                    "Price": "$25",
                    "Tickets": 0
                },
                {
                    "id": "S7",
                    "Name": "The Avengers",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 30 Minutes",
                    "Hall": "Hall B",
                    "Price": "$30",
                    "Tickets": 36
                },
                {
                    "id": "S8",
                    "Name": "The Matrix",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 30 Minutes",
                    "Hall": "Hall B",
                    "Price": "$30",
                    "Tickets": 53
                }
            ]
        },
        {
            "id": "V3",
            "Venue": "The Paramount",
            "City": "Oakland",
            "State": "CA",
            "Movies": [
                {
                    "id": "S9",
                    "Name": "The Lion King",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 30 Minutes",
                    "Hall": "Hall A",
                    "Price": "$30",
                    "Tickets": 12
                },
                {
                    "id": "S10",
                    "Name": "Batman",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 20 Minutes",
                    "Hall": "Hall C",
                    "Price": "$25",
                    "Tickets": 53
                },
                {
                    "id": "S11",
                    "Name": "The Avengers",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 30 Minutes",
                    "Hall": "Hall B",
                    "Price": "$30",
                    "Tickets": 0
                },
                {
                    "id": "S12",
                    "Name": "The Matrix",
                    "Date": "2019-01-01",
                    "Time": "20:00",
                    "Duration": "2 Hours 30 Minutes",
                    "Hall": "Hall B",
                    "Price": "$30",
                    "Tickets": 23
                }
            ]
        }
    ]
    return showData

if __name__ == '__main__':
    print(getDummyData())