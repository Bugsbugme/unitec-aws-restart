import redis

con = redis.Redis()

con.keys()

con.set("age", "32")
