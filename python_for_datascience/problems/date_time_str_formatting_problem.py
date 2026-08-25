from datetime import datetime,timedelta

orders = [
                {"order_date": "2023-11-01 10:00:00", "expected_days": 3, "actual_date": "2023-11-04 15:00:00"},
                {"order_date": "2023-11-02 14:30:00", "expected_days": 2, "actual_date": "2023-11-05 16:45:00"},
                {"order_date": "2023-11-03 09:15:00", "expected_days": 5, "actual_date": "2023-11-08 08:00:00"},
                {"order_date": "2023-11-04 13:00:00", "expected_days": 1, "actual_date": "2023-11-05 12:00:00"}
            ]

for order in orders:

   order_d=datetime.strptime(order['order_date'], '%Y-%m-%d %H:%M:%S')
   expected_days=order['expected_days']
   exp_delivery_date=timedelta(order_d,days=expected_days)



