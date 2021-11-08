from flask import Flask, request, jsonify
from redis import Redis, StrictRedis, RedisError


# Create the Flask server
app = Flask(__name__)
#redis = Redis(host="redis-server")
redis = StrictRedis('redis-server', 6379, charset="utf-8", decode_responses=True)


# Make a simple route to respond to '/'
@app.route('/')
def hello():
    return jsonify(
        output="Hello World!"
    )

@app.route('/keyval', methods=['PUT'])
def handle_put():

    client_data = request.get_json()



# Example to handle a request payload in JSON
@app.route('/keyval', methods=['POST'])
def handle_post():
    
    client_data = request.get_json()
    if client_data.get('key'):
        k = client_data.get('key')
    else:
        k = ''
        err_string = "Invalid JSON from client: No Key found"
        return jsonify(
            key=k,
            value=v,
            command=f"CREATE {k}/{v}", 
            result=False,
            error=err_string
        ), 400

    v = client_data['value']

    # Now we have the data from the client, let's store it in Redis

    # First, check if this key is already there
    if redis.exists(k):
        # OOps, the key already exists
        # send a 409 back with the JSON
        return jsonify(), 409

    redis_result = redis.set(k, v)
    if redis_result == False:
        err_string = "There was a problem writing to the db"
    else:
        err_string = None


    return jsonify(
        key=k,
        value=v,
        command=f"CREATE {k}/{v}", 
        result=redis_result,
        error=err_string
    ), 400

