import argparse

class AppArgs:
    parser = argparse.ArgumentParser(description='ES Smoke Tester Tool')
    parser.add_argument('-v','--verbose', action='store_true', help='Control verbosity output')
    parser.add_argument('-e','--env', default='dev', help="specify target environment. The default is 'dev'")
    args = None

    def __init__(self) -> None:
        self.args = self.parser.parse_args()

    
