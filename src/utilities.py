import time

import ujson as json


class DeviceSettings:
    secrets_fp = ""
    settings_fp = ""

    device_name = ""
    advertising_interval_ms = ""
    controller_poll_interval_ms = ""
    sleep_duration_s = ""
    cache_size_bytes = ""
    last_network_ssid = ""
    last_network_pass = ""

    def __init__(self, p_settings=None):
        if p_settings is None:
            p_settings = {'secrets_fp': "src/secrets.json", 'settings_fp': "src/device_settings.json",
                          'device_name': "Satyr", 'advertising_interval_ms': 250000,
                          "controller_poll_interval_ms": 5500, 'sleep_duration_s': 5, 'cache_size_bytes': 100000,
                          'last_network_ssid': "", 'last_network_pass': ""}

        for attr in p_settings:
            self.__setattr__(attr, p_settings[attr])

        self._update_config_file()

    @staticmethod
    def initialize_from_files(p_config_fp=None, p_secrets_fp=None):
        """
        This method should take a filepath and return a DeviceSettings
        object after initializing it from a file
        :param p_secrets_fp:
        :param p_config_fp:
        :return: A DeviceSettings object initialized with values contained in the provided files
        """

        if (p_config_fp is None) or (p_secrets_fp is None):
            return DeviceSettings()
        else:
            try:
                # Load settings
                with open("src/device_settings.json", 'r') as file:
                    settings = json.load(file)
                # Load secrets
                with open("src/secrets.json", 'r') as file:
                    secrets = json.load(file)

                settings.update(secrets)
                settings.update({'secrets_fp': p_config_fp, 'settings_fp': p_secrets_fp})
                return DeviceSettings(p_settings=settings)

            except ValueError:
                print(f'Failed to initialize with settings or secrets at provided paths:\n'
                      f'Settings FP: {p_config_fp}\n'
                      f'Secrets FP: {p_secrets_fp}')
                return DeviceSettings()
            except NotImplementedError as e:
                raise e

    def _update_config_file(self):
        # TODO: Implement _update_config_file for DeviceSettings
        data = self.__dict__

        secrets = {k: v for k, v in data if (k == 'last_network_ssid') or (k == 'last_network_pass')}
        data = {k: v for k, v in data if not ((k == 'last_network_ssid') or (k == 'last_network_pass'))}

        # Write settings
        with open(self.settings_fp, 'w') as file:
            json.dump(data, file)
        # Write secrets
        with open(self.secrets_fp, 'w') as file:
            json.dump(secrets, file)


def do_startup_blink(p_pin):
    i = 0
    p_pin.value(0)
    while i < 3:
        i += 1
        p_pin.value(1)
        time.sleep(0.2)
        p_pin.value(0)
        time.sleep(0.2)