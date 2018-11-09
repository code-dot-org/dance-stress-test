# Dance stress tests

Runs Dance Party against real iOS and Android devices using AWS Device Farm.

## Running on AWS Device Farm

_Based on [this setup guide](https://github.com/aws-samples/aws-device-farm-sample-web-app-using-appium-python) so check there if you get lost._

### System Dependencies

1. Install Python 2

1. Install [`pip`](https://pip.pypa.io/en/stable/installing/)
   
   For Ubuntu use the `python-pip` package:
   ```bash
   sudo apt install python-pip
   ```
   
1. Install python [virtualenv](https://pypi.org/project/virtualenv/)

   ```bash
   pip install virtualenv
   ```

### Project setup

1. Clone this repo

   ```bash
   git clone https://github.com/code-dot-org/dance-stress-test.git
   cd dance-stress-test
   ```

1. Create a virtualenv workspace

   ```bash
   virtualenv .
   ```
   
1. Active your workspace in your current terminal

   You'll need to do this each time you open a new interactive terminal session for this project.
   
   ```bash
   source bin/activate
   ```
   
1. Install additional project dependencies into your workspace

   ```bash
   pip install pytest
   pip install Appium-Python-Client
   ```
   
1. Verify you can load and list tests

   ```bash
   py.test --collect-only tests
   ```

### Running tests on Device Farm

1. Run the `buildzip` script to generate a package for upload to Device Farm

    ```bash
    ./buildzip
    # Expect output to end with:
    # 2.0M	test_bundle.zip
    ```
    
2. Sign into AWS Console and open our AWS Device Farm project [here](https://us-west-2.console.aws.amazon.com/devicefarm/home?region=us-east-1#/projects/f720d748-5279-410f-8144-a6c7be46fd63/runs).

   At "Choose your application" pick "Test a web application."  The run name is just a label.
   
   At "Configure" pick "Appium Python" and upload the test_bundle.zip you just generated.  After the zip file is processed more settings will pop up - use "Run your test in a custom environment" and the default YAML spec.
   
   At "Select devices" use whatever device pool you like - I've been using iPhone 5s and Samsung Galaxy S4.
   
   At "Review and start run" use a 30 minute timeout.


## Local testing

Not solved yet! This is more difficult than it looks
