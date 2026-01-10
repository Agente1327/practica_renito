import os
from todor import app  # importa tu app desde el paquete todor

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
