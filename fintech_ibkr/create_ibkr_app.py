
from fintech_ibkr.ibkr_app import ibkr_app
from datetime import datetime
import time
import threading

# If you want different default values, configure it here.
default_hostname = '127.0.0.1'
default_port = 7497
default_client_id = 10645 # can set and use your Master Client ID
timeout_sec = 5

def create_ibkr_app(hostname = default_hostname, port = default_port,
                    client_id = default_client_id):

    app = ibkr_app()
    app.connect(hostname, int(port), int(client_id))

    start_time = datetime.now()
    while not app.isConnected():
        time.sleep(0.01)
        if (datetime.now() - start_time).seconds > timeout_sec:
            app.disconnect()
            raise Exception(
                "fetch_managed_accounts",
                "timeout",
                "couldn't connect to IBKR"
            )

    def run_loop():
        app.run()

    api_thread = threading.Thread(target=run_loop, daemon=True)
    api_thread.start()
    while app.next_valid_id is None:
        time.sleep(0.01)

    return app
