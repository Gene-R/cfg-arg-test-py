#!/usr/bin/env python3
import appconfig
import appargs


args = appargs.AppArgs().args
config = appconfig.AppConfig(args.env).config

print (config[args.env].get('protocol'))