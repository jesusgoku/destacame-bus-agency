select driver_id, start_time, end_time from control_itinerary as ci WHERE NOT ('2018-09-10 16:00:00' <= ci.end_time AND '2018-09-10 18:00:00' >=  ci.start_time);

