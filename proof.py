import hid


vid = 4292  # Reemplazar con tu vendor_id
pid = 6169  # Reemplazar con tu product_id
def connect():
    try:
        # Abrir conexión con el dispositivo
        device = hid.device()
        device.open(vid, pid)
        device.set_nonblocking(1)  # Configurar modo no bloqueante
        return device

    except OSError as e:
        print(f"Error al conectar con el dispositivo HID: {e}")
        return False