import configparser
from pathlib import Path



class AppConfig:
    path2cfg = '/Users/eugene/projects/ML/smoke-tester/smoke-tester.cfg'
    if not Path(path2cfg).is_file():
        raise Exception('Specified file does not exist')
 
    config = configparser.ConfigParser()

    def __init__(self, envId) -> None: 
        self.config.read(self.path2cfg)
        result = list(filter(lambda section: (section == envId), self.config.sections()))
        print(result)
        if not result:
            raise Exception('There is no configuration for ' + envId+ ' in ' + self.path2cfg)


    # def getInstance(self) -> configparser.ConfigParser():
    #     return self.config
