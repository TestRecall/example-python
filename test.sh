#!/bin/bash

export TR_UPLOAD_TOKEN=XCRybxclcyqFCmehpkorenPfEtKrzO

trap 'testrecall-reporter' EXIT
pytest --junit-xml=report.xml
