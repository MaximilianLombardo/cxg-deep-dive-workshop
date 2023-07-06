https://cellxgene.cziscience.com/e/31b49393-4485-4998-9ef4-33e03c4c1789.cxg/#!/bin/bash

#python screenshot_script.py -o ~/Desktop/TestOutput.png "https://cellxgene.cziscience.com"

#python screenshot_plus.py --width 3840 --height 2160 --crop-x 0 --crop-y 0 --crop-width 3840 --crop-height 2160 -o ~/Desktop/TestOutput.png "https://cellxgene.cziscience.com"

python screenshot_plus.py --width 3200 --height 1800 -o ~/Desktop/TestOutputFull.png "https://cellxgene.cziscience.com/e/31b49393-4485-4998-9ef4-33e03c4c1789.cxg/"

python screenshotFull.py -o ~/Desktop/TestOutputFullLength.png "https://cellxgene.cziscience.com"

#HTML Elements
#python screenshot_html.py --display-tree "https://cellxgene.cziscience.com"

python screenshot_html.py "https://cellxgene.cziscience.com/e/31b49393-4485-4998-9ef4-33e03c4c1789.cxg/"
