import configparser
from pathlib import Path
import sys


class AppConfig:
    config = configparser.ConfigParser()
    envId = None
    env = None
    envUrl = None

    def __init__(self, envId) -> None:
        path2cfg = Path(sys.argv[0]).name.replace(
            '.py', '.ini')  # use config file with extension .ini
        if not Path(path2cfg).is_file():
            raise Exception('The app config file does not exist: ' + path2cfg)

        self.config.read(path2cfg)
        result = list(
            filter(lambda section: (section == envId), self.config.sections()))

        if not result:
            raise Exception('There is no configuration for ' + envId + ' in ' +
                            path2cfg)

        self.envId = envId
        self.env = self.config[envId]
        self.envUrl = self.env['protocol'] + '//' + self.env['host']
        print('... selected env: ' + self.envId)
