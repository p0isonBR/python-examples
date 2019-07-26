from sinric import SinricPro
from credentials import apiKey, deviceId
from sinric import SinricProUdp


def power_state(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state.get('state'))
    return True, state.get('state')


def set_brightness(did, state):
    # Alexa set device brightness to 40%
    print(did, 'BrightnessLevel : ', state)
    return True, state


def adjust_brightness(did, state):
    # Alexa increase/decrease device brightness by 44
    print(did, 'AdjustBrightnessLevel : ', state)

    return True, state


def set_color(did, r, g, b):
    # Alexa set device color to Red/Green
    print(did, 'Red: ', r, 'Green: ', g, 'Blue : ', b)

    return True


def set_color_temperature(did, value):
    print(did, value)
    return True


def increase_color_temperature(deviceId, value):
    return True, value


def decrease_color_temperature(deviceId, value):
    return True, value


callbacks = {
    'powerState': power_state,
    'setBrightness': set_brightness,
    'adjustBrightness': adjust_brightness,
    'setColor': set_color,
    'setColorTemperature': set_color_temperature,
    'increaseColorTemperature': increase_color_temperature,
    'decreaseColorTemperature': decrease_color_temperature
}

if __name__ == '__main__':
    client = SinricPro(apiKey, deviceId, callbacks, enable_trace=False)
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
